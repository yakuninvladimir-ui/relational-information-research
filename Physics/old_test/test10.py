import os
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================== НАСТРОЙКИ ==================

TABLE1_FILE   = "table1.mrt"
ROTMOD_FOLDER = "rotmod"   # поправь, если файлы в другом месте
DENS_FOLDER   = "dens"

ML_DISK  = 0.5
ML_BULGE = 0.7

# параметры a0(Σ*)
B_SLOPE = -0.22        # из test8: g_DM/g_bar ∝ Σ_*^{-0.22}
A0_REF  = 1.2e-10      # м/с^2, стандартный MOND-порядок

# ================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==================

def load_table1(path=TABLE1_FILE):
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
    base = gal_name.strip()
    candidates = [
        os.path.join(ROTMOD_FOLDER, f"{base}_rotmod.dat"),
        os.path.join(ROTMOD_FOLDER, f"{base.replace(' ','')}_rotmod.dat"),
        f"{base}_rotmod.dat",
        f"{base.replace(' ','')}_rotmod.dat",
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
    base = gal_name.strip()
    candidates = [
        os.path.join(DENS_FOLDER, f"{base}.dens"),
        os.path.join(DENS_FOLDER, f"{base.replace(' ','')}.dens"),
        f"{base}.dens",
        f"{base.replace(' ','')}.dens",
    ]
    path = None
    for c in candidates:
        if os.path.exists(c):
            path = c
            break
    if path is None:
        return None

    # предполагаем формат: Rad_kpc, SBdisk, SBbulge
    df = pd.read_csv(path, sep=r"\s+", comment="#", header=None,
                     names=["Rad_kpc", "SBdisk", "SBbulge"])
    if len(df) < 3:
        return None
    return df


def nu_func(x):
    """Интерполяционная функция ν(x) для RAR (MOND-подобная)."""
    x = np.array(x, dtype=float)
    # защитимся от нулей/отрицательных
    x[x <= 0] = 1e-30
    return 1.0 / (1.0 - np.exp(-np.sqrt(x)))


# ================== СБОР РАДИАЛЬНЫХ ТОЧЕК ==================

def collect_rar_points():
    tab = load_table1()
    all_gbar   = []
    all_gobs   = []
    all_sigma_star = []

    for _, row in tab.iterrows():
        gal = row["Galaxy"].strip()
        rot = load_rotmod(gal)
        dens = load_dens(gal)

        if rot is None or dens is None:
            continue

        # радиусы и скорости
        R_kpc = rot["Rad"].values
        R_m   = R_kpc * 3.086e19
        vfac  = 1000.0

        V_obs  = np.abs(rot["Vobs"].values)  * vfac
        V_gas  = np.abs(rot["Vgas"].values)  * vfac
        V_disk = np.abs(rot["Vdisk"].values) * vfac
        V_bul  = np.abs(rot["Vbul"].values)  * vfac

        # Σ_* из dens (фотометрическая яркость: SBdisk+SBbulge)
        R_star = dens["Rad_kpc"].values
        SBdisk = dens["SBdisk"].values
        SBbul  = dens["SBbulge"].values
        sigma_star_prof = SBdisk + SBbul  # Lsun/pc^2, в относительных единицах

        sigma_star = np.interp(
            R_kpc, R_star, sigma_star_prof,
            left=np.nan, right=np.nan
        )

        # гравитации
        V_bar_sq = (
            V_gas**2 +
            (V_disk**2) * ML_DISK +
            (V_bul**2) * ML_BULGE
        )
        V_obs_sq = V_obs**2

        g_obs = V_obs_sq / R_m
        g_bar = V_bar_sq / R_m

        mask = (
            np.isfinite(sigma_star) & (sigma_star > 0) &
            np.isfinite(g_bar) & (g_bar > 0) &
            np.isfinite(g_obs) & (g_obs > 0)
        )

        if np.count_nonzero(mask) < 5:
            continue

        all_sigma_star.append(sigma_star[mask])
        all_gbar.append(g_bar[mask])
        all_gobs.append(g_obs[mask])

    if not all_gbar:
        raise RuntimeError("Не удалось собрать ни одной галактики с валидными RAR-данными.")

    sigma_star = np.concatenate(all_sigma_star)
    g_bar      = np.concatenate(all_gbar)
    g_obs      = np.concatenate(all_gobs)

    return sigma_star, g_bar, g_obs


# ================== ОСНОВНАЯ ФУНКЦИЯ ==================

def run_rar_a0_sigma():
    sigma_star, g_bar, g_obs = collect_rar_points()
    print(f"Всего радиальных точек: {len(g_bar)}")

    # нормировка Σ0 — возьмём медиану по всем точкам
    Sigma0 = np.median(sigma_star)
    print(f"Медиана Σ_* ≈ {Sigma0:.3g} (в тех же условных единицах, что и .dens)")

    # --- 1) Модель с КОНСТАНТНЫМ a0 ---
    a0_const = A0_REF
    x_const = g_bar / a0_const
    g_model_const = g_bar * nu_func(x_const)

    # --- 2) Модель с a0(Σ_*) ---
    a0_local = A0_REF * (sigma_star / Sigma0)**B_SLOPE
    x_var = g_bar / a0_local
    g_model_var = g_bar * nu_func(x_var)

    # общий фильтр: только положительные и конечные значения
    m = (
        (g_bar > 0) & (g_obs > 0) &
        (g_model_const > 0) & (g_model_var > 0) &
        np.isfinite(g_bar) & np.isfinite(g_obs) &
        np.isfinite(g_model_const) & np.isfinite(g_model_var) &
        (sigma_star > 0) & np.isfinite(sigma_star)
    )

    g_bar_m        = g_bar[m]
    g_obs_m        = g_obs[m]
    g_model_const_m = g_model_const[m]
    g_model_var_m   = g_model_var[m]
    sigma_star_m    = sigma_star[m]

    print(f"Точек после фильтрации: {len(g_bar_m)}")

    log_gbar   = np.log10(g_bar_m)
    log_gobs   = np.log10(g_obs_m)
    log_gmodel_const = np.log10(g_model_const_m)
    log_gmodel_var   = np.log10(g_model_var_m)
    log_sigma  = np.log10(sigma_star_m)

    # --- RAR: obs vs model (показываем, как и раньше, только вариативный a0(Σ_*)) ---
    plt.figure(figsize=(7,6))
    plt.hexbin(log_gbar, log_gobs,    gridsize=50, cmap="Blues",   mincnt=5, alpha=0.7)
    plt.hexbin(log_gbar, log_gmodel_var, gridsize=50, cmap="Oranges", mincnt=5, alpha=0.5)
    lim_min = min(log_gbar.min(), log_gobs.min(), log_gmodel_var.min())
    lim_max = max(log_gbar.max(), log_gobs.max(), log_gmodel_var.max())
    plt.plot([lim_min, lim_max], [lim_min, lim_max], "k--", label="g_obs = g_bar")
    plt.xlabel(r"log$_{10}\,g_{\rm bar}$ [м/с$^2$]")
    plt.ylabel(r"log$_{10}\,g$ [м/с$^2$]")
    plt.title("RAR: наблюдаемое (синее) и модель с a$_0(\\Sigma_*)$ (оранжевое)")
    plt.colorbar(label="N points (слои)\nсиняя: obs, оранжевая: model")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # --- Остатки: Δ log g для обеих моделей ---
    residual_const = log_gobs - log_gmodel_const
    residual_var   = log_gobs - log_gmodel_var

    # Δ log g vs log g_bar (для вариативного a0, как было)
    plt.figure(figsize=(7,5))
    sc = plt.scatter(log_gbar, residual_var, s=5, alpha=0.4, c=log_sigma, cmap="plasma")
    plt.axhline(0, color="k", linestyle="--")
    plt.xlabel(r"log$_{10}\,g_{\rm bar}$")
    plt.ylabel(r"Δ log$_{10}\,g$ (obs - model, a0(Σ_*))")
    plt.title("Остатки RAR с a$_0(\\Sigma_*)$ vs log g_bar (цвет = log Σ_*)")
    plt.colorbar(sc, label=r"log$_{10}\,\Sigma_\star$")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Δ log g vs log Σ_* (для вариативного a0, как было)
    plt.figure(figsize=(7,5))
    plt.scatter(log_sigma, residual_var, s=5, alpha=0.4)
    plt.axhline(0, color="k", linestyle="--")
    plt.xlabel(r"log$_{10}\,\Sigma_\star$")
    plt.ylabel(r"Δ log$_{10}\,g$ (obs - model, a0(Σ_*))")
    plt.title("Остатки RAR с a$_0(\\Sigma_*)$ vs Σ_*")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # --- RMS сравнение ---
    rms_const = np.sqrt(np.mean(residual_const**2))
    rms_var   = np.sqrt(np.mean(residual_var**2))

    print(f"RMS(Δ log g) для модели с КОНСТАНТНЫМ a0 = {rms_const:.3f} dex")
    print(f"RMS(Δ log g) для модели с a0(Σ_*)      = {rms_var:.3f} dex")


if __name__ == "__main__":
    run_rar_a0_sigma()
