import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from scipy.stats import linregress

# Папка с rotmod-файлами SPARC
DATA_FOLDER = "rotmod"

# Константы
A0 = 1.2e-10          # фундаментальное ускорение (м/с^2)
G_kpc = 4.301e-6      # гравитационная, (km/s)^2 * kpc / Msun

# Массо-световые отношения (можно потом калибровать)
ML_DISK  = 0.5
ML_BULGE = 0.7


def get_galaxy_properties(file_path):
    """
    Считывает rotmod-файл и возвращает основные параметры галактики:
    M_bar, V_flat, M_disk, M_bul, f_disk, name.

    file_path: путь к .dat файлу.
    """
    col_names = ["Rad", "Vobs", "errV", "Vgas", "Vdisk", "Vbul",
                 "SBdisk", "SBbul"]
    df = pd.read_csv(file_path, sep=r"\s+", names=col_names, comment="#")

    # Берём только точки с положительным наблюдаемым V
    valid_v = df["Vobs"][df["Vobs"] > 0]
    if len(valid_v) < 3:
        return None

    # Плоская скорость — средняя по последним 3 точкам
    V_flat = np.mean(valid_v.iloc[-3:])

    # Последняя точка по радиусу
    last_row = df.iloc[-1]
    R_last_kpc = last_row["Rad"]  # в kpc

    # Компоненты скоростей в последней точке
    V_gas_last  = abs(last_row["Vgas"])
    V_disk_last = abs(last_row["Vdisk"])
    V_bul_last  = abs(last_row["Vbul"])

    # Массы по простому динамическому оцениванию M ~ V^2 R / G
    M_gas  = (V_gas_last**2  * R_last_kpc) / G_kpc
    M_disk = (V_disk_last**2 * R_last_kpc) / G_kpc * ML_DISK
    M_bul  = (V_bul_last**2  * R_last_kpc) / G_kpc * ML_BULGE

    M_bar = M_gas + M_disk + M_bul

    # Доля диска в звёздной массе — наш "температурный" прокси
    M_star = M_disk + M_bul
    if M_star > 0:
        f_disk = M_disk / M_star
    else:
        f_disk = np.nan

    return {
        "M_bar":  M_bar,
        "V_flat": V_flat,
        "M_disk": M_disk,
        "M_bul":  M_bul,
        "f_disk": f_disk,
        "name":   os.path.basename(file_path).replace(".dat", "")
    }


def plot_btfr_with_retention(gamma=1.0):
    """
    Строит BTFR с учётом retention-фактора:
      R_gal = (f_ref / f_disk)^gamma
      M_eff = R_gal * M_bar

    gamma: степень зависимости от f_disk.
    """
    files = glob.glob(os.path.join(DATA_FOLDER, "*.dat"))
    print(f"Обработка {len(files)} галактик...")

    records = []
    for f in files:
        props = get_galaxy_properties(f)
        if props is None:
            continue

        # Фильтрация совсем "карликовых" и странных случаев
        if props["M_bar"] <= 1e6 or props["V_flat"] <= 10:
            continue
        if not np.isfinite(props["f_disk"]):
            continue

        records.append(props)

    if not records:
        print("Нет пригодных галактик для анализа.")
        return

    # Вытаскиваем массивы
    M_bar  = np.array([r["M_bar"]   for r in records])
    V_flat = np.array([r["V_flat"]  for r in records])
    f_disk = np.array([r["f_disk"]  for r in records])

    # Опорное значение f_ref — медиана по выборке
    f_ref = np.nanmedian(f_disk)

    # --- ВАЖНО: инвертированный retention-фактор ---
    # Bulge-dominated (малое f_disk) → больший M_eff
    # Disk-dominated → M_eff ближе к M_bar.
    with np.errstate(divide="ignore", invalid="ignore"):
        R_gal = (f_ref / f_disk)**gamma

    # На всякий случай обрежем дикие значения (если f_disk сильно < f_ref)
    R_gal = np.clip(R_gal, 0.1, 10.0)

    M_eff = R_gal * M_bar

    # Линейная регрессия в логарифмах:
    # log10(V) = slope * log10(M_eff) + intercept
    slope, intercept, r_value, p_value, std_err = linregress(
        np.log10(M_eff), np.log10(V_flat)
    )

    print(f"BTFR: log V = {slope:.3f} log M_eff + {intercept:.3f}")
    print(f"Число галактик: {len(M_eff)}")
    print(f"R^2 регрессии: {r_value**2:.3f}")

    # Правильная эквивалентная степень n в законе V^4 ~ M^n
    n_equiv = 4.0 * slope
    print(f"Эквивалент закона V^4 ~ M^n: n = {n_equiv:.2f}")

    # --- График BTFR ---
    plt.figure(figsize=(10, 8))
    sc = plt.scatter(
        M_eff, V_flat,
        c=f_disk,
        cmap="plasma",
        alpha=0.8,
        edgecolors="k",
        linewidths=0.4,
        label="SPARC (скорректировано)"
    )

    # Теоретическая линия V^4 = G a0 M_eff
    m_range = np.logspace(7, 12, 100)  # Msun
    G_si = 6.674e-11
    M_sun_kg = 1.989e30

    v_theory_ms  = (G_si * (m_range * M_sun_kg) * A0)**0.25
    v_theory_kms = v_theory_ms / 1000.0

    plt.plot(
        m_range, v_theory_kms,
        "r-",
        lw=3,
        label="V^4 = G a0 M_eff"
    )

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$M_{\rm eff}$ [$M_\odot$]")
    plt.ylabel(r"$V_{\rm flat}$ [km/s]")
    plt.title(f"BTFR с retention-фактором, gamma={gamma}")

    cbar = plt.colorbar(sc)
    cbar.set_label("f_disk (доля диска во звёздной массе)")

    plt.grid(True, which="both", alpha=0.2)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # <<< ЗДЕСЬ МЕНЯЕШЬ GAMMA >>>
    GAMMA = 1.0  # например: 0.5, 1.0, 1.5 ...
    plot_btfr_with_retention(gamma=GAMMA)
