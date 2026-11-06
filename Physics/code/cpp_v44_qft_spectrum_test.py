# cpp_v44_qft_spectrum_test.py
# Протокол P-QFT-1 (v1.1): спектр, евклидов пропагатор Sigma = Pi^{-1},
# причинный коммутатор Паули-Йоста Delta_PJ = i(G_ret - G_adv),
# граничная масса Шура M_eff = Tr(K_int) и сдвиг граничной щели d_gamma
# на причинных скелетах CPP v4.4 (Hypercube, Minkowski sprinklings, KR, Random DAG).
#
# Зависимости: cpp_v44_reference.py (в той же директории или в PYTHONPATH).

import argparse
from datetime import datetime
import os
import sys

import numpy as np
from scipy.linalg import eigvals
from scipy.sparse.csgraph import shortest_path

import cpp_v44_reference as cpp

# Детерминированные смещения сидов (вместо нестабильного hash(name))
_ENSEMBLE_SEED_OFFSET = {
    "Hypercube_2D": 101,
    "Minkowski_2D": 202,
    "Minkowski_3D": 303,
    "KR_T3": 404,
    "KR_T2": 505,
    "Random_DAG": 606,
}


# =====================================================================
# 1. ПОСТРОЕНИЕ ЧАСТИЧНЫХ ПОРЯДКОВ И РЕДУКЦИЯ ХАССЕ
# =====================================================================

def transitive_reduction_from_poset(C):
    """Транзитивная редукция Хассе R из булевой матрицы строгого порядка C."""
    C = (np.asarray(C) > 0).astype(np.int64)
    two_or_more = (C @ C) > 0
    R = (C > 0) & (~two_or_more)
    return R.astype(np.int64)


def causal_closure_from_hasse(R):
    """Восстановление полного строгого порядка C (x < y) из матрицы Хассе R."""
    R = np.asarray(R, dtype=float)
    N = len(R)
    C = (np.linalg.inv(np.eye(N) - R) - np.eye(N)) > 0.5
    return C.astype(np.int64)


def minkowski_sprinkling_hasse(N, d=2, seed=0):
    """Пуассоновский посев N событий в ромб Александрова в M^{1, d-1}."""
    rng = np.random.default_rng(seed)
    pts = []
    while len(pts) < N:
        batch = rng.uniform(-0.5, 0.5, size=(4 * N, d))
        t = batch[:, 0] + 0.5
        r_norm = np.linalg.norm(batch[:, 1:], axis=1) if d > 1 else np.zeros(len(batch))
        mask = r_norm <= np.minimum(t, 1.0 - t)
        for pt in batch[mask]:
            pts.append(np.concatenate([[pt[0] + 0.5], pt[1:]]))
            if len(pts) == N:
                break
    pts = np.array(pts[:N])
    order = np.argsort(pts[:, 0])
    pts = pts[order]
    dt = pts[None, :, 0] - pts[:, None, 0]
    if d > 1:
        dx = np.linalg.norm(pts[None, :, 1:] - pts[:, None, 1:], axis=2)
    else:
        dx = np.zeros((N, N))
    C = ((dt > dx) & (np.arange(N)[:, None] < np.arange(N)[None, :])).astype(np.int64)
    R = transitive_reduction_from_poset(C)
    return R, C


def kleitman_rothschild_hasse(N, layers=3, p_edge=0.5, seed=0):
    """Генератор двухслойных (T_2) и трёхслойных (T_3) порядков Клейтмана-Ротшильда."""
    rng = np.random.default_rng(seed)
    R0 = np.zeros((N, N), dtype=np.int64)
    if layers == 2:
        n1 = N // 2
        R0[:n1, n1:] = (rng.random((n1, N - n1)) < p_edge).astype(np.int64)
        return R0, R0.copy()
    if layers == 3:
        n1 = N // 4
        n2 = N // 2
        idx1 = slice(0, n1)
        idx2 = slice(n1, n1 + n2)
        idx3 = slice(n1 + n2, N)
        R0[idx1, idx2] = (rng.random((n1, n2)) < p_edge).astype(np.int64)
        R0[idx2, idx3] = (rng.random((n2, N - n1 - n2)) < p_edge).astype(np.int64)
        C = R0.copy()
        C[idx1, idx3] = 1
        R = transitive_reduction_from_poset(C)
        return R, C
    raise ValueError("layers must be 2 or 3")


# =====================================================================
# 2. СПЕКТР, ЕВКЛИДОВ ПРОПАГАТОР SIGMA И ПРИЧИННЫЙ КОММУТАТОР ПАУЛИ-ЙОСТА
# =====================================================================

def undirected_graph_distance(R):
    """Комбинаторное расстояние на неориентированном скелете R + R^T."""
    A = (R + R.T) > 0
    return shortest_path(A.astype(float), directed=False, unweighted=True)


def spectrum_of_pi(Pi):
    """Собственные значения эрмитовой матрицы Pi по возрастанию."""
    ev = np.linalg.eigvalsh(0.5 * (Pi + Pi.conj().T))
    return np.sort(np.real(ev))


def causal_pauli_jordan_propagators(R, Theta, m2=0.5):
    """
    Вычисление направленного запаздывающего пропагатора G_ret и эрмитова
    причинного коммутатора Паули-Йоста Delta_PJ на графе Хассе:
      Pi_ret := D_m - W,   D_m = m^2 I + D,   W = R * exp(i Theta),
      G_ret  := (D_m - W)^{-1} = D_m^{-1/2} (I - W_hop)^{-1} D_m^{-1/2},
      G_adv  := G_ret^dagger = (D_m - W^dagger)^{-1},
      Delta_PJ := i * (G_ret - G_adv).
    Свойства:
      1. G_ret[x, y] == 0 строго вне причинного конуса будущего (x not<= y).
      2. Delta_PJ эрмитова (Delta_PJ^dagger == Delta_PJ) и тождественно равна нулю
         на всех пространственноподобных (несравнимых) парах событий.
      3. При обращении причинности (R, Theta) -> (R^T, -Theta^T) знак Delta_PJ
         меняется на противоположный: Delta_PJ -> -Delta_PJ (аналогично Q_W в Лемме 2.4.1).
    """
    R = np.asarray(R, dtype=float)
    W = R * np.exp(1j * Theta)
    deg = (R + R.T).sum(axis=1)
    Dm = np.diag(m2 + deg)
    G_ret = np.linalg.inv(Dm - W)
    G_adv = G_ret.conj().T
    Delta_PJ = 1j * (G_ret - G_adv)
    return G_ret, Delta_PJ


def propagator_profiles(Mat, R, C, r_max=6):
    """
    Средний модуль |Mat_xy|, сгруппированный по графовому расстоянию r на скелете R+R^T
    и причинному типу пары:
      timelike  : x < y или y < x в частичном порядке C
      spacelike : x и y несравнимы в C
      all       : любая пара на расстоянии r
    """
    dist = undirected_graph_distance(R)
    absM = np.abs(Mat)

    C = (np.asarray(C) > 0).astype(np.int64)
    comparable = (C + C.T) > 0
    np.fill_diagonal(comparable, False)

    profiles = {"all": {}, "timelike": {}, "spacelike": {}}
    for r in range(1, r_max + 1):
        mask_r = (dist >= r - 0.5) & (dist < r + 0.5)
        np.fill_diagonal(mask_r, False)
        for key, type_mask in (
            ("all", np.ones_like(mask_r, dtype=bool)),
            ("timelike", comparable),
            ("spacelike", ~comparable),
        ):
            m = mask_r & type_mask
            if np.any(m):
                profiles[key][r] = float(np.mean(absM[m]))
            else:
                profiles[key][r] = float("nan")
    return profiles


def _compute_triad_gap_and_meff(Pi, Q, b, I, E, Gamma_scale=1.0):
    """Вычисление M_eff = Tr(K_int) и сдвига граничной щели d_gamma = gamma_bdry - gamma_bdry0."""
    if hasattr(cpp, "boundary_effective_gap"):
        out = cpp.boundary_effective_gap(Pi, Q, b, I, E, Gamma_scale=Gamma_scale)
        return float(out["M_eff"]), float(out["d_gamma"]), float(out["gamma_bdry"])

    blk = lambda u, v: Pi[np.ix_(u, v)]
    Pi_I, Pi_b, Pi_E = blk(I, I), blk(b, b), blk(E, E)
    K_int = blk(b, I) @ np.linalg.inv(Pi_I) @ blk(I, b)
    K_ext = blk(b, E) @ np.linalg.inv(Pi_E) @ blk(E, b)
    S_dA = Pi_b - K_int - K_ext
    S_0 = Pi_b - K_ext
    M_eff = float(np.real(np.trace(K_int)))
    nb = len(b)
    Gb = Gamma_scale * np.eye(nb)
    Qb = Q[np.ix_(b, b)]
    g_bdry = float(np.min(np.real(eigvals((Gb + Qb) @ S_dA))))
    g_bdry0 = float(np.min(np.real(eigvals((Gb + Qb) @ S_0))))
    return M_eff, float(g_bdry - g_bdry0), g_bdry


def triad_metrics_on_central_region(R, Theta, m2, beta=1.0, L_side=None):
    """
    Находит непустую триаду (I_A, dA, E_A) и вычисляет M_eff = Tr(K_int) и d_gamma.
    Для двухслойных/плотных графов (где индексные срезы не дают внутренней зоны I_A)
    использует замкнутые единичные шары B_1(x_0) = {x_0} U N(x_0), для которых x_0 in I_A
    гарантировано по определению границы.
    """
    N = len(R)
    side = L_side or int(round(np.sqrt(N)))
    candidates = []

    if side * side == N:
        coords = [(i // side, i % side) for i in range(N)]
        cx = cy = (side - 1) / 2.0
        for half in range(2, max(3, side // 2)):
            A = [
                i for i, (x, y) in enumerate(coords)
                if abs(x - cx) <= half + 1e-9 and abs(y - cy) <= half + 1e-9
            ]
            candidates.append(A)

    for lo, hi in [(N // 5, 4 * N // 5), (N // 4, 3 * N // 4), (N // 3, 2 * N // 3)]:
        candidates.append(list(range(lo, hi)))

    # Гарантированный резервный вариант: замкнутая 1-окрестность вершины умеренной степени
    A_sym = (R + R.T) > 0
    degs = A_sym.sum(axis=1)
    order_deg = np.argsort(np.abs(degs - np.median(degs)))
    for u0 in order_deg[:12]:
        if 1 <= degs[u0] <= N - 3:
            ball_1 = [int(u0)] + [int(v) for v in np.where(A_sym[u0])[0]]
            candidates.append(ball_1)

    Pi = cpp.magnetic_precision(R, Theta, m2=m2)
    Q = cpp.solenoidal_from_transport(R, Theta, beta=beta)

    for A in candidates:
        if len(A) < 2 or len(A) >= N:
            continue
        I, b, E, _ = cpp.partition_triad(R, A)
        if len(I) == 0 or len(b) == 0 or len(E) == 0:
            continue
        try:
            meff, d_gam, g_bdry = _compute_triad_gap_and_meff(Pi, Q, b, I, E)
            return meff, d_gam, g_bdry
        except Exception:
            continue
    return float("nan"), float("nan"), float("nan")


# =====================================================================
# 3. ОЦЕНКА ОДНОГО ЭКЗЕМПЛЯРА ГРАФА
# =====================================================================

def evaluate_qft_instance(R, C, rng, m2=0.5, theta_mode="flat", r_max=6):
    """
    Вычисляет спектр Pi, профили евклидова пропагатора Sigma = Pi^{-1},
    профили причинного коммутатора Паули-Йоста Delta_PJ, а также M_eff и d_gamma.
    """
    R = np.asarray(R, dtype=int)
    N = len(R)
    if theta_mode == "flat":
        Theta = np.zeros((N, N), dtype=float)
    elif theta_mode == "noise":
        Theta = (rng.normal(0.0, 0.1, size=(N, N)) % (2.0 * np.pi)) * (R > 0)
    else:
        Theta = rng.uniform(0.0, 2.0 * np.pi, size=(N, N)) * (R > 0)

    Pi = cpp.magnetic_precision(R, Theta, m2=m2)
    ev = spectrum_of_pi(Pi)
    logdet = float(np.linalg.slogdet(Pi)[1])
    Sigma = np.linalg.inv(Pi)
    _, Delta_PJ = causal_pauli_jordan_propagators(R, Theta, m2=m2)

    prof_sig = propagator_profiles(Sigma, R, C, r_max=r_max)
    prof_pj = propagator_profiles(Delta_PJ, R, C, r_max=r_max)
    meff, d_gamma, g_bdry = triad_metrics_on_central_region(R, Theta, m2=m2)

    # Максимальная утечка причинного коммутатора Паули-Йоста вне светового конуса
    C_bool = (np.asarray(C) > 0)
    spacelike_mask = ~(C_bool | C_bool.T)
    np.fill_diagonal(spacelike_mask, False)
    pj_spacelike_max = float(np.max(np.abs(Delta_PJ[spacelike_mask]))) if np.any(spacelike_mask) else 0.0

    return {
        "N": N,
        "m2": m2,
        "lambda_min": float(ev[0]),
        "lambda_max": float(ev[-1]),
        "lambda_2": float(ev[1]) if N > 1 else float(ev[0]),
        "gap": float(ev[1] - ev[0]) if N > 1 else 0.0,
        "logdet_Pi": logdet,
        "logdet_Pi_per_N": logdet / N,
        "G_all_1": prof_sig["all"].get(1, np.nan),
        "G_all_3": prof_sig["all"].get(3, np.nan),
        "G_time_3": prof_sig["timelike"].get(3, np.nan),
        "G_space_3": prof_sig["spacelike"].get(3, np.nan),
        "PJ_time_3": prof_pj["timelike"].get(3, np.nan),
        "PJ_space_max": pj_spacelike_max,
        "M_eff": meff,
        "d_gamma": d_gamma,
        "gamma_bdry": g_bdry,
        "ev": ev,
        "profiles_sigma": prof_sig,
        "profiles_pj": prof_pj,
    }


# =====================================================================
# 4. ДРАЙВЕРЫ БЛОКОВ A+D, B И C
# =====================================================================

def build_ensemble_graph(name, N, seed):
    if name == "Hypercube_2D":
        side = int(round(np.sqrt(N)))
        R, _ = cpp.directed_hypercube((side, side))
        C = causal_closure_from_hasse(R)
        return R, C
    if name == "Minkowski_2D":
        return minkowski_sprinkling_hasse(N, d=2, seed=seed)
    if name == "Minkowski_3D":
        return minkowski_sprinkling_hasse(N, d=3, seed=seed)
    if name == "KR_T3":
        return kleitman_rothschild_hasse(N, layers=3, seed=seed)
    if name == "KR_T2":
        return kleitman_rothschild_hasse(N, layers=2, seed=seed)
    if name == "Random_DAG":
        R = cpp._random_hasse(N, p=0.35, seed=seed)
        C = causal_closure_from_hasse(R)
        return R, C
    raise ValueError(f"Unknown ensemble: {name}")


def run_block_AD(
    N=64,
    n_seeds=10,
    m2=0.5,
    theta_mode="flat",
    seed_base=2000,
    verbose=True,
):
    """Блок A+D: спектр, евклидов Sigma vs причинный Паули-Йост и граничный сдвиг Шура."""
    ensembles = [
        "Hypercube_2D",
        "Minkowski_2D",
        "Minkowski_3D",
        "KR_T3",
        "KR_T2",
        "Random_DAG",
    ]
    stats = {e: [] for e in ensembles}

    for s in range(n_seeds):
        seed = seed_base + s
        rng = np.random.default_rng(seed)
        for name in ensembles:
            offset = _ENSEMBLE_SEED_OFFSET[name]
            R, C = build_ensemble_graph(name, N, seed + offset)
            res = evaluate_qft_instance(R, C, rng, m2=m2, theta_mode=theta_mode)
            stats[name].append(res)

    arr = lambda ens, k: np.array([x[k] for x in stats[ens]], dtype=float)

    if verbose:
        print(
            f"=== P-QFT-1 Block A+D: Spectrum, Propagators & Schur Boundary Shift "
            f"(N={N}, m^2={m2}, theta={theta_mode}, seeds={n_seeds}) ==="
        )
        hdr = (
            f"{'Ensemble':13s} | {'gap':>7s} | {'(1/N)ln det':>11s} | "
            f"{'G_time(3)':>9s} | {'G_space(3)':>10s} | {'PJ_time(3)':>10s} | "
            f"{'PJ_spc_max':>10s} | {'M_eff':>7s} | {'d_gamma':>8s}"
        )
        print("-" * len(hdr))
        print(hdr)
        print("-" * len(hdr))
        for name in ensembles:
            print(
                f"{name:13s} | "
                f"{np.nanmean(arr(name, 'gap')):7.4f} | "
                f"{np.nanmean(arr(name, 'logdet_Pi_per_N')):11.4f} | "
                f"{np.nanmean(arr(name, 'G_time_3')):9.4f} | "
                f"{np.nanmean(arr(name, 'G_space_3')):10.4f} | "
                f"{np.nanmean(arr(name, 'PJ_time_3')):10.4f} | "
                f"{np.nanmax(arr(name, 'PJ_space_max')):10.2e} | "
                f"{np.nanmean(arr(name, 'M_eff')):7.3f} | "
                f"{np.nanmean(arr(name, 'd_gamma')):+8.4f}"
            )
        print("-" * len(hdr))
        print()
    return stats


def run_propagator_decay(
    N=64,
    n_seeds=8,
    m2=0.5,
    theta_mode="flat",
    seed_base=4000,
    r_max=6,
    verbose=True,
):
    """
    Блок B: детальное сравнение затухания евклидова пропагатора Sigma = Pi^{-1}
    и причинного коммутатора Паули-Йоста Delta_PJ по расстоянию r.
    """
    targets = ["Hypercube_2D", "Minkowski_2D", "KR_T3", "KR_T2"]
    if verbose:
        print(
            f"=== P-QFT-1 Block B: Euclidean Sigma vs Causal Pauli-Jordan Delta_PJ "
            f"(N={N}, m^2={m2}, theta={theta_mode}) ==="
        )

    for name in targets:
        acc_sig = {k: {r: [] for r in range(1, r_max + 1)} for k in ("all", "timelike", "spacelike")}
        acc_pj = {k: {r: [] for r in range(1, r_max + 1)} for k in ("all", "timelike", "spacelike")}
        offset = _ENSEMBLE_SEED_OFFSET[name]
        for s in range(n_seeds):
            seed = seed_base + s
            rng = np.random.default_rng(seed)
            R, C = build_ensemble_graph(name, N, seed + offset)
            res = evaluate_qft_instance(R, C, rng, m2=m2, theta_mode=theta_mode, r_max=r_max)
            for k in acc_sig:
                for r, val in res["profiles_sigma"][k].items():
                    if np.isfinite(val):
                        acc_sig[k][r].append(val)
                for r, val in res["profiles_pj"][k].items():
                    if np.isfinite(val):
                        acc_pj[k][r].append(val)
        if verbose:
            print(f"  {name}:")
            print(
                f"    {'r':>3s} | {'Sigma_all':>10s} | {'Sigma_time':>11s} | {'Sigma_space':>11s} || "
                f"{'PJ_time':>11s} | {'PJ_space':>11s}"
            )
            for r in range(1, r_max + 1):
                sa = np.mean(acc_sig["all"][r]) if acc_sig["all"][r] else np.nan
                st = np.mean(acc_sig["timelike"][r]) if acc_sig["timelike"][r] else np.nan
                ss = np.mean(acc_sig["spacelike"][r]) if acc_sig["spacelike"][r] else np.nan
                pt = np.mean(acc_pj["timelike"][r]) if acc_pj["timelike"][r] else np.nan
                ps = np.mean(acc_pj["spacelike"][r]) if acc_pj["spacelike"][r] else np.nan
                print(
                    f"    {r:3d} | {sa:10.5f} | {st:11.5f} | {ss:11.5f} || "
                    f"{pt:11.5f} | {ps:11.5f}"
                )
            print()
    return None


def run_block_C_trajectory(
    N=64,
    n_seeds=8,
    m2_grid=(0.05, 0.2, 0.5, 1.0, 2.0, 5.0),
    theta_mode="flat",
    seed_base=3000,
    verbose=True,
):
    """
    Блок C: траектория по m^2 для (1/N)ln det Pi, M_eff, d_gamma, Sigma(3) и PJ_time(3).
    """
    targets = ["Hypercube_2D", "Minkowski_2D", "KR_T3"]
    graphs = {}
    for name in targets:
        offset = _ENSEMBLE_SEED_OFFSET[name]
        graphs[name] = [
            build_ensemble_graph(name, N, seed_base + 100 * i + offset)
            for i in range(n_seeds)
        ]

    if verbose:
        print(f"=== P-QFT-1 Block C: m^2 Trajectory (N={N}, theta={theta_mode}, seeds={n_seeds}) ===")

    summary = {t: [] for t in targets}
    for m2 in m2_grid:
        if verbose:
            print(f"  m^2 = {m2:.2f}")
        for name in targets:
            vals = []
            for i, (R, C) in enumerate(graphs[name]):
                rng = np.random.default_rng(seed_base + 7 * i)
                vals.append(evaluate_qft_instance(R, C, rng, m2=m2, theta_mode=theta_mode))
            row = {
                "lambda_min": float(np.mean([v["lambda_min"] for v in vals])),
                "logdet_Pi_per_N": float(np.mean([v["logdet_Pi_per_N"] for v in vals])),
                "M_eff": float(np.nanmean([v["M_eff"] for v in vals])),
                "d_gamma": float(np.nanmean([v["d_gamma"] for v in vals])),
                "G_all_3": float(np.nanmean([v["G_all_3"] for v in vals])),
                "PJ_time_3": float(np.nanmean([v["PJ_time_3"] for v in vals])),
            }
            summary[name].append({"m2": m2, **row})
            if verbose:
                print(
                    f"    {name:14s}: (1/N)ln det={row['logdet_Pi_per_N']:.4f}, "
                    f"M_eff={row['M_eff']:.3f}, d_gamma={row['d_gamma']:+.4f}, "
                    f"Sigma(3)={row['G_all_3']:.4f}, PJ_time(3)={row['PJ_time_3']:.4f}"
                )
    if verbose:
        print()
    return summary


# =====================================================================
# 5. ТОЧКА ВХОДА CLI
# =====================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CPP v4.4 Protocol P-QFT-1 (v1.1): Spectrum, Euclidean vs Pauli-Jordan Propagator & Schur Shift"
    )
    parser.add_argument("--N", type=int, default=64)
    parser.add_argument("--seeds", type=int, default=10)
    parser.add_argument("--m2", type=float, default=0.5)
    parser.add_argument(
        "--theta",
        choices=["flat", "noise", "random"],
        default="flat",
        help="Phase configuration on Hasse edges (default: flat)",
    )
    parser.add_argument(
        "--blocks",
        default="all",
        help="Comma-separated list: AD,B,C or 'all'",
    )
    parser.add_argument("--log", default=None)
    args = parser.parse_args()

    if args.log is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.log = f"cpp_v44_qft_spectrum_{stamp}.txt"

    log_path = os.path.abspath(args.log)
    log_file = open(log_path, "w", encoding="utf-8")
    old_stdout = sys.stdout
    sys.stdout = cpp._Tee(old_stdout, log_file)

    blocks = [b.strip().upper() for b in args.blocks.split(",")]
    if "ALL" in blocks:
        blocks = ["AD", "B", "C"]

    try:
        print(f"CPP v4.4 P-QFT-1 (v1.1) log: {log_path}")
        print(f"Started: {datetime.now().isoformat(timespec='seconds')}")
        print(f"Parameters: N={args.N}, seeds={args.seeds}, m2={args.m2}, theta={args.theta}")
        print("=" * 112)
        if "AD" in blocks:
            run_block_AD(
                N=args.N, n_seeds=args.seeds, m2=args.m2,
                theta_mode=args.theta, verbose=True,
            )
        if "B" in blocks:
            run_propagator_decay(
                N=args.N, n_seeds=max(6, args.seeds // 2), m2=args.m2,
                theta_mode=args.theta, verbose=True,
            )
        if "C" in blocks:
            run_block_C_trajectory(
                N=args.N, n_seeds=max(6, args.seeds // 2),
                theta_mode=args.theta, verbose=True,
            )
        print("=" * 112)
        print(f"Finished: {datetime.now().isoformat(timespec='seconds')}")
        print(f"Results saved to: {log_path}")
    finally:
        sys.stdout = old_stdout
        log_file.close()
        print(f"\nResults also saved to: {log_path}")