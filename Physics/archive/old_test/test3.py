# test3_v2.py
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

# MOND-параметр a0 (можно откалибровать по test10)
A0_CONST = 1.2e-10  # м/с^2, примерное значение


# ================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==================


def bulge_fraction_from_T(T):
    """Та же прокси-функция f_bulge(T), что и в test7_v3."""
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
    """Читаем table1.mrt."""
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


def collect_rar_points():
    """
    Собираем g_obs, g_bar, f_bulge по всем галактикам.
    .dens не нужен, так как здесь мы используем только rotmod.
    """
    tab = load_table1(TABLE1_FILE)

    all_g_obs = []
    all_g_bar = []
    all_f_bulge = []

    for _, row in tab.iterrows():
        gal = row["Galaxy"].strip()
        T = row["T"]
        f_bulge_global = bulge_fraction_from_T(T)

        rot = load_rotmod(gal)
        if rot is None:
            continue

        R_kpc = rot["Rad"].values
        R_m = R_kpc * 3.086e19
        vfac = 1000.0

        V_obs = np.abs(rot["Vobs"].values) * vfac
        V_gas = np.abs(rot["Vgas"].values) * vfac
        V_disk = np.abs(rot["Vdisk"].values) * vfac
        V_bul = np.abs(rot["Vbul"].values) * vfac

        V_bar_sq = (
            V_gas**2 +
            (V_disk**2) * ML_DISK +
            (V_bul**2) * ML_BULGE
        )
        V_obs_sq = V_obs**2

        g_obs = V_obs_sq / R_m
        g_bar = V_bar_sq / R_m

        valid = (
            np.isfinite(g_obs) & np.isfinite(g_bar) &
            (g_obs > 0) & (g_bar > 0)
        )
        if np.count_nonzero(valid) < 5:
            continue

        all_g_obs.append(g_obs[valid])
        all_g_bar.append(g_bar[valid])
        all_f_bulge.append(
            np.full(np.count_nonzero(valid), f_bulge_global)
        )

    if not all_g_obs:
        raise RuntimeError("Не удалось собрать радиальные точки RAR.")

    g_obs = np.concatenate(all_g_obs)
    g_bar = np.concatenate(all_g_bar)
    f_bulge = np.concatenate(all_f_bulge)
    return g_obs, g_bar, f_bulge


# ================== ОСНОВНОЙ АНАЛИЗ ==================


def mond_model(g_bar, a0=A0_CONST):
    """
    Простая MOND-формула:
    g_obs = g_bar / (1 - exp(-sqrt(g_bar/a0))).
    """
    x = np.sqrt(g_bar / a0)
    with np.errstate(over="ignore", invalid="ignore"):
        denom = 1.0 - np.exp(-x)
    # защищаемся от нулевого знаменателя
    denom[denom <= 0] = np.nan
    return g_bar / denom


def running_median(x, y, nbins=20):
    """Медианная кривая для визуализации тренда."""
    x = np.asarray(x)
    y = np.asarray(y)
    order = np.argsort(x)
    x = x[order]
    y = y[order]

    bins = np.logspace(np.log10(x.min()), np.log10(x.max()), nbins + 1)
    x_mid = []
    y_med = []

    for i in range(nbins):
        mask = (x >= bins[i]) & (x < bins[i+1])
        if np.count_nonzero(mask) < 10:
            continue
        x_mid.append(np.median(x[mask]))
        y_med.append(np.median(y[mask]))

    return np.array(x_mid), np.array(y_med)


def run_test3():
    g_obs, g_bar, f_bulge = collect_rar_points()
    print(f"Всего радиальных точек: {len(g_obs)}")

    g_model = mond_model(g_bar, A0_CONST)
    ratio = g_obs / g_model

    mask = np.isfinite(g_model) & np.isfinite(ratio) & (ratio > 0)
    g_obs = g_obs[mask]
    g_bar = g_bar[mask]
    f_bulge = f_bulge[mask]
    ratio = ratio[mask]

    print(f"После фильтра: {len(g_bar)} точек")

    log_gbar = np.log10(g_bar)
    # отклонение: g_obs/g_model
    dev = ratio

    # --- Основной scatter с цветом по f_bulge ---
    plt.figure(figsize=(11, 7))
    sc = plt.scatter(
        g_bar, dev,
        c=f_bulge,
        s=8,
        cmap="magma",
        alpha=0.4
    )
    plt.xscale("log")
    plt.axhline(1.0, color="k", linestyle="--", label="Точное совпадение с моделью")
    cbar = plt.colorbar(sc)
    cbar.set_label(r"Доля балджа (f$_{\rm bulge}$, прокси по T)")

    plt.xlabel(r"$g_{\rm bar}$ [м/с$^2$]")
    plt.ylabel(r"Отклонение $(g_{\rm obs}/g_{\rm model})$")
    plt.title("Влияют ли балдж/ЧД на диссипацию? (Анализ остатков)")

    plt.text(
        0.9 * g_bar.min(), 1.82,
        "Выше линии: TM больше, чем надо",
        fontsize=9
    )
    plt.text(
        0.9 * g_bar.min(), 0.58,
        "Ниже линии: TM меньше, чем надо (эффект балджа/ЧД?)",
        fontsize=9
    )

    plt.grid(True, which="both", alpha=0.2)

    # --- Кривые для разных f_bulge (квантили) ---
    quantiles = np.quantile(f_bulge, [0.2, 0.4, 0.6, 0.8])
    bins_fb = [
        (0.0, quantiles[0]),
        (quantiles[0], quantiles[1]),
        (quantiles[1], quantiles[2]),
        (quantiles[2], quantiles[3]),
        (quantiles[3], 1.0)
    ]
    colors_curves = ["gold", "orange", "magenta", "purple", "black"]
    labels_curves = []

    for (fb_min, fb_max), col in zip(bins_fb, colors_curves):
        mask_fb = (f_bulge >= fb_min) & (f_bulge < fb_max)
        if np.count_nonzero(mask_fb) < 50:
            continue
        x_med, y_med = running_median(g_bar[mask_fb], dev[mask_fb], nbins=18)
        plt.plot(
            x_med, y_med,
            color=col,
            linewidth=2
        )
        labels_curves.append(
            f"{fb_min:.2f} ≤ f_bulge < {fb_max:.2f}"
        )

    # условная легенда
    plt.legend(
        [plt.Line2D([0], [0], color=c, lw=2) for c in colors_curves[:len(labels_curves)]]
        + [plt.Line2D([0], [0], color="k", lw=1, ls="--")],
        labels_curves + ["Точное совпадение с моделью"],
        fontsize=8,
        loc="upper right"
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_test3()
