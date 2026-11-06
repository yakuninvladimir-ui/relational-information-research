import os
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================== НАСТРОЙКИ ==================

TABLE1_FILE   = "table1.mrt"
ROTMOD_FOLDER = "rotmod"   # где лежат *_rotmod.dat
DENS_FOLDER   = "dens"   # где лежат *.dens (или поправь при необходимости)

ML_DISK  = 0.5
ML_BULGE = 0.7
G_SI     = 6.674e-11


# ================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==================

def load_table1(path=TABLE1_FILE):
    """Читаем table1.mrt (как в предыдущих скриптах)."""
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
    """Читаем *.dens (Rad[kpc], SBdisk, SBbulge)."""
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

    df = pd.read_csv(path, sep=r"\s+", comment="#", header=None,
                     names=["Rad_kpc", "SBdisk", "SBbulge"])
    if len(df) < 3:
        return None
    return df


# ================== СБОР РАДИАЛЬНЫХ ТОЧЕК ==================

def collect_points_sigma_star_vs_dmbar():
    tab = load_table1(TABLE1_FILE)

    all_sigma_star = []
    all_ratio_dmbar = []

    for _, row in tab.iterrows():
        gal = row["Galaxy"].strip()

        rot = load_rotmod(gal)
        dens = load_dens(gal)
        if rot is None or dens is None:
            continue

        # --- радиусы и скорости из rotmod ---
        R_kpc = rot["Rad"].values
        R_m   = R_kpc * 3.086e19
        vfac  = 1000.0  # km/s -> m/s

        V_obs  = np.abs(rot["Vobs"].values)  * vfac
        V_gas  = np.abs(rot["Vgas"].values)  * vfac
        V_disk = np.abs(rot["Vdisk"].values) * vfac
        V_bul  = np.abs(rot["Vbul"].values)  * vfac

        # --- Σ_* из .dens (SBdisk+SBbulge), интерполяция на радиусы rotmod ---
        R_star_kpc = dens["Rad_kpc"].values
        SBdisk     = dens["SBdisk"].values
        SBbulge    = dens["SBbulge"].values
        sigma_star_profile = SBdisk + SBbulge   # Lsun/pc^2 (относительные единицы)

        sigma_star_interp = np.interp(
            R_kpc, R_star_kpc, sigma_star_profile,
            left=np.nan, right=np.nan
        )

        # --- гравитации ---
        V_bar_sq = (
            V_gas**2 +
            (V_disk**2) * ML_DISK +
            (V_bul**2) * ML_BULGE
        )
        V_obs_sq = V_obs**2

        g_obs = V_obs_sq / R_m
        g_bar = V_bar_sq / R_m
        g_dm  = g_obs - g_bar

        # маска валидных точек: всё >0 и конечно
        mask = (
            np.isfinite(sigma_star_interp) & (sigma_star_interp > 0) &
            np.isfinite(g_bar) & (g_bar > 0) &
            np.isfinite(g_dm)  & (g_dm > 0)
        )

        if np.count_nonzero(mask) < 5:
            continue

        sig_star = sigma_star_interp[mask]
        ratio_dmbar = g_dm[mask] / g_bar[mask]

        # отфильтруем ratio<=0 на всякий случай
        pos = ratio_dmbar > 0
        if np.count_nonzero(pos) < 3:
            continue

        all_sigma_star.append(sig_star[pos])
        all_ratio_dmbar.append(ratio_dmbar[pos])

    if not all_sigma_star:
        raise RuntimeError("Не удалось собрать ни одной галактики с валидными точками.")

    sigma_star = np.concatenate(all_sigma_star)
    ratio_dmbar = np.concatenate(all_ratio_dmbar)

    return sigma_star, ratio_dmbar


# ================== ОСНОВНОЙ АНАЛИЗ ==================

def run_sigma_star_fit():
    sigma_star, ratio_dmbar = collect_points_sigma_star_vs_dmbar()
    print(f"Всего точек: {len(sigma_star)}")

    # логарифмы
    log_sigma_star = np.log10(sigma_star)
    log_ratio      = np.log10(ratio_dmbar)

    # грубый фильтр по диапазонам (убрать явные хвосты / выбросы, если хочется)
    # тут можно при желании ограничить, например, log_sigma_star∈[-1,4], log_ratio∈[-2,2]

    # линейный фит y = a + b x
    b, a = np.polyfit(log_sigma_star, log_ratio, 1)
    # коэффициент корреляции
    R = np.corrcoef(log_sigma_star, log_ratio)[0, 1]

    print("Фит зависимости log10(g_DM/g_bar) = a + b * log10(Sigma_star):")
    print(f"  a = {a:.3f}")
    print(f"  b = {b:.3f}  (=> g_DM/g_bar ∝ Sigma_star^{b:.3f})")
    print(f"Пирсоновская корреляция R = {R:.3f}")

    # --- График с линией фита ---
    plt.figure(figsize=(7, 5))
    hb = plt.hexbin(log_sigma_star, log_ratio,
                    gridsize=50, cmap="inferno", mincnt=5)
    plt.colorbar(hb, label="N points")
    # линия фита
    x_line = np.linspace(log_sigma_star.min(), log_sigma_star.max(), 100)
    y_line = a + b * x_line
    plt.plot(x_line, y_line, "cyan", lw=2,
             label=f"fit: y = {a:.2f} + {b:.2f} x")

    plt.xlabel(r"log$_{10}\,\Sigma_\star$ (L$_\odot$/pc$^2$)")
    plt.ylabel(r"log$_{10}\,(g_{\rm DM}/g_{\rm bar})$")
    plt.title("RADIAL: зависимость TM/барионы от Σ_*")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_sigma_star_fit()
