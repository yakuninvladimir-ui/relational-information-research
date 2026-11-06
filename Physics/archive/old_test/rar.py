import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
from scipy.stats import binned_statistic

# ===============================
# Константы
# ===============================
KPC_TO_M = 3.0856776e19
KM_TO_M = 1e3

# ===============================
# Загрузка rotmod
# ===============================
def load_rotmod(path):
    df = pd.read_csv(
        path,
        sep=r"\s+",
        comment="#",
        header=None,
        names=[
            "r_kpc",
            "v_obs",
            "errV",
            "v_gas",
            "v_disk",
            "v_bul",
            "sb_disk",
            "sb_bul",
        ],
    )
    df = df[(df["r_kpc"] > 0) & (df["v_obs"] > 0)]
    return df


# ===============================
# Ускорения
# ===============================
def compute_g(r_kpc, v_kms):
    r = r_kpc * KPC_TO_M
    v = v_kms * KM_TO_M
    return v**2 / r


# ===============================
# Средняя эмпирическая RAR
# (McGaugh 2016 — только как reference)
# ===============================
def g_rar_mean(g_bar):
    g0 = 1.2e-10
    return g_bar / (1 - np.exp(-np.sqrt(g_bar / g0)))


# ===============================
# Основной анализ
# ===============================
def analyze_rar_by_mu(
    rotmod_dir="rotmod",
    mu_table_path="sparc_mu_table.csv",
):
    mu_table = pd.read_csv(mu_table_path)
    mu_dict = dict(zip(mu_table.galaxy, mu_table.mu))

    rar_points = []

    files = sorted(glob.glob(os.path.join(rotmod_dir, "*_rotmod.dat")))

    for path in files:
        gal = os.path.basename(path).replace("_rotmod.dat", "")
        if gal not in mu_dict:
            continue

        mu = mu_dict[gal]
        df = load_rotmod(path)

        v_bar = np.sqrt(
            df.v_gas.values**2 +
            df.v_disk.values**2 +
            df.v_bul.values**2
        )

        g_bar = compute_g(df.r_kpc.values, v_bar)
        g_obs = compute_g(df.r_kpc.values, df.v_obs.values)

        for gb, go in zip(g_bar, g_obs):
            if gb > 0 and go > 0:
                rar_points.append({
                    "galaxy": gal,
                    "mu": mu,
                    "g_bar": gb,
                    "g_obs": go
                })

    return pd.DataFrame(rar_points)


# ===============================
# Визуализация RAR по μ-группам
# ===============================
def plot_rar_groups(df):
    # группы μ
    bins = [
        (0.0, 0.05, "low μ"),
        (0.05, 0.2, "mid μ"),
        (0.2, 1.0, "high μ"),
    ]

    plt.figure(figsize=(7, 6))

    for lo, hi, label in bins:
        sub = df[(df.mu >= lo) & (df.mu < hi)]
        plt.scatter(
            sub.g_bar,
            sub.g_obs,
            s=8,
            alpha=0.4,
            label=f"{label} (N={len(sub)})"
        )

    g = np.logspace(-13, -9, 200)
    plt.plot(g, g_rar_mean(g), "k--", lw=2, label="Mean RAR")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$g_{\rm bar}$  [m/s$^2$]")
    plt.ylabel(r"$g_{\rm obs}$  [m/s$^2$]")
    plt.legend()
    plt.title("RAR split by coupling parameter μ")
    plt.tight_layout()
    plt.show()


# ===============================
# Остатки RAR vs μ
# ===============================
def plot_rar_residuals(df):
    g_mean = g_rar_mean(df.g_bar.values)
    delta = np.log10(df.g_obs.values) - np.log10(g_mean)

    plt.figure(figsize=(6, 4))
    plt.scatter(df.mu, delta, s=6, alpha=0.4)
    plt.axhline(0, color="k", ls="--")
    plt.xlabel("μ (coupling parameter)")
    plt.ylabel(r"$\Delta \log g$ (RAR residual)")
    plt.title("RAR residuals vs μ")
    plt.tight_layout()
    plt.show()


# ===============================
# Бинированная RAR для групп
# ===============================
def plot_binned_rar(df):
    bins_mu = [
        (0.0, 0.05, "low μ"),
        (0.05, 0.2, "mid μ"),
        (0.2, 1.0, "high μ"),
    ]

    plt.figure(figsize=(7, 6))

    for lo, hi, label in bins_mu:
        sub = df[(df.mu >= lo) & (df.mu < hi)]
        if len(sub) < 50:
            continue

        log_gb = np.log10(sub.g_bar)
        log_go = np.log10(sub.g_obs)

        stat, edges, _ = binned_statistic(
            log_gb,
            log_go,
            statistic="mean",
            bins=15
        )

        centers = 0.5 * (edges[1:] + edges[:-1])
        plt.plot(10**centers, 10**stat, "-o", label=label)

    g = np.logspace(-13, -9, 200)
    plt.plot(g, g_rar_mean(g), "k--", lw=2, label="Mean RAR")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$g_{\rm bar}$  [m/s$^2$]")
    plt.ylabel(r"$g_{\rm obs}$  [m/s$^2$]")
    plt.legend()
    plt.title("Binned RAR by μ groups")
    plt.tight_layout()
    plt.show()


# ===============================
# Запуск
# ===============================
if __name__ == "__main__":
    df_rar = analyze_rar_by_mu(
        rotmod_dir="rotmod",
        mu_table_path="sparc_mu_table.csv"
    )

    print("Total RAR points:", len(df_rar))

    plot_rar_groups(df_rar)
    plot_rar_residuals(df_rar)
    plot_binned_rar(df_rar)
