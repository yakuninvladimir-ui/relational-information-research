import numpy as np
import os
import matplotlib.pyplot as plt

def mass_test_universal_vacuum(folder='rotmod/'):
    files = [f for f in os.listdir(folder) if f.endswith('_rotmod.dat')]
    
    # ФИКСИРОВАННЫЕ КОНСТАНТЫ (НАЙДЕННЫЕ РАНЕЕ)
    V_LIM = 128.2
    R_SCALE = 5.9
    
    v_obs_all = []
    v_pred_all = []
    
    r_vac_check = []
    v_vac_resid = [] # Остаточная скорость (наблюдения минус барионы)
    
    print(f"Обработка {len(files)} галактик с константами: V={V_LIM}, R={R_SCALE}...")
    
    for f in files:
        try:
            data = np.genfromtxt(os.path.join(folder, f))
            r = data[:, 0]
            v_obs = data[:, 1]
            err = data[:, 2]
            
            # Барионы (Газ + Диск + Балдж)
            v_gas = np.abs(data[:, 3])
            v_disk = np.abs(data[:, 4])
            v_bulge = np.abs(data[:, 5])
            v_bar_sq = v_gas**2 + v_disk**2 + v_bulge**2
            
            # Фильтр данных: убираем плохие точки (большие ошибки или наклон)
            # Берем только точки с ошибкой < 15% и скоростью > 20 км/с
            mask = (v_obs > 20) & (err < 0.15 * v_obs)
            
            if np.sum(mask) < 5: continue # Пропускаем совсем мусорные файлы
            
            r_cl = r[mask]
            v_obs_cl = v_obs[mask]
            v_bar_sq_cl = v_bar_sq[mask]
            
            # 1. РАСЧЕТ МОДЕЛИ
            v_vac_theory = V_LIM * (r_cl / (r_cl + R_SCALE))
            v_pred_sq = v_bar_sq_cl + v_vac_theory**2
            v_pred = np.sqrt(v_pred_sq)
            
            v_obs_all.extend(v_obs_cl)
            v_pred_all.extend(v_pred)
            
            # 2. ПРОВЕРКА: "СУЩЕСТВУЕТ ЛИ СИНЯЯ ЛИНИЯ?"
            # Вычитаем барионы из наблюдений: V_resid^2 = V_obs^2 - V_bar^2
            # Если теория верна, остаток должен лечь на Синюю Линию
            diff_sq = v_obs_cl**2 - v_bar_sq_cl
            # Берем только те точки, где V_obs > V_bar (иначе корень из отриц. числа)
            valid_resid = diff_sq > 0
            
            if np.any(valid_resid):
                r_vac_check.extend(r_cl[valid_resid])
                v_vac_resid.extend(np.sqrt(diff_sq[valid_resid]))
                
        except Exception as e:
            continue

    # --- ВИЗУАЛИЗАЦИЯ ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # График 1: Предсказание vs Наблюдение
    ax1.scatter(v_obs_all, v_pred_all, alpha=0.1, s=3, c='k')
    ax1.plot([0, 350], [0, 350], 'r--', lw=2, label='Ideal Match')
    
    # Статистика
    v_obs_all = np.array(v_obs_all)
    v_pred_all = np.array(v_pred_all)
    rms = np.sqrt(np.mean((v_obs_all - v_pred_all)**2))
    
    ax1.set_title(f'Universal Constant Check (RMS = {rms:.1f} km/s)')
    ax1.set_xlabel('Observed Velocity [km/s]')
    ax1.set_ylabel('Predicted Velocity (Newton + Vacuum) [km/s]')
    ax1.set_xlim(0, 300)
    ax1.set_ylim(0, 300)
    ax1.grid(True, alpha=0.2)
    ax1.legend()
    
    # График 2: Виден ли Аттрактор?
    ax2.scatter(r_vac_check, v_vac_resid, alpha=0.05, s=2, c='dodgerblue', label='Observed - Baryons')
    
    # Рисуем нашу теоретическую синюю линию
    r_plot = np.linspace(0, 100, 200)
    v_plot = V_LIM * (r_plot / (r_plot + R_SCALE))
    ax2.plot(r_plot, v_plot, 'r-', lw=3, label=f'Theoretical Attractor\n$V={V_LIM:.0f}, R_s={R_SCALE}$')
    
    ax2.set_title('Residual Vacuum Signature: $V_{vac} = \sqrt{V_{obs}^2 - V_{bar}^2}$')
    ax2.set_xlabel('Radius [kpc]')
    ax2.set_ylabel('Vacuum Velocity Contribution [km/s]')
    ax2.set_xlim(0, 60)
    ax2.set_ylim(0, 200)
    ax2.grid(True, alpha=0.2)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    mass_test_universal_vacuum()