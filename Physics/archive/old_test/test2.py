import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# --- НАСТРОЙКИ ---
# Папка с файлами .dat (SPARC Mass Models)
DATA_FOLDER = 'rotmod' 

# Параметр a0 для теоретической кривой
A0 = 1.2e-10 

# Коэффициенты Масса/Светимость (M/L)
ML_DISK = 0.5
ML_BULGE = 0.7

def theoretical_curve(g_bar):
    """
    Теоретическая кривая вашей модели.
    """
    g_bar = np.maximum(g_bar, 1e-18)
    return g_bar / (1 - np.exp(-np.sqrt(g_bar / A0)))

def process_files_with_gas_fraction():
    # Ищем файлы
    search_path = os.path.join(DATA_FOLDER, "*.dat")
    files = glob.glob(search_path)
    
    if not files:
        print(f"ОШИБКА: Не найдено файлов .dat в папке '{DATA_FOLDER}'")
        return [], [], []
        
    print(f"Найдено галактик: {len(files)}. Обработка...")

    all_g_bar = []
    all_g_obs = []
    all_f_gas = [] # Сюда будем складывать долю газа для каждой точки

    # Имена колонок (для файлов без заголовка, как CamB_rotmod.dat)
    col_names = ['Rad', 'Vobs', 'errV', 'Vgas', 'Vdisk', 'Vbul', 'SBdisk', 'SBbul']

    for file_path in files:
        try:
            # Читаем файл
            df = pd.read_csv(file_path, sep=r'\s+', names=col_names, comment='#')
            
            # Перевод единиц
            R_m = df['Rad'] * 3.086e19  # kpc -> m
            v_factor = 1000.0           # km/s -> m/s
            
            # --- КОМПОНЕНТЫ СКОРОСТИ ---
            # Берем модуль (abs), так как SPARC иногда пишет "-" для направления
            V_gas = np.abs(df['Vgas']) * v_factor
            V_disk = np.abs(df['Vdisk']) * v_factor
            V_bul = np.abs(df['Vbul']) * v_factor
            
            # Квадраты скоростей (пропорциональны массе внутри радиуса R)
            # V^2 ~ M/R -> M ~ V^2 * R
            # Для расчета ДОЛИ газа (отношения) R и G сокращаются.
            # Mass_gas ~ V_gas^2
            # Mass_star ~ V_disk^2 * ML + V_bul^2 * ML
            
            M_gas_proxy = V_gas**2
            M_star_proxy = (V_disk**2 * ML_DISK) + (V_bul**2 * ML_BULGE)
            M_tot_proxy = M_gas_proxy + M_star_proxy
            
            # Доля газа в данной точке (f_gas)
            # Защита от деления на ноль (если вся скорость 0)
            f_gas = np.divide(M_gas_proxy, M_tot_proxy, out=np.zeros_like(M_gas_proxy), where=M_tot_proxy!=0)
            
            # --- УСКОРЕНИЯ ---
            V_bar_sq = M_tot_proxy # Это и есть полная барионная "скорость в квадрате"
            V_obs_sq = (np.abs(df['Vobs']) * v_factor)**2
            
            valid = (R_m > 0) & np.isfinite(V_obs_sq) & np.isfinite(V_bar_sq) & (V_bar_sq > 0)
            
            g_bar = V_bar_sq[valid] / R_m[valid]
            g_obs = V_obs_sq[valid] / R_m[valid]
            f_gas_valid = f_gas[valid]
            
            # Фильтр шума
            mask = (g_bar > 1e-15) & (g_bar < 1e-8) & (g_obs > 1e-15)
            
            all_g_bar.extend(g_bar[mask])
            all_g_obs.extend(g_obs[mask])
            all_f_gas.extend(f_gas_valid[mask])
            
        except Exception as e:
            # print(f"Skip {os.path.basename(file_path)}: {e}")
            pass

    return np.array(all_g_bar), np.array(all_g_obs), np.array(all_f_gas)

# --- MAIN ---
if __name__ == "__main__":
    gb, go, fg = process_files_with_gas_fraction()
    
    if len(gb) > 0:
        print(f"Построение графика по {len(gb)} точкам...")
        
        plt.figure(figsize=(12, 9))
        
        # 1. Точки данных с цветовой кодировкой (cmap='jet' или 'viridis')
        # c=fg задает цвет по массиву доли газа
        sc = plt.scatter(gb, go, c=fg, cmap='jet', s=10, alpha=0.4, label='Данные SPARC')
        
        # Цветовая шкала
        cbar = plt.colorbar(sc)
        cbar.set_label('Доля газа ($f_{gas} = M_{gas}/M_{bar}$)', fontsize=14)
        
        # 2. Линия Ньютона
        x = np.logspace(-13, -8, 100)
        plt.plot(x, x, 'k--', lw=2, label='Ньютон (1:1)')
        
        # 3. Твоя Теория
        y_model = theoretical_curve(x)
        plt.plot(x, y_model, 'r-', lw=3, label='Модель Диссипации')
        
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel(r'$g_{bar}$ [м/с$^2$]', fontsize=14)
        plt.ylabel(r'$g_{obs}$ [м/с$^2$]', fontsize=14)
        plt.title('RAR: Проверка гипотезы "Запирания" в газе', fontsize=16)
        plt.legend(loc='upper left', fontsize=12)
        plt.grid(True, which="both", alpha=0.2)
        
        plt.xlim(1e-13, 1e-8)
        plt.ylim(1e-13, 1e-8)
        
        plt.show()
    else:
        print("Нет данных.")