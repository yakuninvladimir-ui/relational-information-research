# test7_gas_bh.py
import os
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================== НАСТРОЙКИ ==================

TABLE1_FILE   = "table1.mrt"
ROTMOD_FOLDER = "rotmod"
DENS_FOLDER   = "dens"

ML_DISK  = 0.5
ML_BULGE = 0.7

# Параметры окна по Σ_gas
SIGMA_GAS_MIN_REL = 0.3
SIGMA_GAS_MAX_REL = 3.0

# Параметры влияния балджа/ЧД в факторе F_BH
F0_BULGE = 0.3   # характерная доля балджа
DELTA_BH = 1.0   # степень подавления (знак физически интерпретируем уже по результату)

# ================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==================


def bulge_fraction_from_T(T):
    """
    Простейшее приближение f_bulge по морфологическому типу T (SPARC):
    ранние типы -> большой балдж, поздние -> маленький.
    Это именно прокси, а не точная фотометрия.
    """
    if T <= 0:
        return 0.8
    elif T <= 2:
        return 0.6
    elif T <= 4:
        return 0.4
    elif T <= 7:
        return 0.2
    else:
        return 0.05


def load_table1(path=TABLE1_FILE):
    """Читаем table1.mrt (как в прошлых тестах)."""
    with open(path, "r", encoding="latin-1") as f:
        lines = f.readlines()

    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "" or line.startswith("Title"):
            continue
        if i > 50 and line.strip().split()[0] == "CamB":
            start_idx = i
            break
    if start_idx is None:
        raise RuntimeError("Не найдено начало данных в table1.mrt")

    data_str = "".join(lines[start_idx:])
    df = pd.read_fwf(
        io.StringIO(data_str),
        header=None,
        names=[
            "Galaxy", "T", "D", "e_D", "f_D",
            "Inc", "e_Inc",
            "L36", "e_L36",
            "Reff", "SBeff",
            "Rdisk", "SBdisk",
            "MHI", "RHI",
            "Vflat", "e_Vflat",
            "Q", "Ref"
        ]
    )
    df = df.dropna(subset=["Galaxy"]).reset_index(drop=True)
    return df


def load_rotmod(gal_name):
    """Читаем *_rotmod.dat."""
    base = gal_name.strip()
    candidates = [
        os.path.join(ROTMOD_FOLDER, f"{base}_rotmod.dat"),
        os.path.join(ROTMOD_FOLDER, f"{base.replace(' ', '')}_rotmod.dat"),
        f"{base}_rotmod.dat",
        f"{base.replace(' ', '')}_rotmod.dat",
    ]
    path = None
    for c in candidates:
        if os.path.exists(c):
            path = c
            break
    if path is None:
        return None

    cols = ['Rad', 'Vobs', 'errV', 'Vgas', 'Vdisk', 'Vbul', 'SBdisk', 'SBbul']
    df = pd.read_csv(path, sep=r"\s+", comment="#", names=cols)
    if len(df) < 3:
        return None
    return df


def load_dens(gal_name):
    """Читаем *.dens (Rad[kpc], SBdisk, SBbulge)."""
    base = gal_name.strip()
    candidates = [
        os.path.join(DENS_FOLDER, f"{base}.dens"),
        os.path.join(DENS_FOLDER, f"{base.replace(' ', '')}.dens"),
        f"{base}.dens",
        f"{base.replace(' ', '')}.dens",
    ]
    path = None
    for c in candidates:
        if os.path.exists(c):
            path = c
            break
    if path is None:
        return None

    df = pd.read_csv(path, sep=r"\s+", comment="#", header=None,
                     names=["Rad_kpc", "SBdisk", "SBbulge"])
    if len(df) < 3:
        return None
    return df


# ================== СБОР РАДИАЛЬНЫХ ТОЧЕК ==================


def collect_radial_points():
    tab = load_table1(TABLE1_FILE)

    all_sigma_star = []
    all_sigma_gas = []
    all_g_dm = []
    all_g_bar = []
    all_g_obs = []
    all_f_bulge = []

    for _, row in tab.iterrows():
        gal = row["Galaxy"].strip()
        T = row["T"]
        f_bulge_global = bulge_fraction_from_T(T)

        rot = load_rotmod(gal)
        dens = load_dens(gal)
        if rot is None or dens is None:
            continue

        # радиусы и скорости из rotmod
        R_kpc = rot["Rad"].values
        R_m = R_kpc * 3.086e19  # kpc -> m
        vfac = 1000.0           # km/s -> m/s

        V_obs = np.abs(rot["Vobs"].values) * vfac
        V_gas = np.abs(rot["Vgas"].values) * vfac
        V_disk = np.abs(rot["Vdisk"].values) * vfac
        V_bul = np.abs(rot["Vbul"].values) * vfac

        # Σ_* из .dens (Lsun/pc^2), интерполяция на те же радиусы
        R_star_kpc = dens["Rad_kpc"].values
        SBdisk = dens["SBdisk"].values
        SBbulge = dens["SBbulge"].values
        sigma_star_profile = SBdisk + SBbulge  # относительные единицы

        sigma_star_interp = np.interp(
            R_kpc, R_star_kpc, sigma_star_profile,
            left=np.nan, right=np.nan
        )

        # Газовая "поверхностная плотность" (условная)
        sigma_gas = (V_gas**2 / R_m)  # ∝ Σ_gas

        # Гравитации
        V_bar_sq = (
            V_gas**2 +
            (V_disk**2) * ML_DISK +
            (V_bul**2) * ML_BULGE
        )
        V_obs_sq = V_obs**2

        g_obs = V_obs_sq / R_m
        g_bar = V_bar_sq / R_m
        g_dm = g_obs - g_bar

        # базовый фильтр
        valid = (
            np.isfinite(sigma_star_interp) &
            np.isfinite(sigma_gas) &
            np.isfinite(g_obs) &
            np.isfinite(g_bar) &
            (R_m > 0) &
            (g_obs > 0) &
            (g_bar > 0)
        )
        if np.count_nonzero(valid) < 5:
            continue

        all_sigma_star.append(sigma_star_interp[valid])
        all_sigma_gas.append(sigma_gas[valid])
        all_g_dm.append(g_dm[valid])
        all_g_bar.append(g_bar[valid])
        all_g_obs.append(g_obs[valid])
        # один и тот же f_bulge для всех радиальных точек данной галактики
        all_f_bulge.append(
            np.full(np.count_nonzero(valid), f_bulge_global)
        )

    if not all_sigma_star:
        raise RuntimeError("Не удалось собрать ни одной галактики с валидными данными.")

    sigma_star = np.concatenate(all_sigma_star)
    sigma_gas = np.concatenate(all_sigma_gas)
    g_dm = np.concatenate(all_g_dm)
    g_bar = np.concatenate(all_g_bar)
    g_obs = np.concatenate(all_g_obs)
    f_bulge = np.concatenate(all_f_bulge)

    return sigma_star, sigma_gas, g_dm, g_bar, g_obs, f_bulge


# ================== ОСНОВНОЙ АНАЛИЗ ==================


def run_radial_model():
    sigma_star, sigma_gas, g_dm, g_bar, g_obs, f_bulge = collect_radial_points()
    print(f"Всего радиальных точек: {len(sigma_star)}")

    ratio_dm_bar = g_dm / g_bar

    base_mask = (
        np.isfinite(sigma_star) & (sigma_star > 0) &
        np.isfinite(sigma_gas) & (sigma_gas > 0) &
        np.isfinite(ratio_dm_bar) & (ratio_dm_bar > 0)
    )

    sigma_star = sigma_star[base_mask]
    sigma_gas = sigma_gas[base_mask]
    g_dm = g_dm[base_mask]
    g_bar = g_bar[base_mask]
    ratio_dm_bar = ratio_dm_bar[base_mask]
    f_bulge = f_bulge[base_mask]

    print(f"После базового фильтра: {len(sigma_star)} точек")

    # --- Диаграммы g_DM/g_bar vs Σ_gas и Σ_* ---
    plt.figure(figsize=(7, 5))
    plt.hexbin(np.log10(sigma_gas), np.log10(ratio_dm_bar),
               gridsize=40, cmap="viridis", mincnt=5)
    plt.colorbar(label="N points")
    plt.xlabel(r"log$_{10}\,\Sigma_{\rm gas}$ (условн.)")
    plt.ylabel(r"log$_{10}\,(g_{\rm DM}/g_{\rm bar})$")
    plt.title("RADIAL: g_DM/g_bar vs Σ_gas")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.hexbin(np.log10(sigma_star), np.log10(ratio_dm_bar),
               gridsize=40, cmap="magma", mincnt=5)
    plt.colorbar(label="N points")
    plt.xlabel(r"log$_{10}\,\Sigma_\star$ (L$_\odot$/pc$^2$)")
    plt.ylabel(r"log$_{10}\,(g_{\rm DM}/g_{\rm bar})$")
    plt.title("RADIAL: g_DM/g_bar vs Σ_* (генерация)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # --- Нормировки и фактор F_BH ---
    sigma_gas_med = np.median(sigma_gas)
    sigma_gas_rel = sigma_gas / sigma_gas_med

    # окно по Σ_gas
    retain = ((sigma_gas_rel >= SIGMA_GAS_MIN_REL) &
              (sigma_gas_rel <= SIGMA_GAS_MAX_REL))

    # фактор балджа / ЧД
    F_BH = (1.0 + f_bulge / F0_BULGE) ** (-DELTA_BH)

    # ===== РЕГРЕССИЯ ТОЛЬКО ПО Σ_gas И F_BH =====
    mask_reg = retain & (g_dm > 0) & np.isfinite(g_dm)
    print(f"Точек после фильтра для регрессии: {np.count_nonzero(mask_reg)}")

    log_gdm = np.log10(g_dm[mask_reg])
    x_gas = np.log10(sigma_gas[mask_reg])
    x_fbh = np.log10(F_BH[mask_reg])

    # регрессия: log g_DM = C + β log Σ_gas + γ log F_BH
    X = np.vstack([np.ones_like(x_gas), x_gas, x_fbh]).T
    coeffs, *_ = np.linalg.lstsq(X, log_gdm, rcond=None)
    C, beta_hat, gamma_hat = coeffs

    # предсказание и метрики
    log_gdm_pred = C + beta_hat * x_gas + gamma_hat * x_fbh
    residuals = log_gdm - log_gdm_pred
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((log_gdm - np.mean(log_gdm))**2)
    R2 = 1.0 - ss_res / ss_tot
    corr = np.corrcoef(log_gdm, log_gdm_pred)[0, 1]

    print("=== РЕЗУЛЬТАТЫ РЕГРЕССИИ (лог g_DM) по Σ_gas и F_BH ===")
    print("log g_DM ≈ C + β log Σ_gas + γ log F_BH")
    print(f"C    = {C:.3f}")
    print(f"β    = {beta_hat:.3f}")
    print(f"γ    = {gamma_hat:.3f}")
    print(f"R²   = {R2:.3f}")
    print(f"corr = {corr:.3f}")

    # построим модель g_DM для всех точек
    log_sigma_gas_all = np.log10(sigma_gas)
    log_F_BH_all = np.log10(F_BH)

    log_gdm_model_all = (
        C + beta_hat * log_sigma_gas_all +
        gamma_hat * log_F_BH_all
    )
    gdm_model_all = 10**log_gdm_model_all

    # График модель vs наблюдение
    valid_corr = (g_dm > 0) & np.isfinite(g_dm) & np.isfinite(gdm_model_all)
    log_obs = np.log10(g_dm[valid_corr])
    log_mod = np.log10(gdm_model_all[valid_corr])

    plt.figure(figsize=(7, 5))
    plt.hexbin(log_mod, log_obs, gridsize=40, cmap="plasma", mincnt=5)
    lim_min = min(log_mod.min(), log_obs.min())
    lim_max = max(log_mod.max(), log_obs.max())
    plt.plot([lim_min, lim_max], [lim_min, lim_max],
             "r--", label="model = obs")
    plt.xlabel(r"log$_{10}\,g_{\rm DM}^{\rm model}$")
    plt.ylabel(r"log$_{10}\,g_{\rm DM}^{\rm obs}$")
    plt.title("Сравнение модели g_DM(Σ_gas, F_BH) с наблюдениями")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Остатки как функция Σ_* и Σ_gas
    delta_log = log_obs - log_mod[valid_corr]

    plt.figure(figsize=(7, 5))
    plt.scatter(np.log10(sigma_star[valid_corr]), delta_log, s=5, alpha=0.4)
    plt.axhline(0.0, color="k", linestyle="--")
    plt.xlabel(r"log$_{10}\,\Sigma_\star$")
    plt.ylabel(r"$\Delta \log_{10} g_{\rm DM}$ (obs - model)$")
    plt.title("Остатки модели g_DM(Σ_gas, F_BH) vs log Σ_*")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.scatter(np.log10(sigma_gas[valid_corr]), delta_log, s=5, alpha=0.4)
    plt.axhline(0.0, color="k", linestyle="--")
    plt.xlabel(r"log$_{10}\,\Sigma_{\rm gas}$")
    plt.ylabel(r"$\Delta \log_{10} g_{\rm DM}$ (obs - model)$")
    plt.title("Остатки модели g_DM(Σ_gas, F_BH) vs log Σ_gas")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_radial_model()
