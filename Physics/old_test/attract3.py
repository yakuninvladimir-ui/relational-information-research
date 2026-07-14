import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def check_gas_fraction_scaling(folder='rotmod/'):
    files = [f for f in os.listdir(folder) if f.endswith('_rotmod.dat')]
    R_FIXED = 5.9
    
    gas_fractions = []
    v_vac_plateaus = []
    
    for f in files:
        try:
            data = np.genfromtxt(os.path.join(folder, f))
            r, v_obs = data[:, 0], data[:, 1]
            v_gas = np.abs(data[:, 3])
            v_disk = np.abs(data[:, 4])
            v_bulge = np.abs(data[:, 5])
            
            v_bar_sq = v_gas**2 + v_disk**2 + v_bulge**2
            
            # Считаем долю газа (gas fraction) как прокси отношения масс
            # Берем среднее значение по внешним областям, где формируется плато
            outer_mask = (r > 0.5 * np.max(r))
            f_gas = np.mean(v_gas[outer_mask]**2 / v_bar_sq[outer_mask])
            
            # Фитируем высоту аттрактора V_vac
            def model(r_val, v_plat):
                return v_plat * (r_val / (r_val + R_FIXED))
            
            resid_sq = v_obs**2 - v_bar_sq
            mask = (resid_sq > 0) & (r > 2)
            if np.sum(mask) < 5: continue
            
            popt, _ = curve_fit(model, r[mask], np.sqrt(resid_sq[mask]), p0=[120])
            
            gas_fractions.append(f_gas)
            v_vac_plateaus.append(popt[0])
        except: continue

    plt.figure(figsize=(10, 6))
    plt.scatter(gas_fractions, v_vac_plateaus, alpha=0.6, c='seagreen', edgecolors='k')
    
    # Тренд
    z = np.polyfit(gas_fractions, v_vac_plateaus, 1)
    p = np.poly1d(z)
    plt.plot(np.sort(gas_fractions), p(np.sort(gas_fractions)), "r--", alpha=0.8)
    
    plt.title('Зависимость отклика Вакуума от доли Газа ($f_{gas}$)')
    plt.xlabel('Доля Газа ($M_{gas}/M_{bar}$)')
    plt.ylabel('Высота Аттрактора ($V_{vac}$) [km/s]')
    plt.grid(True, alpha=0.2)
    plt.show()

if __name__ == "__main__":
    check_gas_fraction_scaling()