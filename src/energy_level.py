import numpy as np
import matplotlib.pyplot as plt

def calculate_energy_levels(n, L, m, hbar):
    """
    固有エネルギーを計算する関数

    パラメータ:
    n (int): 量子数
    L (float): 井戸の幅 (メートル)
    m (float): 粒子の質量 (キログラム)
    hbar (float): プランク定数

    戻り値:
    float: 固有エネルギー (ジュール)
    """
    return (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)

# 定数の定義
L = 1e-9  # 1 nm
m = 9.109e-31  # 電子の質量 (kg)
hbar = 1.054e-34  # プランク定数 (Js)

# n = 1 から 10 までの固有エネルギーを計算
n_values = np.arange(1, 11)
energies = [calculate_energy_levels(n, L, m, hbar) for n in n_values]

# 結果の表示
for n, energy in zip(n_values, energies):
    print(f"n = {n}, E_n = {energy:.3e} J")

# エネルギー準位のプロット
plt.figure(figsize=(10, 6))
plt.plot(n_values, energies, 'bo-')
plt.xlabel('量子数 n')
plt.ylabel('固有エネルギー E_n (J)')
plt.title('無限に深い井戸型ポテンシャルの固有エネルギー')
plt.grid(True)
plt.show()