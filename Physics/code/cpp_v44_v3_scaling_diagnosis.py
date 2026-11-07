# cpp_v44_v3_scaling_diagnosis.py
# Диагностика масштабного поведения Протокола V3 при L in {5, 6, 7, 8, 9} (CPP v4.4):
#  1. Сравнение базового сэмплера M1 (глобальный выбор пар + фикс. n_steps)
#     с локально-оконным сэмплером M1 при постоянном числе шагов на внешнее ребро.
#  2. Разделение внешней зоны E_A на приграничный слой (near, 1 шаг от dA)
#     и глубокий слой (far), где рёбра удерживаются кратностью d_diamond = 2.
#  3. Разложение полного сдвига Delta f_null на эффект упорядочивания оболочки
#     Delta f_shell = f(eta, 0) - f(0, pi) и чистый эффект фрустрированного ядра
#     Delta f_core  = f(eta, pi) - f(eta, 0) (Раздел 9, таблица V3 в CPP v4.4).

import argparse
from datetime import datetime
import os
import sys

import numpy as np

import cpp_v44_reference as cpp


def classify_external_zones(R_init, b_idx, E_idx):
    """
    Разбивает вершины E_idx на:
      - E_near_set: вершины E_A, смежные с интерфейсом dA в исходном скелете R_init + R_init^T
      - E_far_set : остальные вершины E_A (на расстоянии >= 2 шагов от dA)
    """
    A_sym = (R_init + R_init.T) > 0
    b_mask = np.zeros(len(R_init), dtype=bool)
    b_mask[b_idx] = True
    near_nodes = set()
    for u in E_idx:
        if np.any(A_sym[u] & b_mask):
            near_nodes.add(int(u))
    far_nodes = set(int(u) for u in E_idx) - near_nodes
    return near_nodes, far_nodes


def external_f_null_stratified(R, E_idx, near_nodes):
    """
    Вычисляет f_null(E_A) глобально, в приграничном слое вокруг dA (near, хотя бы один
    конец ребра в near_nodes) и во внешнем слое (far, оба конца вне near_nodes).
    """
    d_diam, _, _ = cpp.diamond_participation(R)
    N = len(R)
    E_mask = np.zeros(N, dtype=bool)
    E_mask[E_idx] = True
    near_mask = np.zeros(N, dtype=bool)
    for u in near_nodes:
        near_mask[u] = True

    ext_edges = (R == 1) & np.outer(E_mask, E_mask)
    near_touch = np.outer(near_mask, E_mask) | np.outer(E_mask, near_mask)
    near_edges = ext_edges & near_touch
    far_edges = ext_edges & (~near_touch)

    def _frac(mask):
        cnt = int(np.sum(mask))
        if cnt == 0:
            return np.nan
        return float(np.sum(mask & (d_diam == 0)) / cnt)

    return _frac(ext_edges), _frac(near_edges), _frac(far_edges)


def run_v3_chain_scaled(
    R_init,
    idx_map,
    core_set,
    I_idx,
    b_idx,
    E_idx,
    near_nodes,
    L,
    nu=0.5,
    kmax=8,
    T=0.5,
    m2=0.5,
    eta_val=50.0,
    phi_core=np.pi,
    n_steps=1200,
    burn_in=150,
    audit_every=200,
    local_proposer=True,
    seed=100,
):
    """
    Одиночная цепь Метрополиса-Гастингса с логированием числа предложенных и принятых
    шагов M1 на одно внешнее ребро и стратифицированных долей f_null.
    """
    rng = np.random.default_rng(seed)
    R = R_init.copy()
    Theta = rng.uniform(0.0, 2.0 * np.pi, size=R.shape) * R

    # Установка потока phi_core на центральную плакетку ядра
    c0 = (L // 2 - 1, L // 2 - 1)
    c1 = (L // 2, L // 2 - 1)
    c2 = (L // 2, L // 2)
    c3 = (L // 2 - 1, L // 2)
    Theta[idx_map[c0], idx_map[c1]] = phi_core
    Theta[idx_map[c1], idx_map[c2]] = 0.0
    Theta[idx_map[c0], idx_map[c3]] = 0.0
    Theta[idx_map[c3], idx_map[c2]] = 0.0

    # Предварительный список всех локально допустимых пар (u, v) в E_A x E_A с 0 < v - u <= L + 2
    local_pairs = [
        (int(u), int(v))
        for u in E_idx
        for v in E_idx
        if 0 < (v - u) <= (L + 2)
    ]

    F_struct, F_joint, logdet_curr = cpp.structural_and_joint_cost(
        R, Theta, eta_field=eta_val, m2=m2, T=T
    )
    max_woodbury_drift = 0.0
    f_all_list, f_near_list, f_far_list, wc_list = [], [], [], []
    m1_valid_proposals = 0
    m1_accepted = 0

    for step in range(1, n_steps + 1):
        if rng.random() < 0.5:
            # Шаг фазового обновления вне ядра
            ext_edges = [
                (u, v) for u, v in np.argwhere(R == 1) if not (u in core_set and v in core_set)
            ]
            if ext_edges:
                e_mod = ext_edges[rng.integers(len(ext_edges))]
                Th_prop = Theta.copy()
                Th_prop[e_mod] = (Th_prop[e_mod] + rng.normal(0.0, 0.35)) % (2.0 * np.pi)
                _, F_prop, ld_prop = cpp.structural_and_joint_cost(
                    R, Th_prop, eta_field=eta_val, m2=m2, T=T
                )
                if np.log(rng.random()) < -(F_prop - F_joint) / T:
                    Theta = Th_prop
                    F_joint = F_prop
                    logdet_curr = ld_prop
        else:
            # Шаг M1: переброска внешнего ребра
            ext_edges = [(int(u), int(v)) for u, v in np.argwhere(R == 1) if u in E_idx and v in E_idx]
            if ext_edges:
                e_del = ext_edges[rng.integers(len(ext_edges))]
                cand_ok = False
                if local_proposer:
                    non_edges_local = [(u, v) for (u, v) in local_pairs if R[u, v] == 0]
                    if non_edges_local:
                        u_cand, v_cand = non_edges_local[rng.integers(len(non_edges_local))]
                        cand_ok = True
                else:
                    u_cand, v_cand = sorted(rng.choice(E_idx, size=2, replace=False))
                    if R[u_cand, v_cand] == 0 and abs(u_cand - v_cand) <= L + 2:
                        cand_ok = True

                if cand_ok:
                    m1_valid_proposals += 1
                    R_prop = R.copy()
                    R_prop[e_del] = 0
                    R_prop[u_cand, v_cand] = 1
                    if cpp.admissible(R_prop, nu=nu, kmax=kmax):
                        th_add = float(rng.uniform(0.0, 2.0 * np.pi))
                        Th_prop = Theta.copy()
                        Th_prop[e_del] = 0.0
                        Th_prop[u_cand, v_cand] = th_add
                        if eta_val > 0.0:
                            Pi_curr = cpp.magnetic_precision(R, Theta, m2=m2)
                            ratio_w, _, _, _ = cpp.woodbury_edge_swap_ratio(
                                Pi_curr, e_del, float(Theta[e_del]), (u_cand, v_cand), th_add
                            )
                            ld_prop = logdet_curr + float(np.log(max(1e-30, ratio_w)))
                            F_s_prop, _, _ = cpp.structural_and_joint_cost(
                                R_prop, Th_prop, eta_field=0.0, m2=m2, T=T
                            )
                            F_prop = F_s_prop + eta_val * ld_prop
                        else:
                            F_s_prop, F_prop, ld_prop = cpp.structural_and_joint_cost(
                                R_prop, Th_prop, eta_field=0.0, m2=m2, T=T
                            )
                        if np.log(rng.random()) < -(F_prop - F_joint) / T:
                            R = R_prop
                            Theta = Th_prop
                            F_joint = F_prop
                            logdet_curr = ld_prop
                            m1_accepted += 1

        if eta_val > 0.0 and step % audit_every == 0:
            ld_exact = float(np.linalg.slogdet(cpp.magnetic_precision(R, Theta, m2=m2))[1])
            max_woodbury_drift = max(max_woodbury_drift, abs(logdet_curr - ld_exact))
            logdet_curr = ld_exact

        if step > burn_in and step % 10 == 0:
            fa, fn, ff = external_f_null_stratified(R, E_idx, near_nodes)
            f_all_list.append(fa)
            f_near_list.append(fn)
            f_far_list.append(ff)
            cw = cpp.cross_wilson_action_identity(R, Theta, I_idx, b_idx, E_idx, m2=m2)
            wc_list.append(cw["W_cross"])

    return {
        "f_all": float(np.nanmean(f_all_list)),
        "f_near": float(np.nanmean(f_near_list)),
        "f_far": float(np.nanmean(f_far_list)) if not np.all(np.isnan(f_far_list)) else np.nan,
        "W_cross": float(np.mean(wc_list)),
        "m1_valid": m1_valid_proposals,
        "m1_acc": m1_accepted,
        "drift": float(max_woodbury_drift),
    }


def evaluate_L_point(
    L,
    eta_field=50.0,
    n_seeds=60,
    steps_per_ext_edge=60,
    fixed_steps=1200,
    local_proposer=True,
    scale_steps=True,
    seed_base=100,
):
    """
    Запускает тройку ансамблей (1: eta, phi=pi; 2: eta, phi=0; 3: eta=0, phi=pi)
    для заданного размера решётки L и возвращает полную статистику.
    """
    R_init, coords = cpp.directed_hypercube((L, L))
    idx_map = {c: i for i, c in enumerate(coords)}
    lo, hi = L // 2 - 2, L // 2 + 1
    A_core = [i for i, c in enumerate(coords) if lo <= c[0] <= hi and lo <= c[1] <= hi]
    I_idx, b_idx, E_idx, _ = cpp.partition_triad(R_init, A_core)
    core_set = set(A_core)
    near_nodes, _ = classify_external_zones(R_init, b_idx, E_idx)

    E_mask = np.zeros(len(R_init), dtype=bool)
    E_mask[E_idx] = True
    n_ext_edges = int(np.sum((R_init == 1) & np.outer(E_mask, E_mask)))

    if scale_steps:
        n_steps = max(fixed_steps, int(steps_per_ext_edge * n_ext_edges))
        burn_in = max(150, n_steps // 6)
    else:
        n_steps = fixed_steps
        burn_in = 150

    df_tot, df_near, df_far = [], [], []
    df_shell, df_core = [], []
    wc_list = []
    m1_prop_per_edge, m1_acc_per_edge = [], []
    max_drift = 0.0

    for s in range(n_seeds):
        # 1. Coupled frustrated core (eta_field, phi_core = pi)
        r_pi = run_v3_chain_scaled(
            R_init, idx_map, core_set, I_idx, b_idx, E_idx, near_nodes, L,
            eta_val=eta_field, phi_core=np.pi, n_steps=n_steps, burn_in=burn_in,
            local_proposer=local_proposer, seed=seed_base + s,
        )
        # 2. Coupled flat core (eta_field, phi_core = 0)
        r_flat = run_v3_chain_scaled(
            R_init, idx_map, core_set, I_idx, b_idx, E_idx, near_nodes, L,
            eta_val=eta_field, phi_core=0.0, n_steps=n_steps, burn_in=burn_in,
            local_proposer=local_proposer, seed=seed_base + 500 + s,
        )
        # 3. Uncoupled control (eta_field = 0, phi_core = pi)
        r_0 = run_v3_chain_scaled(
            R_init, idx_map, core_set, I_idx, b_idx, E_idx, near_nodes, L,
            eta_val=0.0, phi_core=np.pi, n_steps=n_steps, burn_in=burn_in,
            local_proposer=local_proposer, seed=seed_base + 1000 + s,
        )

        df_tot.append(r_pi["f_all"] - r_0["f_all"])
        df_near.append(r_pi["f_near"] - r_0["f_near"])
        if np.isfinite(r_pi["f_far"]) and np.isfinite(r_0["f_far"]):
            df_far.append(r_pi["f_far"] - r_0["f_far"])
        df_shell.append(r_flat["f_all"] - r_0["f_all"])
        df_core.append(r_pi["f_all"] - r_flat["f_all"])
        wc_list.append(r_pi["W_cross"])
        m1_prop_per_edge.append(r_pi["m1_valid"] / max(1, n_ext_edges))
        m1_acc_per_edge.append(r_pi["m1_acc"] / max(1, n_ext_edges))
        max_drift = max(max_drift, r_pi["drift"], r_flat["drift"])

    def _stat(arr):
        a = np.asarray(arr, dtype=float)
        a = a[np.isfinite(a)]
        if len(a) == 0:
            return np.nan, np.nan, np.nan
        m = float(np.mean(a))
        se = float(np.std(a, ddof=1) / np.sqrt(len(a))) if len(a) > 1 else 0.0
        z = m / max(1e-12, se)
        return m, se, z

    m_tot, se_tot, z_tot = _stat(df_tot)
    m_near, se_near, z_near = _stat(df_near)
    m_far, se_far, z_far = _stat(df_far)
    m_sh, se_sh, z_sh = _stat(df_shell)
    m_co, se_co, z_co = _stat(df_core)
    m_wc, se_wc, _ = _stat(wc_list)

    return {
        "L": L,
        "ndA": len(b_idx),
        "n_ext_edges": n_ext_edges,
        "n_steps": n_steps,
        "m1_prop_per_edge": float(np.mean(m1_prop_per_edge)),
        "m1_acc_per_edge": float(np.mean(m1_acc_per_edge)),
        "df_tot": (m_tot, se_tot, z_tot),
        "df_near": (m_near, se_near, z_near),
        "df_far": (m_far, se_far, z_far),
        "df_shell": (m_sh, se_sh, z_sh),
        "df_core": (m_co, se_co, z_co),
        "W_cross": (m_wc, se_wc),
        "max_drift": max_drift,
    }


def run_scaling_diagnosis(
    L_list=(5, 6, 7, 8, 9),
    eta_field=50.0,
    n_seeds=60,
    steps_per_ext_edge=60,
    verbose=True,
):
    if verbose:
        print(
            f"=== БЛОК 1: Базовый сэмплер (глобальный выбор пар, фикс. n_steps=1200, "
            f"eta={eta_field}, seeds={n_seeds}) ==="
        )
        hdr1 = (
            f"{'L':>2s} | {'|dA|':>4s} | {'|E_edg|':>7s} | {'M1_prop/e':>9s} | {'M1_acc/e':>8s} | "
            f"{'Delta f_tot (z)':>22s} | {'Delta f_near (z)':>22s} | {'W_cross':>14s}"
        )
        print("-" * len(hdr1))
        print(hdr1)
        print("-" * len(hdr1))
    for L in L_list:
        res = evaluate_L_point(
            L, eta_field=eta_field, n_seeds=n_seeds,
            local_proposer=False, scale_steps=False,
        )
        mt, st, zt = res["df_tot"]
        mn, sn, zn = res["df_near"]
        mw, sw = res["W_cross"]
        if verbose:
            print(
                f"{L:2d} | {res['ndA']:4d} | {res['n_ext_edges']:7d} | "
                f"{res['m1_prop_per_edge']:9.2f} | {res['m1_acc_per_edge']:8.2f} | "
                f"{mt:+.4f}±{st:.4f} ({zt:+5.2f}s) | "
                f"{mn:+.4f}±{sn:.4f} ({zn:+5.2f}s) | "
                f"{mw:+.4f}±{sw:.4f}"
            )
    if verbose:
        print("-" * len(hdr1))
        print()

        print(
            f"=== БЛОК 2: Локально-оконный сэмплер + нормировка шагов "
            f"({steps_per_ext_edge} шагов/ребро, eta={eta_field}, seeds={n_seeds}) ==="
        )
        hdr2 = (
            f"{'L':>2s} | {'steps':>5s} | {'M1_prop/e':>9s} | {'M1_acc/e':>8s} | "
            f"{'Delta f_tot (z)':>22s} | {'Delta f_near (z)':>22s} | "
            f"{'Delta f_shell (z)':>22s} | {'Delta f_core (z)':>21s}"
        )
        print("-" * len(hdr2))
        print(hdr2)
        print("-" * len(hdr2))
    for L in L_list:
        res = evaluate_L_point(
            L, eta_field=eta_field, n_seeds=n_seeds,
            steps_per_ext_edge=steps_per_ext_edge,
            local_proposer=True, scale_steps=True,
        )
        mt, st, zt = res["df_tot"]
        mn, sn, zn = res["df_near"]
        ms, ss, zs = res["df_shell"]
        mc, sc, zc = res["df_core"]
        if verbose:
            print(
                f"{L:2d} | {res['n_steps']:5d} | "
                f"{res['m1_prop_per_edge']:9.2f} | {res['m1_acc_per_edge']:8.2f} | "
                f"{mt:+.4f}±{st:.4f} ({zt:+5.2f}s) | "
                f"{mn:+.4f}±{sn:.4f} ({zn:+5.2f}s) | "
                f"{ms:+.4f}±{ss:.4f} ({zs:+5.2f}s) | "
                f"{mc:+.4f}±{sc:.4f} ({zc:+5.2f}s)"
            )
    if verbose:
        print("-" * len(hdr2))
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CPP v4.4 V3 L-Scaling & Proposer Starvation Diagnosis")
    parser.add_argument("--L", type=int, nargs="+", default=[5, 6, 7, 8, 9], help="Список размеров L")
    parser.add_argument("--eta", type=float, default=50.0, help="Параметр eta_field (по умолчанию: 50.0)")
    parser.add_argument("--seeds", type=int, default=60, help="Число сидов на точку L (по умолчанию: 60)")
    parser.add_argument(
        "--steps-per-edge",
        type=int,
        default=60,
        help="Число шагов Метрополиса на одно внешнее ребро в Блоке 2 (по умолчанию: 60)",
    )
    parser.add_argument("--log", default=None)
    args = parser.parse_args()

    if args.log is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.log = f"cpp_v44_v3_scaling_{stamp}.txt"

    log_path = os.path.abspath(args.log)
    log_file = open(log_path, "w", encoding="utf-8")
    old_stdout = sys.stdout
    sys.stdout = cpp._Tee(old_stdout, log_file)

    try:
        print(f"CPP v4.4 V3 Scaling Diagnosis log: {log_path}")
        print(f"Started: {datetime.now().isoformat(timespec='seconds')}")
        print("=" * 136)
        run_scaling_diagnosis(
            L_list=args.L,
            eta_field=args.eta,
            n_seeds=args.seeds,
            steps_per_ext_edge=args.steps_per_edge,
            verbose=True,
        )
        print("=" * 136)
        print(f"Finished: {datetime.now().isoformat(timespec='seconds')}")
        print(f"Results saved to: {log_path}")
    finally:
        sys.stdout = old_stdout
        log_file.close()
        print(f"\nResults also saved to: {log_path}")