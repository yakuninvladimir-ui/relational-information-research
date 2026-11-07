# cpp_v44_minkowski_bd_test.py
# Протокол сравнения (v1.1): функционалы CPP v4.4 (F_struct, чистое поле (1/N)ln det Pi,
# диамагнитная энергия Phi_mag, граничная масса Шура M_eff = Tr K_int и сдвиг щели d_gamma)
# против действия Бенинказы-Доукера (S_BD^(2d), S_BD^(4d)) и оценок размерности (d_MM, d_mid)
# на пуассоновских посевах в пространство Минковского M^{1,d-1}, гиперкубах H_d и
# не-многообразных порядках (KR_3layer_T3, KR_2layer_T2, Random_DAG_35).
#
# Зависимости: cpp_v44_reference.py (в той же директории или в PYTHONPATH).

import argparse
from datetime import datetime
import os
import sys

import numpy as np
from scipy.linalg import eigvals
from scipy.optimize import brentq
from scipy.special import gamma

import cpp_v44_reference as cpp


# =====================================================================
# 1. ПОСТРОЕНИЕ ЧАСТИЧНЫХ ПОРЯДКОВ И РЕДУКЦИЯ ХАССЕ
# =====================================================================

def transitive_reduction_from_poset(C):
    """
    Построение транзитивно неприводимой матрицы Хассе R из булевой матрицы
    строгого частичного порядка C (C_xy = 1 <=> x < y).
    """
    C = (np.asarray(C) > 0).astype(np.int64)
    two_or_more = (C @ C) > 0
    R = (C > 0) & (~two_or_more)
    return R.astype(np.int64)


def causal_closure_from_hasse(R):
    """Восстановление полного частичного порядка C (x < y) из матрицы Хассе R."""
    R = np.asarray(R, dtype=float)
    N = len(R)
    C = (np.linalg.inv(np.eye(N) - R) - np.eye(N)) > 0.5
    return C.astype(np.int64)


def minkowski_sprinkling_hasse(N, d=2, seed=0):
    """
    Пуассоновский посев N точек в причинный ромб Александрова I(p, q)
    в d-мерном пространстве Минковского M^{1, d-1}:
      p = (0, 0, ..., 0), q = (1, 0, ..., 0),
      точка x = (t, r_vec) принадлежит I(p, q) <=> 0 <= t <= 1 и ||r_vec|| <= min(t, 1 - t).
    Возвращает транзитивно неприводимую матрицу Хассе R и матрицу порядка C.
    """
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
    """
    Генератор двухслойных (T_2) и трёхслойных (T_3) частичных порядков
    Клейтмана-Ротшильда с точной транзитивной редукцией Хассе.
    """
    rng = np.random.default_rng(seed)
    R0 = np.zeros((N, N), dtype=np.int64)
    if layers == 2:
        n1 = N // 2
        R0[:n1, n1:] = (rng.random((n1, N - n1)) < p_edge).astype(np.int64)
        return R0, R0.copy()
    elif layers == 3:
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
    else:
        raise ValueError("Параметр layers должен быть равен 2 или 3.")


# =====================================================================
# 2. ДЕЙСТВИЕ БЕНИНКАЗЫ-ДОУКЕРА, РАЗМЕРНОСТИ И ГРАНИЧНЫЙ СДВИГ ШУРА
# =====================================================================

def benincasa_dowker_action(C, d=2, eps_smear=None):
    """
    Вычисление дискретного действия Бенинказы-Доукера S_BD^{(2d)} и S_BD^{(4d)}
    (а также его нелокально сглаженной версии при eps_smear in (0, 1))
    по матрице строгого частичного порядка C (C_xy = 1 <=> x < y).
    """
    C = (np.asarray(C) > 0).astype(np.int64)
    N = len(C)
    interval_sizes = (C @ C)[C == 1]
    N1 = int(np.sum(interval_sizes == 0))
    N2 = int(np.sum(interval_sizes == 1))
    N3 = int(np.sum(interval_sizes == 2))
    N4 = int(np.sum(interval_sizes == 3))

    if eps_smear is None:
        if d == 2:
            S_bd = float(N - 2 * N1 + 4 * N2 - 2 * N3)
        elif d == 4:
            S_bd = float(N - N1 + 9 * N2 - 16 * N3 + 8 * N4)
        else:
            raise ValueError("Действие Бенинказы-Доукера реализовано для d=2 и d=4.")
    else:
        xi = float(eps_smear)
        n = interval_sizes.astype(float)
        if d == 2:
            f_n = (1.0 - xi) ** n * (
                1.0
                - (2.0 * xi * n) / (1.0 - xi)
                + (xi ** 2 * n * (n - 1.0)) / (2.0 * (1.0 - xi) ** 2)
            )
            S_bd = float(2.0 * xi * N - 4.0 * (xi ** 2) * np.sum(f_n))
        elif d == 4:
            f_n = (1.0 - xi) ** n * (
                1.0
                - (9.0 * xi * n) / (1.0 - xi)
                + (8.0 * (xi ** 2) * n * (n - 1.0)) / ((1.0 - xi) ** 2)
                - (4.0 * (xi ** 3) * n * (n - 1.0) * (n - 2.0)) / (3.0 * (1.0 - xi) ** 3)
            )
            c4 = (4.0 / np.sqrt(6.0)) ** 0.5
            S_bd = float(c4 * (np.sqrt(xi) * N - (xi ** 1.5) * np.sum(f_n)))
        else:
            raise ValueError("Сглаженное действие Бенинказы-Доукера реализовано для d=2 и d=4.")

    return S_bd, {"N1": N1, "N2": N2, "N3": N3, "N4": N4}


def myrheim_meyer_dimension(C):
    """
    Оценка размерности Мирхейма-Мейера d_tau по доле сравнимых пар r = |C| / binom(N, 2)
    с явным флагом валидности (Раздел 9.1 п. 5 спецификации CPP v4.4).
    """
    N = len(C)
    if N < 2:
        return np.nan, 0.0, False
    r = float(np.sum(C > 0)) / (0.5 * N * (N - 1))
    if r <= 1e-5 or r >= 1.0 - 1e-5:
        return np.nan, r, False

    def mm_fraction(d):
        return float(gamma(d + 1.0) * gamma(0.5 * d) / (2.0 * gamma(1.5 * d)))

    if r > mm_fraction(1.05) or r < mm_fraction(10.0):
        return np.nan, r, False
    d_est = brentq(lambda d: mm_fraction(d) - r, 1.05, 10.0)
    return float(d_est), r, True


def midpoint_scaling_dimension(C):
    """
    Оценка размерности масштабирования средней точки (Midpoint Scaling Dimension d_mid)
    по максимальному интервалу I(x, y). Возвращает (d_mid, max_interval_size).
    """
    C = (np.asarray(C) > 0).astype(np.int64)
    I_mat = C @ C
    max_int = int(np.max(I_mat)) if I_mat.size else 0
    if max_int < 4:
        return np.nan, max_int
    x, y = np.unravel_index(np.argmax(I_mat), I_mat.shape)
    n_tot = float(I_mat[x, y]) + 2.0
    zs = np.where((C[x] == 1) & (C[:, y] == 1))[0]
    if len(zs) == 0:
        return np.nan, max_int
    sub_sizes = np.minimum(I_mat[x, zs] + 1.0, I_mat[zs, y] + 1.0)
    n_half = float(np.max(sub_sizes))
    if n_half <= 0.0:
        return np.nan, max_int
    return float(np.log2(n_tot / n_half)), max_int


def schur_triad_metrics(R, Theta, m2=0.5, beta=1.0):
    """
    Вычисляет граничную массу Шура M_eff = Tr(K_int), сдвиг граничной щели
    релаксации d_gamma = gamma_bdry - gamma_bdry0 (Проверка [19] в cpp_v44_reference.py)
    и перекрёстное действие Вильсона W_cross >= 0 на центральной триаде (I_A, dA, E_A).
    Включает резервный выбор замкнутой 1-окрестности вершины B_1(u_0) для двухслойных
    графов KR_2layer_T2, гарантирующий I_A != empty.
    """
    N = len(R)
    side = int(round(np.sqrt(N)))
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
            cw = cpp.cross_wilson_action_identity(R, Theta, I, b, E, m2=m2)
            if hasattr(cpp, "boundary_effective_gap"):
                bg = cpp.boundary_effective_gap(Pi, Q, b, I, E, Gamma_scale=1.0)
                return float(bg["M_eff"]), float(bg["d_gamma"]), float(cw["W_cross"])

            blk = lambda u, v: Pi[np.ix_(u, v)]
            Pi_I, Pi_b, Pi_E = blk(I, I), blk(b, b), blk(E, E)
            K_int = blk(b, I) @ np.linalg.inv(Pi_I) @ blk(I, b)
            K_ext = blk(b, E) @ np.linalg.inv(Pi_E) @ blk(E, b)
            S_dA = Pi_b - K_int - K_ext
            S_0 = Pi_b - K_ext
            meff = float(np.real(np.trace(K_int)))
            Gb = np.eye(len(b))
            Qb = Q[np.ix_(b, b)]
            g_bdry = float(np.min(np.real(eigvals((Gb + Qb) @ S_dA))))
            g_bdry0 = float(np.min(np.real(eigvals((Gb + Qb) @ S_0))))
            return meff, float(g_bdry - g_bdry0), float(cw["W_cross"])
        except Exception:
            continue

    return float("nan"), float("nan"), float("nan")


# =====================================================================
# 3. ВЫЧИСЛЕНИЕ МЕТРИК НА ОДНОМ ЭКЗЕМПЛЯРЕ ПРИЧИННОГО МНОЖЕСТВА
# =====================================================================

def evaluate_poset_instance(
    R,
    C,
    rng,
    a=1.0,
    b=0.5,
    g=0.1,
    p=2.0,
    m2=0.5,
    eta_field=1.0,
    T=0.5,
    alpha_deg=0.1,
):
    """
    Вычисление инвариантов CPP v4.4, спектральных и граничных характеристик Шура,
    действия Бенинказы-Доукера и оценок размерности на одном графе Хассе R и его
    причинном замыкании C при фиксированных параметрах.
    """
    assert cpp.is_hasse_irreducible(R), "Нарушен нуль-тест N-Adm: матрица R не является матрицей Хассе!"

    N = len(R)
    Theta = rng.uniform(0.0, 2.0 * np.pi, size=R.shape) * R
    F_struct, F_joint, logdet_Pi = cpp.structural_and_joint_cost(
        R, Theta, a=a, b=b, g=g, p=p, eta_field=eta_field, m2=m2, T=T
    )
    K, _, J, L_raw, L_norm = cpp.causal_phase_invariants(R, Theta)

    # Диамагнитный вклад поля Phi_mag(R, Theta) = ln det Pi(Theta) - ln det Pi(0) >= 0 (Предложение 6.3)
    Pi_0 = cpp.magnetic_precision(R, np.zeros_like(Theta), m2=m2)
    logdet_Pi0 = float(np.linalg.slogdet(Pi_0)[1])
    Phi_mag = logdet_Pi - logdet_Pi0

    # Спектральная щель лапласиана Pi(0)
    ev0 = np.sort(np.real(np.linalg.eigvalsh(0.5 * (Pi_0 + Pi_0.conj().T))))
    spec_gap = float(ev0[1] - ev0[0]) if N > 1 else 0.0

    # Граничная масса Шура M_eff = Tr(K_int), сдвиг щели d_gamma и W_cross
    M_eff, d_gamma, W_cross = schur_triad_metrics(R, Theta, m2=m2, beta=1.0)

    # Нелинейный регулятор степени вершин sum_x deg(x)^2 (Замечание к Предложению 3.2 в §3.2)
    deg = (R + R.T).sum(axis=1).astype(float)
    deg_sq_penalty = float(alpha_deg * np.sum(deg ** 2))
    F_joint_deg = F_joint + deg_sq_penalty

    # Доля бинарных ромбов K_xy == 2 среди всех активных перетяжек K_xy >= 2
    active_pairs = K[K >= 2]
    f_K2_combinatorial = float(np.sum(active_pairs == 2) / len(active_pairs)) if len(active_pairs) > 0 else 0.0

    # Действие Бенинказы-Доукера (локальное и сглаженное при eps=0.25)
    S_bd2, counts = benincasa_dowker_action(C, d=2, eps_smear=None)
    S_bd4, _ = benincasa_dowker_action(C, d=4, eps_smear=None)
    S_bd2_smear, _ = benincasa_dowker_action(C, d=2, eps_smear=0.25)
    S_bd4_smear, _ = benincasa_dowker_action(C, d=4, eps_smear=0.25)

    # Оценки размерности Мирхейма-Мейера d_tau и средней точки d_mid
    d_mm, r_rel, mm_valid = myrheim_meyer_dimension(C)
    d_mid, max_int_size = midpoint_scaling_dimension(C)

    return {
        "F_struct": F_struct,
        "logdet_Pi": logdet_Pi,
        "logdet_Pi_per_N": logdet_Pi / N,
        "Phi_mag": Phi_mag,
        "spec_gap": spec_gap,
        "M_eff": M_eff,
        "d_gamma": d_gamma,
        "W_cross": W_cross,
        "F_joint": F_joint,
        "F_joint_over_T": F_joint / T,
        "F_joint_deg_over_T": F_joint_deg / T,
        "L_raw": L_raw,
        "L_norm": L_norm,
        "f_K2": f_K2_combinatorial,
        "K_max": int(np.max(K)) if K.size else 0,
        "S_BD2": S_bd2,
        "abs_S_BD2": abs(S_bd2),
        "S_BD4": S_bd4,
        "abs_S_BD4": abs(S_bd4),
        "abs_S_BD2_smear": abs(S_bd2_smear),
        "abs_S_BD4_smear": abs(S_bd4_smear),
        "d_MM": d_mm,
        "d_mid": d_mid,
        "max_interval": max_int_size,
        "mm_gap": abs(d_mm - d_mid) if (mm_valid and np.isfinite(d_mid)) else np.nan,
        "r_rel": r_rel,
        "N1_links": counts["N1"],
    }


def _separation_snr(arr_nonmanifold, arr_manifold):
    """
    Безразмерное отношение сигнал/шум (Z_sep), инвариантное к общему масштабу действия:
      Z_sep = (Mean(non-manifold) - Mean(manifold)) / sqrt(Var(non-manifold) + Var(manifold)).
    """
    a1 = np.asarray(arr_nonmanifold, dtype=float)
    a0 = np.asarray(arr_manifold, dtype=float)
    a1 = a1[np.isfinite(a1)]
    a0 = a0[np.isfinite(a0)]
    if len(a1) == 0 or len(a0) == 0:
        return np.nan
    m1, s1 = float(np.mean(a1)), float(np.var(a1, ddof=1)) if len(a1) > 1 else 0.0
    m0, s0 = float(np.mean(a0)), float(np.var(a0, ddof=1)) if len(a0) > 1 else 0.0
    denom = np.sqrt(max(1e-24, s1 + s0))
    return (m1 - m0) / denom


# =====================================================================
# 4. ОСНОВНОЙ ПРОТОКОЛ СРАВНЕНИЯ АНСАМБЛЕЙ И СКЕЙЛИНГА ПО N
# =====================================================================

def run_bd_vs_cpp_benchmark(N=64, n_seeds=20, seed_base=1000, verbose=True):
    """
    Слепой тест (без подгонки параметров):
    Фиксированы эталонные параметры из cpp_v44_reference.py:
      a=1.0, b=0.5, g=0.1, p=2.0, m2=0.5, eta_field=1.0, T=0.5 (n_bos = 2.0).
    Сравниваются:
      1. Minkowski_2D  — пуассоновский посев в ромб Александрова M^{1,1}
      2. Minkowski_3D  — пуассоновский посев в ромб Александрова M^{1,2}
      3. Minkowski_4D  — пуассоновский посев в ромб Александрова M^{1,3}
      4. Hypercube_2D  — регулярная решётка H_2 (для сверки с эталоном)
      5. KR_3layer_T3  — главный не-многообразный аттрактор Клейтмана-Ротшильда T_3
      6. Random_DAG_35 — перколирующий случайный частичный порядок (p=0.35)
      7. KR_2layer_T2  — вырожденный двухслойный сектор Клейтмана-Ротшильда T_2 (Предложение 3.2)
    """
    A_PAR, B_PAR, G_PAR, P_PAR = 1.0, 0.5, 0.1, 2.0
    M2_PAR, ETA_FIELD, T_PAR = 0.5, 1.0, 0.5
    ALPHA_DEG = 0.1

    ensembles = [
        "Minkowski_2D",
        "Minkowski_3D",
        "Minkowski_4D",
        "Hypercube_2D",
        "KR_3layer_T3",
        "Random_DAG_35",
        "KR_2layer_T2",
    ]
    stats = {name: [] for name in ensembles}

    side = int(round(np.sqrt(N)))
    R_h2, _ = cpp.directed_hypercube((side, side))
    C_h2 = causal_closure_from_hasse(R_h2)

    for s in range(n_seeds):
        seed = seed_base + s
        rng = np.random.default_rng(seed)

        R_m2, C_m2 = minkowski_sprinkling_hasse(N, d=2, seed=seed)
        R_m3, C_m3 = minkowski_sprinkling_hasse(N, d=3, seed=seed + 300)
        R_m4, C_m4 = minkowski_sprinkling_hasse(N, d=4, seed=seed + 600)
        R_t3, C_t3 = kleitman_rothschild_hasse(N, layers=3, seed=seed + 1000)
        R_er = cpp._random_hasse(N, p=0.35, seed=seed + 1500)
        C_er = causal_closure_from_hasse(R_er)
        R_t2, C_t2 = kleitman_rothschild_hasse(N, layers=2, seed=seed + 2000)

        cases = [
            ("Minkowski_2D", R_m2, C_m2),
            ("Minkowski_3D", R_m3, C_m3),
            ("Minkowski_4D", R_m4, C_m4),
            ("Hypercube_2D", R_h2, C_h2),
            ("KR_3layer_T3", R_t3, C_t3),
            ("Random_DAG_35", R_er, C_er),
            ("KR_2layer_T2", R_t2, C_t2),
        ]
        for name, R, C in cases:
            res = evaluate_poset_instance(
                R, C, rng,
                a=A_PAR, b=B_PAR, g=G_PAR, p=P_PAR,
                m2=M2_PAR, eta_field=ETA_FIELD, T=T_PAR, alpha_deg=ALPHA_DEG,
            )
            stats[name].append(res)

    arr = lambda ens, k: np.array([x[k] for x in stats[ens]], dtype=float)

    if verbose:
        print(f"=== CPP v4.4 vs Benincasa-Dowker & Schur Benchmark (N={N}, seeds={n_seeds}) ===")
        print(
            f"Locked parameters: a={A_PAR}, b={B_PAR}, g={G_PAR}, p={P_PAR}, "
            f"m^2={M2_PAR}, eta_field={ETA_FIELD}, T={T_PAR} (n_bos={ETA_FIELD/T_PAR:.1f})"
        )
        h1 = (
            f"{'Ensemble':14s} | {'d_MM':>4s} | {'d_mid':>5s} | {'f_K2':>5s} | "
            f"{'F_struct':>12s} | {'(1/N)lndet':>10s} | {'Phi_mag':>7s} | "
            f"{'M_eff':>6s} | {'d_gam':>7s} | {'|S_BD^(2d)|':>11s} | {'|S_BD^(4d)|':>11s}"
        )
        print("-" * len(h1))
        print(h1)
        print("-" * len(h1))
        for name in ensembles:
            d_mid_val = np.nanmean(arr(name, "d_mid"))
            d_mid_str = f"{d_mid_val:5.2f}" if np.isfinite(d_mid_val) else "  I=0"
            print(
                f"{name:14s} | "
                f"{np.nanmean(arr(name, 'd_MM')):4.2f} | "
                f"{d_mid_str} | "
                f"{np.mean(arr(name, 'f_K2')):5.3f} | "
                f"{np.mean(arr(name, 'F_struct')):7.1f}±{np.std(arr(name, 'F_struct')):4.1f} | "
                f"{np.mean(arr(name, 'logdet_Pi_per_N')):10.4f} | "
                f"{np.mean(arr(name, 'Phi_mag')):7.2f} | "
                f"{np.nanmean(arr(name, 'M_eff')):6.2f} | "
                f"{np.nanmean(arr(name, 'd_gamma')):+7.3f} | "
                f"{np.mean(arr(name, 'abs_S_BD2')):6.1f}±{np.std(arr(name, 'abs_S_BD2')):4.1f} | "
                f"{np.mean(arr(name, 'abs_S_BD4')):6.1f}±{np.std(arr(name, 'abs_S_BD4')):4.1f}"
            )
        print("-" * len(h1))

        # Таблица 2A: Разделимость Z_sep против Minkowski_2D (показывает преимущество чистого поля ln det Pi и M_eff)
        print("\n=== Таблица 2A: Критерий разделимости Z_sep (Non-Manifold vs Minkowski_2D) ===")
        h2 = (
            f"{'Target vs Minkowski_2D':22s} | {'Z_sep(F_joint)':>14s} | "
            f"{'Z_sep((1/N)lndet)':>17s} | {'Z_sep(Phi_mag)':>14s} | "
            f"{'Z_sep(M_eff)':>12s} | {'Z_sep(|S_BD2|)':>14s} | {'Z_sep(S_BD2_sm)':>15s}"
        )
        print("-" * len(h2))
        print(h2)
        print("-" * len(h2))
        for non_man in ["KR_3layer_T3", "Random_DAG_35", "KR_2layer_T2"]:
            z_fj = _separation_snr(arr(non_man, "F_joint_over_T"), arr("Minkowski_2D", "F_joint_over_T"))
            z_ld = _separation_snr(arr(non_man, "logdet_Pi_per_N"), arr("Minkowski_2D", "logdet_Pi_per_N"))
            z_pm = _separation_snr(arr(non_man, "Phi_mag"), arr("Minkowski_2D", "Phi_mag"))
            z_me = _separation_snr(arr(non_man, "M_eff"), arr("Minkowski_2D", "M_eff"))
            z_bd2 = _separation_snr(arr(non_man, "abs_S_BD2"), arr("Minkowski_2D", "abs_S_BD2"))
            z_bds = _separation_snr(arr(non_man, "abs_S_BD2_smear"), arr("Minkowski_2D", "abs_S_BD2_smear"))
            print(
                f"{non_man:22s} | {z_fj:+13.2f}s | "
                f"{z_ld:+16.2f}s | {z_pm:+13.2f}s | "
                f"{z_me:+11.2f}s | {z_bd2:+13.2f}s | {z_bds:+14.2f}s"
            )
        print("-" * len(h2))

        # Таблица 2B: Разделимость Z_sep против Minkowski_4D
        print("\n=== Таблица 2B: Критерий разделимости Z_sep (Non-Manifold vs Minkowski_4D) ===")
        h3 = (
            f"{'Target vs Minkowski_4D':22s} | {'Z_sep(F_joint)':>14s} | "
            f"{'Z_sep((1/N)lndet)':>17s} | {'Z_sep(Phi_mag)':>14s} | "
            f"{'Z_sep(M_eff)':>12s} | {'Z_sep(|S_BD4|)':>14s} | {'Z_sep(S_BD4_sm)':>15s}"
        )
        print("-" * len(h3))
        print(h3)
        print("-" * len(h3))
        for non_man in ["KR_3layer_T3", "Random_DAG_35", "KR_2layer_T2"]:
            z_fj = _separation_snr(arr(non_man, "F_joint_over_T"), arr("Minkowski_4D", "F_joint_over_T"))
            z_ld = _separation_snr(arr(non_man, "logdet_Pi_per_N"), arr("Minkowski_4D", "logdet_Pi_per_N"))
            z_pm = _separation_snr(arr(non_man, "Phi_mag"), arr("Minkowski_4D", "Phi_mag"))
            z_me = _separation_snr(arr(non_man, "M_eff"), arr("Minkowski_4D", "M_eff"))
            z_bd4 = _separation_snr(arr(non_man, "abs_S_BD4"), arr("Minkowski_4D", "abs_S_BD4"))
            z_bd4s = _separation_snr(arr(non_man, "abs_S_BD4_smear"), arr("Minkowski_4D", "abs_S_BD4_smear"))
            print(
                f"{non_man:22s} | {z_fj:+13.2f}s | "
                f"{z_ld:+16.2f}s | {z_pm:+13.2f}s | "
                f"{z_me:+11.2f}s | {z_bd4:+13.2f}s | {z_bd4s:+14.2f}s"
            )
        print("-" * len(h3))
        print()

    return stats


def run_scaling_sweep(N_list=(32, 64, 96), n_seeds=12, seed_base=5000, verbose=True):
    """
    Проверка асимптотического роста разделимости с ростом N при фиксированных параметрах:
    сравниваются Z_sep(F_joint), Z_sep((1/N)ln det Pi), Z_sep(M_eff) и Z_sep(|S_BD^(2d)|)
    для обоих аттракторов Клейтмана-Ротшильда (KR_3layer_T3 и KR_2layer_T2) против Minkowski_2D.
    """
    summary = {}
    if verbose:
        print("=== Масштабирование разделимости с ростом N (KR_T3 и KR_T2 против Minkowski_2D) ===")
        hdr = (
            f"{'N':>4s} | {'Z_Fjoint(T3)':>12s} | {'Z_lndet(T3)':>11s} | {'Z_Meff(T3)':>10s} | "
            f"{'Z_SBD2(T3)':>10s} || {'Z_Fjoint(T2)':>12s} | {'Z_lndet(T2)':>11s} | {'Z_SBD2(T2)':>10s}"
        )
        print("-" * len(hdr))
        print(hdr)
        print("-" * len(hdr))

    for idx, N in enumerate(N_list):
        st = run_bd_vs_cpp_benchmark(N=N, n_seeds=n_seeds, seed_base=seed_base + 500 * idx, verbose=False)
        arr = lambda ens, k: np.array([x[k] for x in st[ens]], dtype=float)

        z_fj_t3 = _separation_snr(arr("KR_3layer_T3", "F_joint_over_T"), arr("Minkowski_2D", "F_joint_over_T"))
        z_ld_t3 = _separation_snr(arr("KR_3layer_T3", "logdet_Pi_per_N"), arr("Minkowski_2D", "logdet_Pi_per_N"))
        z_me_t3 = _separation_snr(arr("KR_3layer_T3", "M_eff"), arr("Minkowski_2D", "M_eff"))
        z_bd_t3 = _separation_snr(arr("KR_3layer_T3", "abs_S_BD2"), arr("Minkowski_2D", "abs_S_BD2"))

        z_fj_t2 = _separation_snr(arr("KR_2layer_T2", "F_joint_over_T"), arr("Minkowski_2D", "F_joint_over_T"))
        z_ld_t2 = _separation_snr(arr("KR_2layer_T2", "logdet_Pi_per_N"), arr("Minkowski_2D", "logdet_Pi_per_N"))
        z_bd_t2 = _separation_snr(arr("KR_2layer_T2", "abs_S_BD2"), arr("Minkowski_2D", "abs_S_BD2"))

        summary[N] = {
            "Z_Fjoint_T3": z_fj_t3,
            "Z_lndet_T3": z_ld_t3,
            "Z_Meff_T3": z_me_t3,
            "Z_SBD2_T3": z_bd_t3,
            "Z_Fjoint_T2": z_fj_t2,
            "Z_lndet_T2": z_ld_t2,
            "Z_SBD2_T2": z_bd_t2,
        }
        if verbose:
            print(
                f"{N:4d} | {z_fj_t3:+11.2f}s | {z_ld_t3:+10.2f}s | {z_me_t3:+9.2f}s | "
                f"{z_bd_t3:+9.2f}s || {z_fj_t2:+11.2f}s | {z_ld_t2:+10.2f}s | {z_bd_t2:+9.2f}s"
            )
    if verbose:
        print("-" * len(hdr))
        print()
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CPP v4.4 (v1.1) vs Benincasa-Dowker, Schur Impedance & Myrheim-Meyer Benchmark"
    )
    parser.add_argument("--N", type=int, default=64, help="Число событий N для детального сравнения (по умолчанию: 64)")
    parser.add_argument("--seeds", type=int, default=20, help="Число независимых сидов (по умолчанию: 20)")
    parser.add_argument(
        "--no-scaling",
        action="store_true",
        help="Пропустить скан масштабирования по N in {32, 64, 96} (по умолчанию скан включён)",
    )
    parser.add_argument(
        "--log",
        default=None,
        help="Путь к лог-файлу результатов (по умолчанию: cpp_v44_minkowski_bd_YYYYMMDD_HHMMSS.txt)",
    )
    args = parser.parse_args()

    if args.log is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.log = f"cpp_v44_minkowski_bd_{stamp}.txt"

    log_path = os.path.abspath(args.log)
    log_file = open(log_path, "w", encoding="utf-8")
    old_stdout = sys.stdout
    sys.stdout = cpp._Tee(old_stdout, log_file)

    try:
        print(f"CPP v4.4 Minkowski vs Benincasa-Dowker (v1.1) log: {log_path}")
        print(f"Started: {datetime.now().isoformat(timespec='seconds')}")
        print("=" * 116)
        run_bd_vs_cpp_benchmark(N=args.N, n_seeds=args.seeds, verbose=True)
        if not args.no_scaling:
            run_scaling_sweep(N_list=(32, 64, 96), n_seeds=max(8, args.seeds // 2), verbose=True)
        print("=" * 116)
        print(f"Finished: {datetime.now().isoformat(timespec='seconds')}")
        print(f"Results saved to: {log_path}")
    finally:
        sys.stdout = old_stdout
        log_file.close()
        print(f"\nResults also saved to: {log_path}")