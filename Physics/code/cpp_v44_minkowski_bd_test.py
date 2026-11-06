# cpp_v44_minkowski_bd_test.py
# Протокол сравнения функционала CPP v4.4 (F_struct + eta_field * ln det Pi)
# с действием Бенинказы-Доукера (S_BD) и оценкой Мирхейма-Мейера (d_tau)
# на пуассоновских посевах в пространство Минковского M^{1,d-1} против
# не-многообразных порядков (T_3, T_2, случайные DAG) и гиперкубов H_d.
# Все параметры (eta_field=1.0, T=0.5, a=1.0, b=0.5, g=0.1, p=2.0, m2=0.5)
# жёстко зафиксированы из cpp_v44_reference.py без подгонки.

import argparse
from datetime import datetime
import os
import sys

import numpy as np
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
    # Для транзитивного порядка C путь длины >= 2 существует <=> (C @ C)_{xy} > 0
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
        t = batch[:, 0] + 0.5  # t in [0, 1]
        r_norm = np.linalg.norm(batch[:, 1:], axis=1) if d > 1 else np.zeros(len(batch))
        mask = r_norm <= np.minimum(t, 1.0 - t)
        for pt in batch[mask]:
            pts.append(np.concatenate([[pt[0] + 0.5], pt[1:]]))
            if len(pts) == N:
                break
    pts = np.array(pts[:N])
    # Топологическая сортировка по времени t гарантирует строгую верхнетреугольность R
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
        # В каноническом ансамбле T_3 все элементы слоя 1 предшествуют слою 3 в C
        C = R0.copy()
        C[idx1, idx3] = 1
        R = transitive_reduction_from_poset(C)
        return R, C
    else:
        raise ValueError("Параметр layers должен быть равен 2 или 3.")


# =====================================================================
# 2. ДЕЙСТВИЕ БЕНИНКАЗЫ-ДОУКЕРА И ОЦЕНКИ РАЗМЕРНОСТИ
# =====================================================================

def benincasa_dowker_action(C, d=2, eps_smear=None):
    """
    Вычисление дискретного действия Бенинказы-Доукера S_BD^{(2d)} и S_BD^{(4d)}
    (а также его нелокально сглаженной версии при eps_smear in (0, 1))
    по матрице строгого частичного порядка C (C_xy = 1 <=> x < y).
    Мощность причинного интервала: |I(x, y)| = (C @ C)_{xy}.
    N_k = число сравнимых пар (x < y) с |I(x, y)| == k - 1.
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
                1.0 - (2.0 * xi * n) / (1.0 - xi) + (xi ** 2 * n * (n - 1.0)) / (2.0 * (1.0 - xi) ** 2)
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
    по максимальному интервалу I(x, y):
      d_mid = log2(|I(x, y)|_max / max_{z in I(x, y)} min(|I(x, z)|, |I(z, y)|)).
    Для гладкого многообразия d_mid близка к d_tau; для слоистых порядков КР расходится.
    """
    C = (np.asarray(C) > 0).astype(np.int64)
    I_mat = C @ C
    if np.max(I_mat) < 4:
        return np.nan
    x, y = np.unravel_index(np.argmax(I_mat), I_mat.shape)
    n_tot = float(I_mat[x, y]) + 2.0
    zs = np.where((C[x] == 1) & (C[:, y] == 1))[0]
    if len(zs) == 0:
        return np.nan
    sub_sizes = np.minimum(I_mat[x, zs] + 1.0, I_mat[zs, y] + 1.0)
    n_half = float(np.max(sub_sizes))
    if n_half <= 0.0:
        return np.nan
    return float(np.log2(n_tot / n_half))


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
    Вычисление инвариантов CPP v4.4, действия Бенинказы-Доукера и оценок размерности
    на одном графе Хассе R и его причинном замыкании C при фиксированных параметрах.
    Включает нуль-тест неприводимости Хассе (Раздел 9.1 п. 3).
    """
    assert cpp.is_hasse_irreducible(R), "Нарушен нуль-тест N-Adm: матрица R не является матрицей Хассе!"

    Theta = rng.uniform(0.0, 2.0 * np.pi, size=R.shape) * R
    F_struct, F_joint, logdet_Pi = cpp.structural_and_joint_cost(
        R, Theta, a=a, b=b, g=g, p=p, eta_field=eta_field, m2=m2, T=T
    )
    K, _, J, L_raw, L_norm = cpp.causal_phase_invariants(R, Theta)

    # Диамагнитный вклад поля Phi_mag(R, Theta) = ln det Pi(Theta) - ln det Pi(0) >= 0 (Предложение 6.3)
    Pi_0 = cpp.magnetic_precision(R, np.zeros_like(Theta), m2=m2)
    logdet_Pi0 = float(np.linalg.slogdet(Pi_0)[1])
    Phi_mag = logdet_Pi - logdet_Pi0

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

    # Оценки размерности Мирхейма-Мейера d_tau и средней точки d_mid
    d_mm, r_rel, mm_valid = myrheim_meyer_dimension(C)
    d_mid = midpoint_scaling_dimension(C)

    return {
        "F_struct": F_struct,
        "logdet_Pi": logdet_Pi,
        "Phi_mag": Phi_mag,
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
        "d_MM": d_mm,
        "d_mid": d_mid,
        "mm_gap": abs(d_mm - d_mid) if (mm_valid and np.isfinite(d_mid)) else np.nan,
        "r_rel": r_rel,
        "N1_links": counts["N1"],
    }


def _separation_snr(arr_nonmanifold, arr_manifold):
    """
    Безразмерное отношение сигнал/шум (Z_sep), инвариантное к общему масштабу действия:
      Z_sep = (Mean(non-manifold) - Mean(manifold)) / sqrt(Var(non-manifold) + Var(manifold)).
    """
    m1, s1 = float(np.mean(arr_nonmanifold)), float(np.var(arr_nonmanifold, ddof=1))
    m0, s0 = float(np.mean(arr_manifold)), float(np.var(arr_manifold, ddof=1))
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
    # Жёстко замороженные параметры CPP v4.4
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

    # Подготовка регулярной решётки H_2 размера ~ N
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
        print(f"=== CPP v4.4 vs Benincasa-Dowker Blind Benchmark (N={N}, seeds={n_seeds}) ===")
        print(
            f"Locked parameters: a={A_PAR}, b={B_PAR}, g={G_PAR}, p={P_PAR}, "
            f"m^2={M2_PAR}, eta_field={ETA_FIELD}, T={T_PAR} (n_bos={ETA_FIELD/T_PAR:.1f})"
        )
        h1 = (
            f"{'Ensemble':15s} | {'d_MM':>5s} | {'d_mid':>5s} | {'f_K2':>5s} | "
            f"{'F_struct':>12s} | {'ln det Pi':>9s} | {'F_joint / T':>14s} | "
            f"{'|S_BD^(2d)|':>12s} | {'|S_BD^(4d)|':>12s}"
        )
        print("-" * len(h1))
        print(h1)
        print("-" * len(h1))
        for name in ensembles:
            print(
                f"{name:15s} | "
                f"{np.nanmean(arr(name, 'd_MM')):5.2f} | "
                f"{np.nanmean(arr(name, 'd_mid')):5.2f} | "
                f"{np.mean(arr(name, 'f_K2')):5.3f} | "
                f"{np.mean(arr(name, 'F_struct')):7.1f}±{np.std(arr(name, 'F_struct')):4.1f} | "
                f"{np.mean(arr(name, 'logdet_Pi')):9.2f} | "
                f"{np.mean(arr(name, 'F_joint_over_T')):8.1f}±{np.std(arr(name, 'F_joint_over_T')):5.1f} | "
                f"{np.mean(arr(name, 'abs_S_BD2')):7.1f}±{np.std(arr(name, 'abs_S_BD2')):4.1f} | "
                f"{np.mean(arr(name, 'abs_S_BD4')):7.1f}±{np.std(arr(name, 'abs_S_BD4')):4.1f}"
            )
        print("-" * len(h1))

        # Таблица отношения сигнал/шум Z_sep против пуассоновского посева Minkowski_2D и Minkowski_4D
        print("\n=== Безразмерный критерий разделимости Z_sep (Non-Manifold vs Minkowski_2D) ===")
        h2 = (
            f"{'Target vs Minkowski_2D':24s} | {'Delta(F_joint/T)':>16s} | "
            f"{'Z_sep(F_joint)':>14s} | {'Z_sep(F_joint+deg^2)':>20s} | "
            f"{'Z_sep(|S_BD^(2d)|)':>18s} | {'Z_sep(S_BD_smear)':>17s}"
        )
        print("-" * len(h2))
        print(h2)
        print("-" * len(h2))
        for non_man in ["KR_3layer_T3", "Random_DAG_35", "KR_2layer_T2"]:
            d_fj = float(np.mean(arr(non_man, "F_joint_over_T")) - np.mean(arr("Minkowski_2D", "F_joint_over_T")))
            z_fj = _separation_snr(arr(non_man, "F_joint_over_T"), arr("Minkowski_2D", "F_joint_over_T"))
            z_fdeg = _separation_snr(arr(non_man, "F_joint_deg_over_T"), arr("Minkowski_2D", "F_joint_deg_over_T"))
            z_bd2 = _separation_snr(arr(non_man, "abs_S_BD2"), arr("Minkowski_2D", "abs_S_BD2"))
            z_bds = _separation_snr(arr(non_man, "abs_S_BD2_smear"), arr("Minkowski_2D", "abs_S_BD2_smear"))
            print(
                f"{non_man:24s} | {d_fj:+16.1f} | "
                f"{z_fj:+13.2f}s | {z_fdeg:+19.2f}s | "
                f"{z_bd2:+17.2f}s | {z_bds:+16.2f}s"
            )
        print("-" * len(h2))
        print()

    return stats


def run_scaling_sweep(N_list=(32, 64, 96), n_seeds=12, seed_base=5000, verbose=True):
    """
    Проверка асимптотического роста подавления не-многообразных порядков с ростом N
    при фиксированных параметрах (eta_field=1.0, T=0.5).
    """
    summary = {}
    if verbose:
        print("=== Масштабирование подавления с ростом N (Minkowski_2D vs KR_3layer_T3 & Random_DAG) ===")
        hdr = (
            f"{'N':>4s} | {'F_joint/T (Mink2D)':>18s} | {'F_joint/T (KR_T3)':>18s} | "
            f"{'Ratio T3/Mink2D':>15s} | {'Z_sep(F_joint, T3)':>18s} | {'Z_sep(|S_BD2|, T3)':>18s}"
        )
        print("-" * len(hdr))
        print(hdr)
        print("-" * len(hdr))

    for idx, N in enumerate(N_list):
        st = run_bd_vs_cpp_benchmark(N=N, n_seeds=n_seeds, seed_base=seed_base + 500 * idx, verbose=False)
        arr = lambda ens, k: np.array([x[k] for x in st[ens]], dtype=float)
        m_m2 = float(np.mean(arr("Minkowski_2D", "F_joint_over_T")))
        s_m2 = float(np.std(arr("Minkowski_2D", "F_joint_over_T")))
        m_t3 = float(np.mean(arr("KR_3layer_T3", "F_joint_over_T")))
        s_t3 = float(np.std(arr("KR_3layer_T3", "F_joint_over_T")))
        z_fj = _separation_snr(arr("KR_3layer_T3", "F_joint_over_T"), arr("Minkowski_2D", "F_joint_over_T"))
        z_bd = _separation_snr(arr("KR_3layer_T3", "abs_S_BD2"), arr("Minkowski_2D", "abs_S_BD2"))
        summary[N] = {
            "Minkowski_2D_mean": m_m2,
            "KR_T3_mean": m_t3,
            "ratio_T3_to_Mink2D": m_t3 / max(1e-12, m_m2),
            "Z_sep_F_joint": z_fj,
            "Z_sep_S_BD2": z_bd,
        }
        if verbose:
            print(
                f"{N:4d} | {m_m2:10.1f}±{s_m2:6.1f} | {m_t3:10.1f}±{s_t3:6.1f} | "
                f"{m_t3 / max(1e-12, m_m2):14.2f}x | {z_fj:+17.2f}s | {z_bd:+17.2f}s"
            )
    if verbose:
        print("-" * len(hdr))
        print()
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CPP v4.4 vs Benincasa-Dowker & Myrheim-Meyer Blind Test on Minkowski Sprinklings"
    )
    parser.add_argument("--N", type=int, default=64, help="Число событий N для детального сравнения (по умолчанию: 64)")
    parser.add_argument("--seeds", type=int, default=20, help="Число независимых сидов (по умолчанию: 20)")
    parser.add_argument(
        "--scaling",
        action="store_true",
        help="Дополнительно запустить скан масштабирования по N in {32, 64, 96}",
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
        print(f"CPP v4.4 Minkowski vs Benincasa-Dowker log: {log_path}")
        print(f"Started: {datetime.now().isoformat(timespec='seconds')}")
        print("=" * 108)
        run_bd_vs_cpp_benchmark(N=args.N, n_seeds=args.seeds, verbose=True)
        if args.scaling:
            run_scaling_sweep(N_list=(32, 64, 96), n_seeds=max(8, args.seeds // 2), verbose=True)
        print("=" * 108)
        print(f"Finished: {datetime.now().isoformat(timespec='seconds')}")
        print(f"Results saved to: {log_path}")
    finally:
        sys.stdout = old_stdout
        log_file.close()
        print(f"\nResults also saved to: {log_path}")