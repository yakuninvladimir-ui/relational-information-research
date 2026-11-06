import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# --- НАСТРОЙКИ ---
# Имя папки, куда ты положил файлы .dat
DATA_FOLDER = 'rotmod' 

# Параметр ускорения для твоей теории (a0)
A0 = 1.2e-10 

# Коэффициенты Масса/Светимость (M/L)
# В файлах SPARC Vdisk и Vbul обычно даны для M/L = 1.
# Нам нужно домножить квадрат скорости на реальный M/L.
ML_DISK = 0.5
ML_BULGE = 0.7

def theoretical_curve(g_bar):
    """
    Твоя модель диссипации (аналог MOND интерполяции).
    g_obs = g_bar / (1 - exp(-sqrt(g_bar/a0)))
    """
    # Защита от деления на ноль
    g_bar = np.maximum(g_bar, 1e-18)
    return g_bar / (1 - np.exp(-np.sqrt(g_bar / A0)))

def process_local_files():
    # Ищем все .dat файлы в указанной папке
    search_path = os.path.join(DATA_FOLDER, "*.dat")
    files = glob.glob(search_path)
    
    if not files:
        print(f"ОШИБКА: Не найдено файлов .dat в папке '{DATA_FOLDER}'")
        print(f"Создай папку '{DATA_FOLDER}' и положи туда файлы типа CamB_rotmod.dat")
        return [], []
        
    print(f"Найдено файлов: {len(files)}. Обработка...")

    all_g_bar = []
    all_g_obs = []

    # Имена колонок строго по твоему файлу CamB_rotmod.dat
    # Rad, Vobs, errV, Vgas, Vdisk, Vbul, SBdisk, SBbul
    col_names = ['Rad', 'Vobs', 'errV', 'Vgas', 'Vdisk', 'Vbul', 'SBdisk', 'SBbul']

    for file_path in files:
        try:
            # Читаем файл. comment='#' игнорирует строки с #, поэтому заголовки передаем вручную
            df = pd.read_csv(file_path, sep=r'\s+', names=col_names, comment='#')
            
            # Конвертация единиц
            # Радиус: кпк -> метры (1 kpc = 3.086e19 m)
            R_m = df['Rad'] * 3.086e19
            
            # Скорость: км/с -> м/с
            v_factor = 1000.0
            
            # --- РАСЧЕТ БАРИОННОЙ КОМПОНЕНТЫ ---
            # Формула: V_total^2 = V_gas^2 + (V_disk^2 * ML_disk) + (V_bul^2 * ML_bul)
            # Берем abs(), так как иногда скорости указаны с минусом
            V_gas_sq = (np.abs(df['Vgas']) * v_factor)**2
            V_disk_sq = (np.abs(df['Vdisk']) * v_factor)**2 * ML_DISK
            V_bulge_sq = (np.abs(df['Vbul']) * v_factor)**2 * ML_BULGE
            
            V_bar_sq = V_gas_sq + V_disk_sq + V_bulge_sq
            
            # Наблюдаемая скорость
            V_obs_sq = (np.abs(df['Vobs']) * v_factor)**2
            
            # --- РАСЧЕТ УСКОРЕНИЙ ---
            # a = V^2 / R
            # Фильтруем некорректные данные (R=0 или V=NaN)
            valid = (R_m > 0) & np.isfinite(V_obs_sq) & np.isfinite(V_bar_sq)
            
            g_bar_temp = V_bar_sq[valid] / R_m[valid]
            g_obs_temp = V_obs_sq[valid] / R_m[valid]
            
            # Убираем явные выбросы (шум измерения)
            mask = (g_bar_temp > 1e-15) & (g_bar_temp < 1e-8) & (g_obs_temp > 1e-15)
            
            all_g_bar.extend(g_bar_temp[mask])
            all_g_obs.extend(g_obs_temp[mask])
            
        except Exception as e:
            print(f"Ошибка в файле {os.path.basename(file_path)}: {e}")

    return np.array(all_g_bar), np.array(all_g_obs)

# --- ГЛАВНЫЙ БЛОК ---
if __name__ == "__main__":
    gb, go = process_local_files()
    
    if len(gb) > 0:
        print(f"Построение графика по {len(gb)} точкам...")
        
        plt.figure(figsize=(10, 8))
        
        # 1. Реальные данные (Плотность точек)
        plt.hexbin(gb, go, gridsize=60, xscale='log', yscale='log', 
                   cmap='Blues', mincnt=1, bins='log', label='Данные галактик')
        
        # 2. Линия Ньютона (1:1)
        x = np.logspace(-13, -8, 100)
        plt.plot(x, x, 'k--', lw=2, label='Ньютон (нет DM)')
        
        # 3. Твоя Теория
        y_model = theoretical_curve(x)
        plt.plot(x, y_model, 'r-', lw=3, label='Модель Диссипации')
        
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel(r'$g_{bar}$ (Барионы) [м/с$^2$]', fontsize=14)
        plt.ylabel(r'$g_{obs}$ (Наблюдаемое) [м/с$^2$]', fontsize=14)
        plt.title('Проверка теории: Radial Acceleration Relation', fontsize=16)
        plt.legend()
        plt.grid(True, which="both", alpha=0.2)
        plt.xlim(1e-12, 1e-8)
        plt.ylim(1e-12, 1e-8)
        
        plt.show()
    else:
        print("Данные не загружены.")