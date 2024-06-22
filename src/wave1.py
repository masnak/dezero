import numpy as np
import matplotlib.pyplot as plt

# 空間の範囲と分割数を設定
x_min, x_max, num_points = -10, 10, 1000
x = np.linspace(x_min, x_max, num_points)

# 時間の範囲と分割数を設定
t_min, t_max, num_time_points = 0, 10, 100
t = np.linspace(t_min, t_max, num_time_points)

# ガウス波束の初期状態を設定
def initial_wave_function(x):
    """初期波動関数を定義（ガウス波束）"""
    x0 = 0  # 中心位置
    sigma = 1  # 波束の幅
    k0 = 5  # 波数
    return np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)

# 空間グリッド上に初期波動関数を計算
psi_0 = initial_wave_function(x)

# 時間発展のための関数（ここでは時間依存は考慮しない）
def time_evolution(psi_0, t):
    """時間発展を計算（単純化のため、時間依存を無視）"""
    return psi_0

# 波動関数を時間発展させた結果を計算
psi_t = np.array([time_evolution(psi_0, time) for time in t])

# 初期状態の波動関数をプロット
plt.plot(x, np.abs(psi_0)**2, label='Initial |ψ(x)|^2')
plt.xlabel('Position x')
plt.ylabel('Probability Density |ψ(x)|^2')
plt.title('Initial Wave Function')
plt.legend()
plt.show()