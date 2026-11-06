import os
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ================== КОНСТАНТЫ ==================

DATA_FOLDER = "rotmod"
TABLE1_FILE = "table1.mrt"

G_SI = 6.674e-11
M_SUN = 1.989e30

ML_DISK = 0.5
ML_BULGE = 0.7

M0_SCALE = 1e10  # Msun – масштаб для степеней по массе


# ================== ЧТЕНИЕ TABLE1.MRT ==================

def load_table1(path=TABLE1_FILE):
    """Грубый парсер table1.mrt (SPARC)."""
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


# ================== АНАЛИЗ ОДНОЙ ГАЛАКТИКИ (ROTМOD) ==================

def analyze_rotmod_dm_mass(galaxy_name, data_folder=DATA_FOLDER):
    """
    Для одной галактики:
      - оценивает глобальную DM массу M_DM_total внутри R_max
        как медиану M_DM(r) по нескольким внешним точкам:
           M_DM(r) = [V_obs^2(r) - V_bar^2(r)] * r / G
      - оценивает f_gas и f_bulge по тем же внешним точкам.
    Возвращает (M_DM_total [Msun], f_gas, f_bulge).
    """
    rot_path = os.path.join(data_folder, f"{galaxy_name}_rotmod.dat")
    if not os.path.exists(rot_path):
        alt = galaxy_name.replace(" ", "")
        rot_path = os.path.join(data_folder, f"{alt}_rotmod.dat")
        if not os.path.exists(rot_path):
            return None, None, None

    col_names = ['Rad', 'Vobs', 'errV', 'Vgas', 'Vdisk', 'Vbul', 'SBdisk', 'SBbul']
    try:
        df = pd.read_csv(rot_path, sep=r'\s+', comment='#', names=col_names)
    except Exception:
        return None, None, None

    if len(df) < 5:
        return None, None, None

    # --- единицы и базовые величины ---
    R_kpc = df["Rad"].values
    R_m = R_kpc * 3.086e19     # kpc -> m
    v_factor = 1000.0          # km/s -> m/s

    V_obs = np.abs(df["Vobs"].values) * v_factor
    V_gas = np.abs(df["Vgas"].values) * v_factor
    V_disk = np.abs(df["Vdisk"].values) * v_factor
    V_bul = np.abs(df["Vbul"].values) * v_factor

    # барионная скорость (с учётом M/L)
    V_bar_sq = (
        V_gas**2 +
        (V_disk**2) * ML_DISK +
        (V_bul**2) * ML_BULGE
    )
    V_obs_sq = V_obs**2

    valid = (R_m > 0) & np.isfinite(V_obs_sq) & np.isfinite(V_bar_sq)
    if np.count_nonzero(valid) < 5:
        return None, None, None

    R_m = R_m[valid]
    V_bar_sq = V_bar_sq[valid]
    V_obs_sq = V_obs_sq[valid]
    V_gas = V_gas[valid]
    V_disk = V_disk[valid]
    V_bul = V_bul[valid]

    # --- выбираем внешнюю область ---
    R_max = R_m.max()
    outer = R_m > 0.7 * R_max
    if np.count_nonzero(outer) < 3:
        outer = R_m > 0.5 * R_max
    if np.count_nonzero(outer) < 3:
        outer = np.ones_like(R_m, dtype=bool)

    R_out = R_m[outer]
    V_obs_sq_out = V_obs_sq[outer]
    V_bar_sq_out = V_bar_sq[outer]
    V_gas_out = V_gas[outer]
    V_disk_out = V_disk[outer]
    V_bul_out = V_bul[outer]

    # --- масса DM внутри r: M_DM(r) = (V_obs^2 - V_bar^2) * r / G ---
    delta_V_sq = V_obs_sq_out - V_bar_sq_out
    dm_mask = delta_V_sq > 0
    if np.count_nonzero(dm_mask) == 0:
        return 0.0, 0.0, 0.0

    delta_V_sq = delta_V_sq[dm_mask]
    R_out_dm = R_out[dm_mask]

    M_DM_SI = delta_V_sq * R_out_dm / G_SI
    # медиана по внешним точкам
    M_DM_total = np.median(M_DM_SI) / M_SUN   # в Msun

    # --- f_gas и f_bulge по тем же точкам ---
    V_gas_sq = V_gas_out[dm_mask]**2
    V_disk_sq = (V_disk_out[dm_mask]**2) * ML_DISK
    V_bul_sq = (V_bul_out[dm_mask]**2) * ML_BULGE

    M_gas_proxy = V_gas_sq
    M_disk_proxy = V_disk_sq
    M_bul_proxy = V_bul_sq

    M_star_proxy = M_disk_proxy + M_bul_proxy
    M_tot_proxy = M_gas_proxy + M_star_proxy

    if np.all(M_tot_proxy <= 0):
        f_gas = 0.0
        f_bulge = 0.0
    else:
        f_gas = np.mean(M_gas_proxy / (M_gas_proxy + M_star_proxy))
        f_bulge = np.mean(M_bul_proxy / (M_gas_proxy + M_disk_proxy + M_bul_proxy))

    f_gas = float(np.clip(f_gas, 0.0, 1.0))
    f_bulge = float(np.clip(f_bulge, 0.0, 1.0))

    return M_DM_total, f_gas, f_bulge


# ================== МОДЕЛЬ УДЕРЖАНИЯ ==================

def retention_model_packed(vars_tuple, C, p, alpha, beta):
    """
    eps_th = C * (M_bar / M0_SCALE)^p * f_gas^alpha * (1 - f_bulge)^beta
    vars_tuple = (M_bar, f_gas, f_bulge)
    """
    M_bar, f_gas, f_bulge = vars_tuple
    f_gas = np.clip(f_gas, 1e-3, 1.0)
    f_bulge = np.clip(f_bulge, 0.0, 0.999)

    return (C *
            (M_bar / M0_SCALE)**p *
            (f_gas**alpha) *
            ((1.0 - f_bulge)**beta)
           )


# ================== ОСНОВНОЙ АНАЛИЗ ==================

def run_dm_mass_analysis():
    tab = load_table1(TABLE1_FILE)

    M_bar_list = []
    V_flat_list = []
    M_DM_list = []
    f_gas_list = []
    f_bulge_list = []
    names = []

    for _, row in tab.iterrows():
        gal = row["Galaxy"].strip()
        L36 = row["L36"]
        MHI = row["MHI"]
        Vflat = row["Vflat"]

        if not (np.isfinite(L36) and np.isfinite(MHI) and np.isfinite(Vflat)):
            continue
        if Vflat <= 0:
            continue

        # глобальная барионная масса
        M_star = ML_DISK * L36 * 1e9
        M_gas = 1.33 * MHI * 1e9
        M_bar = M_star + M_gas
        if M_bar <= 0:
            continue

        M_DM, f_gas, f_bulge = analyze_rotmod_dm_mass(gal)
        if M_DM is None:
            continue

        M_bar_list.append(M_bar)
        V_flat_list.append(Vflat)
        M_DM_list.append(M_DM)
        f_gas_list.append(f_gas)
        f_bulge_list.append(f_bulge)
        names.append(gal)

    M_bar = np.array(M_bar_list)
    V_flat = np.array(V_flat_list)
    M_DM = np.array(M_DM_list)
    f_gas = np.array(f_gas_list)
    f_bulge = np.array(f_bulge_list)

    print(f"Галактик с валидной M_DM: {len(M_bar)}")

    # --- BTFR raw (контроль) ---
    logV = np.log10(V_flat)
    logM = np.log10(M_bar)
    b_raw, a_raw = np.polyfit(logV, logM, 1)
    print(f"RAW BTFR slope (log M vs log V) = {b_raw:.2f}")

    # --- eps_data = M_DM / M_bar ---
    eps_data = M_DM / M_bar
    print(f"eps_data (M_DM/M_bar) median = {np.median(eps_data):.2f}, "
          f"min = {eps_data.min():.2f}, max = {eps_data.max():.2f}")

    # --- фит модели удержания ---
    mask_pos = eps_data > 0
    M_bar_fit = M_bar[mask_pos]
    f_gas_fit = f_gas[mask_pos]
    f_bulge_fit = f_bulge[mask_pos]
    eps_fit = eps_data[mask_pos]

    # начальные параметры: C~1, p~0, alpha~1, beta~1
    p0 = [1.0, 0.0, 1.0, 1.0]
    bounds = (
        [0.01, -1.0, 0.0, 0.0],
        [50.0,  1.0, 3.0,  3.0]
    )

    popt, pcov = curve_fit(
        retention_model_packed,
        (M_bar_fit, f_gas_fit, f_bulge_fit),
        eps_fit,
        p0=p0,
        bounds=bounds,
        maxfev=20000
    )

    C_fit, p_fit, alpha_fit, beta_fit = popt
    print("Fitted retention parameters (from global M_DM/M_bar):")
    print(f"  C     = {C_fit:.3f}")
    print(f"  p     = {p_fit:.3f}")
    print(f"  alpha = {alpha_fit:.3f}")
    print(f"  beta  = {beta_fit:.3f}")

    eps_th = retention_model_packed((M_bar, f_gas, f_bulge), *popt)

    # ================== ГРАФИКИ ==================

    # 1) BTFR raw
    plt.figure(figsize=(7, 6))
    sc1 = plt.scatter(M_bar, V_flat, c=eps_data, cmap="plasma",
                      s=40, edgecolors="k", alpha=0.8)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$M_{\rm bar}\ [M_\odot]$")
    plt.ylabel(r"$V_{\rm flat}\ [{\rm km/s}]$")
    plt.title(f"BTFR raw (контроль), slope ≈ {b_raw:.2f}")
    plt.grid(True, which="both", alpha=0.2)
    cbar = plt.colorbar(sc1)
    cbar.set_label(r"Глобальное отношение $M_{\rm DM}/M_{\rm bar}$")
    plt.tight_layout()
    plt.show()

    # 2) eps_data vs eps_th
    plt.figure(figsize=(6, 6))
    sc2 = plt.scatter(eps_th[mask_pos], eps_fit,
                      c=f_bulge[mask_pos], cmap="magma_r",
                      s=40, edgecolors="k", alpha=0.8)
    lim_min = min(eps_th[mask_pos].min(), eps_fit.min()) * 0.7
    lim_max = max(eps_th[mask_pos].max(), eps_fit.max()) * 1.3
    plt.plot([lim_min, lim_max], [lim_min, lim_max],
             "r--", label="eps_data = eps_th")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$\varepsilon_{\rm th}(M_{\rm bar}, f_{\rm gas}, f_{\rm bulge})$")
    plt.ylabel(r"$\varepsilon_{\rm data} = M_{\rm DM}/M_{\rm bar}$")
    plt.title("Проверка модели удержания (глобальная M_DM/M_bar)")
    cbar2 = plt.colorbar(sc2)
    cbar2.set_label(r"Доля балджа $f_{\rm bulge}$")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 3) eps_data против отдельных параметров
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    axes[0].scatter(f_gas, eps_data, c=f_bulge, cmap="magma_r",
                    s=35, edgecolors="k", alpha=0.8)
    axes[0].set_xlabel(r"$f_{\rm gas}$")
    axes[0].set_ylabel(r"$M_{\rm DM}/M_{\rm bar}$")
    axes[0].set_title("DM/Baryons vs gas fraction")
    axes[0].set_yscale("log")
    axes[0].grid(True, alpha=0.3)

    axes[1].scatter(f_bulge, eps_data, c=f_gas, cmap="viridis",
                    s=35, edgecolors="k", alpha=0.8)
    axes[1].set_xlabel(r"$f_{\rm bulge}$")
    axes[1].set_title("DM/Baryons vs bulge fraction")
    axes[1].set_yscale("log")
    axes[1].grid(True, alpha=0.3)

    axes[2].scatter(M_bar, eps_data, c=f_gas, cmap="viridis",
                    s=35, edgecolors="k", alpha=0.8)
    axes[2].set_xscale("log")
    axes[2].set_yscale("log")
    axes[2].set_xlabel(r"$M_{\rm bar}\ [M_\odot]$")
    axes[2].set_title("DM/Baryons vs baryonic mass")
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_dm_mass_analysis()
