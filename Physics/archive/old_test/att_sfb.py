import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm  # <--- Исправленный импорт
import os
import seaborn as sns

# ==========================================
# НАСТРОЙКИ
# ==========================================
PATH_ROTMOD = 'rotmod/'
PATH_SFB = 'sfb/'
PATH_TABLE = 'table1.mrt'

# Коэффициенты M/L
UPSILON_DISK = 0.5
UPSILON_BULGE = 0.7

def load_sparc_table(filepath):
    """
    Парсинг table1.mrt используя гибкое разделение по пробелам (split),
    чтобы избежать ошибок смещения колонок.
    """
    names = []
    lums = []   # Total Luminosity
    sbeff = []  # Effective Surface Brightness
    reff = []   # Effective Radius
    
    try:
        with open(filepath, 'r') as f:
            for line in f:
                # Пропускаем комментарии и пустые строки
                if line.strip().startswith('Byte') or line.strip().startswith('#') or line.strip().startswith('-') or not line.strip():
                    continue
                if line.strip().startswith('Galaxy') or line.strip().startswith('Title') or line.strip().startswith('Authors'):
                    continue
                
                parts = line.split()
                
                # Проверка: строка данных должна быть длинной (минимум 11 колонок)
                if len(parts) < 11: 
                    continue
                
                # UGC00119 (0) 8 (1) 15.50 (2) ... 2.636 (7=L) ... 3.57 (9=Reff) 206.52 (10=SBeff)
                try:
                    # Проверяем, что первый элемент похож на имя галактики (не число)
                    if parts[0][0].isdigit(): continue 

                    name = parts[0].strip()
                    l_val = float(parts[7])      # Luminosity (10^9 sol)
                    reff_val = float(parts[9])   # Reff (kpc)
                    sb_val = float(parts[10])    # Surface Brightness (sol/pc^2)
                    
                    names.append(name)
                    lums.append(l_val * 1e9)     # Переводим в абсолютные единицы
                    reff.append(reff_val)
                    sbeff.append(sb_val)
                except ValueError:
                    continue
                    
        print(f"   Успешно загружено {len(names)} записей из table1.")
        return pd.DataFrame({'Galaxy': names, 'L_total': lums, 'Reff': reff, 'SBeff': sbeff})
        
    except Exception as e:
        print(f"Критическая ошибка чтения таблицы {filepath}: {e}")
        return pd.DataFrame()

def calculate_mu_and_sb(rotmod_path, ups_disk=0.5, ups_bulge=0.7):
    """
    Считает локальные значения Mu и яркости.
    """
    try:
        data = np.genfromtxt(rotmod_path)
        # 0:Rad, 1:Vobs, 2:err, 3:Vgas, 4:Vdisk, 5:Vbul, 6:SBdisk, 7:SBbul
        r = data[:, 0]
        v_obs = data[:, 1]
        v_gas = np.abs(data[:, 3])
        v_disk = np.abs(data[:, 4])
        v_bulge = np.abs(data[:, 5])
        sb_disk = data[:, 6]
        sb_bul = data[:, 7]
        
        sb_total = sb_disk + sb_bul
        
        # Барионная скорость
        v_bar_sq = v_gas**2 + ups_disk * v_disk**2 + ups_bulge * v_bulge**2
        
        # Mu = 1 - (Vbar / Vobs)^2
        # Защита от деления на ноль
        with np.errstate(divide='ignore', invalid='ignore'):
            mu_local = 1.0 - (v_bar_sq / v_obs**2)
        
        # Фильтрация: R > 0, Vobs > 10, Mu не бесконечность
        mask = (r > 0.5) & (v_obs > 20) & (sb_total > 0) & np.isfinite(mu_local)
        
        return r[mask], mu_local[mask], sb_total[mask]
        
    except Exception as e:
        return None, None, None

# ==========================================
# ЗАПУСК
# ==========================================

print("1. Загрузка глобальных параметров...")
df_global = load_sparc_table(PATH_TABLE)

all_mu_points = []
all_sb_points = [] 

galaxy_mean_mu = []
galaxy_luminosity = []
galaxy_sbeff = [] # Для цвета точек

print("2. Обработка профилей вращения...")

count_processed = 0
for index, row in df_global.iterrows():
    gal_name = row['Galaxy']
    file_path = os.path.join(PATH_ROTMOD, f"{gal_name}_rotmod.dat")
    
    if os.path.exists(file_path):
        r, mu, sb = calculate_mu_and_sb(file_path, UPSILON_DISK, UPSILON_BULGE)
        
        if r is not None and len(r) > 5:
            # 1. Сбор данных для HEATMAP (Локальная физика)
            # Ограничиваем Mu разумными рамками (шум измерений может давать mu=-5 или mu=5)
            # Нас интересует переход от 0 до 1.
            valid_idx = (mu > -0.5) & (mu < 1.2)
            
            all_mu_points.extend(mu[valid_idx])
            all_sb_points.extend(sb[valid_idx])
            
            # 2. Сбор данных для SCATTER (Глобальная физика)
            # Берем среднее Mu по внешним частям, где аттрактор должен работать чисто
            # Если галактика маленькая, берем все точки
            if np.max(r) > 2 * row['Reff']:
                outer_mask = (r > 2.0 * row['Reff'])
                mean_mu_gal = np.mean(mu[outer_mask])
            else:
                mean_mu_gal = np.mean(mu)
                
            galaxy_mean_mu.append(mean_mu_gal)
            galaxy_luminosity.append(row['L_total'])
            galaxy_sbeff.append(row['SBeff'])
            count_processed += 1

print(f"   Обработано {count_processed} галактик с данными.")
            
# Преобразуем в массивы
all_mu_points = np.array(all_mu_points)
all_sb_points = np.array(all_sb_points)

# ==========================================
# ГРАФИКИ
# ==========================================
plt.style.use('dark_background') 
fig = plt.figure(figsize=(16, 7))

# --- ГРАФИК 1: Глобальная связь (Светимость vs Вакуум) ---
ax1 = fig.add_subplot(121)

# Фильтруем данные для scatter (убираем nan)
mask_glob = np.isfinite(galaxy_luminosity) & np.isfinite(galaxy_mean_mu)
g_lum = np.array(galaxy_luminosity)[mask_glob]
g_mu = np.array(galaxy_mean_mu)[mask_glob]
g_sb = np.array(galaxy_sbeff)[mask_glob]

# scatter c LogNorm для цвета
sc1 = ax1.scatter(g_lum, g_mu, c=g_sb, 
                  cmap='plasma', s=80, edgecolors='w', alpha=0.9, 
                  norm=LogNorm()) # <--- Используем правильный LogNorm

ax1.set_xscale('log')
ax1.set_xlabel(r'Total Luminosity ($L_{\odot}$)', fontsize=12)
ax1.set_ylabel(r'Avg Attractor Strength ($\langle \mu \rangle$)', fontsize=12)
ax1.set_title('Global: Thermodynamics vs Vacuum', fontsize=14)
ax1.grid(True, alpha=0.2)
ax1.axhline(0, color='w', linestyle='--', alpha=0.5, label='Newton (0)')
ax1.axhline(1, color='cyan', linestyle='--', alpha=0.5, label='Attractor (1)')

cbar1 = plt.colorbar(sc1, ax=ax1)
cbar1.set_label(r'Effective Surface Brightness ($L_{\odot}/pc^2$)')

# --- ГРАФИК 2: Локальная фазовая диаграмма ---
ax2 = fig.add_subplot(122)

# Hexbin для тысяч точек - ИСПРАВЛЕНО: xscale='log' вместо xscale('log')
hb = ax2.hexbin(all_sb_points, all_mu_points, gridsize=40, 
                cmap='inferno', bins='log', mincnt=1, xscale='log')

# Тренд (Mean)
try:
    # Делим ось X (яркость) на бины
    bins = np.logspace(np.log10(max(min(all_sb_points), 1e-3)), np.log10(max(all_sb_points)), 20)
    # Считаем среднее Mu в каждом бине яркости
    digitized = np.digitize(all_sb_points, bins)
    means = []
    centers = []
    for i in range(1, len(bins)):
        vals = all_mu_points[digitized == i]
        if len(vals) > 5: # Берем бин только если там есть точки
            means.append(vals.mean())
            centers.append((bins[i-1] + bins[i])/2)
            
    ax2.plot(centers, means, 'cyan', linewidth=4, marker='o', label='Mean Trend')
except Exception as e:
    print(f"Ошибка построения тренда: {e}")

ax2.set_xscale('log')
ax2.set_xlabel(r'Local Surface Brightness ($L_{\odot}/pc^2$)', fontsize=12)
ax2.set_ylabel(r'Local Attractor Strength ($\mu$)', fontsize=12)
ax2.set_title('Local: Phase Transition', fontsize=14)
ax2.set_ylim(-0.5, 1.5)
ax2.set_xlim(left=0.01) # Чтобы не уезжать в -бесконечность логарифма
ax2.axhline(0, color='w', linestyle='--', alpha=0.5)
ax2.axhline(1, color='cyan', linestyle='--', alpha=0.5)
ax2.grid(True, alpha=0.2)
ax2.legend()

cb2 = plt.colorbar(hb, ax=ax2)
cb2.set_label('Point Density (Log)')

plt.tight_layout()
filename = 'thermo_correlation_v2.png'
plt.savefig(filename, dpi=150)
print(f"График сохранен как {filename}")
plt.show()