import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def analyze_blue_line_physics(folder='rotmod/'):
    files = [f for f in os.listdir(folder) if f.endswith('_rotmod.dat')]
    r_all, v_all = [], []

    for f in files:
        try:
            data = np.genfromtxt(os.path.join(folder, f))
            r, v_obs = data[:, 0], data[:, 1]
            v_gas = np.abs(data[:, 3])
            v_stars = np.sqrt(data[:, 4]**2 + data[:, 5]**2)
            
            # Фильтр: газ доминирует, убираем явные нули и шумы
            mask = (v_gas > v_stars) & (v_obs > 0)
            r_all.extend(r[mask])
            v_all.extend(v_obs[mask])
        except: 
            continue

    r_all, v_all = np.array(r_all), np.array(v_all)

    # Модель аттрактора (Синяя линия)
    def blue_line_model(r, v_max, r_scale):
        return v_max * (r / (r + r_scale))

    # Фитируем
    popt, _ = curve_fit(blue_line_model, r_all, v_all, p0=[130, 8])
    
    plt.figure(figsize=(12, 8))
    
    # Газовые точки - наш фундамент
    plt.scatter(r_all, v_all, alpha=0.15, s=12, c='dodgerblue', label='Газо-доминантные точки (SPARC)')
    
    # Синяя линия аттрактора на крупном плане
    r_plot = np.linspace(0.01, 60, 1000)
    v_plot = blue_line_model(r_plot, *popt)
    
    plt.plot(r_plot, v_plot, 'b-', linewidth=4, 
             label=f'Синяя линия: V = {popt[0]:.1f} * R / (R + {popt[1]:.1f})')
    
    # Оформление по твоим параметрам
    plt.title('Детальный профиль Синей Линии (Масштаб: 60 кпк / 150 км/с)', fontsize=14)
    plt.xlabel('Radius (kpc)', fontsize=12)
    plt.ylabel('V_obs (km/s)', fontsize=12)
    
    plt.xlim(0, 60)
    plt.ylim(0, 150) # Твое ограничение
    
    plt.legend(fontsize=12, loc='lower right')
    plt.grid(True, which='both', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    print(f"--- Результаты уточненного фита ---")
    print(f"V_max (Асимптота): {popt[0]:.2f} km/s")
    print(f"R_scale (Масштаб изгиба): {popt[1]:.2f} kpc")
    
    return popt

if __name__ == "__main__":
    params = analyze_blue_line_physics()