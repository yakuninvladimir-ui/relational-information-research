import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from scipy.stats import linregress

# --- НАСТРОЙКИ ---
DATA_FOLDER = 'data_rotmod'  # Та же папка, что и раньше
A0 = 1.2e-10                 # Твой параметр a0
G = 4.301e-6                 # Грав. постоянная (kpc * km^2/s^2 / M_sun) - удобные единицы

# M/L коэффициенты (как в SPARC)
ML_DISK = 0.5
ML_BULGE = 0.7

def get_galaxy_properties(file_path):
    try:
        # Читаем файл, пропуская заголовки с #
        # Имена колонок задаем жестко, так как в файле они закомментированы
        col_names = ['Rad', 'Vobs', 'errV', 'Vgas', 'Vdisk', 'Vbul', 'SBdisk', 'SBbul']
        df = pd.read_csv(file_path, sep=r'\s+', names=col_names, comment='#')
        
        # 1. Вычисляем скорость на плато (V_flat)
        # Берем среднее по последним 3 точкам (внешняя часть галактики)
        # Фильтруем плохие точки
        valid_v = df['Vobs'][df['Vobs'] > 0]
        if len(valid_v) < 3: return None
        V_flat = np.mean(valid_v.iloc[-3:])
        
        # 2. Вычисляем полную массу Барионов (M_bar)
        # V^2 = GM / R  =>  M = V^2 * R / G
        # Но SPARC дает скорости компонент (Vgas, Vdisk), которые уже V = sqrt(GM/R)
        # Значит M_component = V_component^2 * R_last / G
        # Однако, проще и точнее просуммировать светимости, если они есть, 
        # но через скорости в последней точке тоже можно оценить асимптотическую массу.
        
        last_row = df.iloc[-1]
        R_last_kpc = last_row['Rad']
        
        # Вклад газа (обычно доминирует на краях в LSB)
        V_gas_last = np.abs(last_row['Vgas'])
        M_gas = (V_gas_last**2 * R_last_kpc) / G
        
        # Вклад звезд (диск + балдж)
        V_disk_last = np.abs(last_row['Vdisk'])
        V_bul_last = np.abs(last_row['Vbul'])
        
        M_disk = (V_disk_last**2 * R_last_kpc) / G * ML_DISK
        M_bul = (V_bul_last**2 * R_last_kpc) / G * ML_BULGE
        
        M_total = M_gas + M_disk + M_bul
        
        return M_total, V_flat
        
    except Exception as e:
        return None

def plot_btfr():
    files = glob.glob(os.path.join(DATA_FOLDER, "*.dat"))
    print(f"Обработка {len(files)} галактик для BTFR...")
    
    masses = []
    velocities = []
    
    for f in files:
        props = get_galaxy_properties(f)
        if props:
            m, v = props
            if m > 1e6 and v > 10: # Фильтр мусора
                masses.append(m)
                velocities.append(v)
    
    masses = np.array(masses)
    velocities = np.array(velocities)
    
    # --- ПОСТРОЕНИЕ ГРАФИКА ---
    plt.figure(figsize=(10, 8))
    
    # 1. Данные
    plt.scatter(masses, velocities, alpha=0.6, c='blue', edgecolors='k', label='Галактики SPARC')
    
    # 2. Теоретическая линия (Наклон 4)
    # V^4 = G * a0 * M
    # log(V) = 0.25 * log(M) + const
    
    # Генерируем линию для диапазона масс
    m_range = np.logspace(7, 12, 100)
    
    # Перевод единиц для формулы V^4 = G * a0 * M
    # G в (m^3 / kg s^2) = 6.67e-11
    # a0 = 1.2e-10 m/s^2
    # M_sun в kg = 2e30
    # V будет в м/с, переведем в км/с
    
    # Проще: V_km_s = A * (M_solar)^0.25
    # Эмпирически A около 50-60 для BTFR.
    # Посчитаем точное предсказание твоей теории:
    # V = (G_newton * M_kg * a0_si)^(1/4)
    
    G_si = 6.674e-11
    M_sun_kg = 1.989e30
    v_theory_ms = (G_si * (m_range * M_sun_kg) * A0)**0.25
    v_theory_kms = v_theory_ms / 1000.0
    
    plt.plot(m_range, v_theory_kms, 'r-', linewidth=3, label='Предсказание Модели ($V^4 \propto M$)')
    
    # Оформление
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(r'Барионная Масса ($M_{bar}$) [$M_{\odot}$]', fontsize=14)
    plt.ylabel(r'Скорость Вращения ($V_{flat}$) [км/с]', fontsize=14)
    plt.title('Проверка: Барионное Соотношение Талли-Фишера (BTFR)', fontsize=16)
    
    plt.grid(True, which="both", alpha=0.2)
    plt.legend(fontsize=12)
    
    # Вывод статистики
    slope, intercept, r_value, p_value, std_err = linregress(np.log10(masses), np.log10(velocities))
    print(f"Наклон регрессии данных (Slope): {1/slope:.2f} (Теория ожидает ~4.0)")
    
    plt.show()

if __name__ == "__main__":
    plot_btfr()