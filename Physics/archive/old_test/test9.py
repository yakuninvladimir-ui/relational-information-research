import os
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================== НАСТРОЙКИ ==================

TABLE1_FILE   = "table1.mrt"
ROTMOD_FOLDER = "rotmod"   # путь к *_rotmod.dat
DENS_FOLDER   = "dens"   # путь к *.dens (поправь при необходимости)

ML_DISK  = 0.5
ML_BULGE = 0.7

# ================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==================

def load_table1(path=TABLE1_FILE):
    """Чтение table1.mrt (как раньше)."""
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
    for c in candidates:
        if os.path.exists(c):
            cols = ['Rad', 'Vobs', 'errV', 'Vgas', 'Vdisk', 'Vbul', 'SBdisk', 'SBbul']
            df = pd.read_csv(c, sep=r"\s+", comment="#", names=cols)
            return df if len(df) >= 3 else None
    return None


def load_dens(gal_name):
    base = gal_name.strip()
    candidates = [
        os.path.join(DENS_FOLDER, f"{base}.dens"),
        os.path.join(DENS_FOLDER, f"{base.replace(' ','')}.dens"),
        f"{base}.dens",
        f"{base.replace(' ','')}.dens",
    ]
    for c in candidates:
        if os.path.exists(c):
            df = pd.read_csv(c, sep=r"\s+", comment="#", header=None,
                             names=["Rad_kpc", "SBdisk", "SBbulge"])
            return df if len(df) >= 3 else None
    return None


def find_R_flat(rot, Vflat, frac=0.9):
    """
    Ищем радиус, где Vobs достигает frac * Vflat (берём самый внешний такой радиус).
    Если не находим, возвращаем None.
    """
    R = rot["Rad"].values  # kpc
    Vobs = np.abs(rot["Vobs"].values)
    mask = np.isfinite(R) & np.isfinite(Vobs) & (Vobs > 0)
    if np.count_nonzero(mask) < 3:
        return None

    R = R[mask]
    Vobs = Vobs[mask]

    thr = frac * Vflat
    ok = Vobs >= thr
    if np.count_nonzero(ok) == 0:
        return None

    # берём самый большой радиус, где уже достигли плато
    R_flat = R[ok].max()
    return float(R_flat)


# ================== СБОР ДАННЫХ ДЛЯ BTFR+Σ_* ==================

def collect_BTFR_sigma_star():
    tab = load_table1()

    M_bar_list = []
    V_flat_list = []
    Sigma_star_flat_list = []
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

        rot = load_rotmod(gal)
        dens = load_dens(gal)
        if rot is None or dens is None:
            continue

        # барионная масса (как раньше)
        M_star = ML_DISK * L36 * 1e9
        M_gas  = 1.33 * MHI * 1e9
        M_bar  = M_star + M_gas
        if M_bar <= 0:
            continue

        # радиус плато
        R_flat = find_R_flat(rot, Vflat, frac=0.9)
        if R_flat is None:
            continue

        # Σ_* из dens в этом радиусе
        R_star = dens["Rad_kpc"].values
        SBdisk = dens["SBdisk"].values
        SBbul  = dens["SBbulge"].values
        sigma_star_prof = SBdisk + SBbul  # Lsun/pc^2

        if np.all(~np.isfinite(sigma_star_prof)):
            continue

        Sigma_star_flat = np.interp(
            R_flat, R_star, sigma_star_prof,
            left=np.nan, right=np.nan
        )
        if not np.isfinite(Sigma_star_flat) or Sigma_star_flat <= 0:
            continue

        M_bar_list.append(M_bar)
        V_flat_list.append(Vflat)
        Sigma_star_flat_list.append(Sigma_star_flat)
        names.append(gal)

    if not M_bar_list:
        raise RuntimeError("Нет ни одной галактики с валидными BTFR+Sigma_* данными.")

    M_bar_arr = np.array(M_bar_list)
    V_flat_arr = np.array(V_flat_list)
    Sigma_star_flat_arr = np.array(Sigma_star_flat_list)

    return M_bar_arr, V_flat_arr, Sigma_star_flat_arr, names


# ================== ОСНОВНОЙ АНАЛИЗ ==================

def run_BTFR_sigma_star():
    M_bar, V_flat, Sigma_star_flat, names = collect_BTFR_sigma_star()
    print(f"Галактик с валидными данными: {len(M_bar)}")

    # логарифмы
    logM = np.log10(M_bar)
    logV = np.log10(V_flat)
    logSigma = np.log10(Sigma_star_flat)

    # ---------- 1. Обычный BTFR: logM = a + b logV ----------
    b1, a1 = np.polyfit(logV, logM, 1)
    logM_pred1 = a1 + b1 * logV
    residuals1 = logM - logM_pred1
    SS_tot = np.sum((logM - np.mean(logM))**2)
    SS_res1 = np.sum(residuals1**2)
    R2_1 = 1.0 - SS_res1 / SS_tot

    print("BTFR (1D): log M = a + b log V")
    print(f"  a = {a1:.3f}, b = {b1:.3f}, R^2 = {R2_1:.3f}")

    # ---------- 2. Расширенный BTFR: logM = a + b logV + c logSigma ----------
    # Собираем матрицу X = [1, logV, logSigma]
    X = np.vstack([np.ones_like(logV), logV, logSigma]).T
    # Решаем по МНК
    coeffs, *_ = np.linalg.lstsq(X, logM, rcond=None)
    a2, b2, c2 = coeffs
    logM_pred2 = a2 + b2 * logV + c2 * logSigma
    residuals2 = logM - logM_pred2
    SS_res2 = np.sum(residuals2**2)
    R2_2 = 1.0 - SS_res2 / SS_tot

    print("BTFR (2D plane): log M = a + b log V + c log Sigma_star_flat")
    print(f"  a = {a2:.3f}, b = {b2:.3f}, c = {c2:.3f}, R^2 = {R2_2:.3f}")
    print(f"  Улучшение R^2: ΔR^2 = {R2_2 - R2_1:.3f}")

    # ---------- 3. BTFR с цветом по Σ_* ----------
    plt.figure(figsize=(7, 6))
    sc = plt.scatter(M_bar, V_flat, c=logSigma, cmap="plasma",
                     s=45, edgecolors="k", alpha=0.85)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$M_{\rm bar}\ [M_\odot]$")
    plt.ylabel(r"$V_{\rm flat}\ [{\rm km/s}]$")
    plt.title(f"BTFR с цветом по log Σ_* (R_flat)\n1D slope={b1:.2f}, 2D slope={b2:.2f}, c={c2:.2f}")
    plt.grid(True, which="both", alpha=0.3)
    cbar = plt.colorbar(sc)
    cbar.set_label(r"log$_{10}\,\Sigma_{\star,\rm flat}$ (L$_\odot$/pc$^2$)")

    # линия обычного BTFR (для наглядности)
    V_grid = np.logspace(np.log10(V_flat.min()*0.8),
                         np.log10(V_flat.max()*1.2), 100)
    logV_grid = np.log10(V_grid)
    logM_BTFR = a1 + b1 * logV_grid
    M_BTFR = 10**logM_BTFR
    plt.plot(M_BTFR, V_grid, "r--", label=f"BTFR 1D: b={b1:.2f}")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # ---------- 4. BTFR по тертилям Σ_* ----------
    # делим выборку на 3 группы по Σ_*_flat
    q1, q2 = np.percentile(Sigma_star_flat, [33, 66])
    groups = [
        ("низкая Σ_*", Sigma_star_flat <= q1),
        ("средняя Σ_*", (Sigma_star_flat > q1) & (Sigma_star_flat <= q2)),
        ("высокая Σ_*", Sigma_star_flat > q2)
    ]

    plt.figure(figsize=(8, 6))
    colors = ["tab:blue", "tab:orange", "tab:green"]
    for (label, mask), col in zip(groups, colors):
        if np.count_nonzero(mask) < 5:
            continue
        logM_g = logM[mask]
        logV_g = logV[mask]
        b_g, a_g = np.polyfit(logV_g, logM_g, 1)
        plt.scatter(10**logM_g, 10**logV_g, s=35, edgecolors="k",
                    alpha=0.75, color=col, label=f"{label}, b={b_g:.2f}")
        # линия для каждой группы
        Vg_grid = np.logspace(np.log10(10**logV_g.min()*0.9),
                              np.log10(10**logV_g.max()*1.1), 50)
        logVg_grid = np.log10(Vg_grid)
        logMg_BTFR = a_g + b_g * logVg_grid
        Mg_BTFR = 10**logMg_BTFR
        plt.plot(Mg_BTFR, Vg_grid, color=col, lw=2)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$M_{\rm bar}\ [M_\odot]$")
    plt.ylabel(r"$V_{\rm flat}\ [{\rm km/s}]$")
    plt.title("BTFR в тертилях по Σ_* (R_flat)")
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_BTFR_sigma_star()
