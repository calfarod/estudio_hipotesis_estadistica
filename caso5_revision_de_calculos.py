import numpy as np
import pandas as pd
from scipy import stats

# 1. Datos del caso (Enteros)
np.random.seed(42)
pre = np.clip(
    np.random.normal(loc=45, scale=10, size=30).round(), 0, 100
).astype(int)
post = np.clip(
    pre + np.random.normal(loc=8.5, scale=8, size=30).round(), 0, 100
).astype(int)

n = len(pre)

# 2. Fórmulas paso a paso (Manual)
media_pre = sum(pre) / n
media_post = sum(post) / n

# Vector de diferencias (Post - Pre)
d = post - pre
media_diferencia = sum(d) / n
diferencia_medias = media_post - media_pre

# Desviación estándar muestral (s_d) usando fórmula con n - 1
suma_cuadrados_dif = sum((di - media_diferencia) ** 2 for di in d)
s_d = np.sqrt(suma_cuadrados_dif / (n - 1))

# Error estándar (SE_d)
se_d = s_d / np.sqrt(n)

# t-calculado manual
t_calc_manual = media_diferencia / se_d

# 3. Cálculo automatizado con scipy (para verificación)
t_stat_scipy, p_val_scipy = stats.ttest_rel(post, pre, alternative="greater")

# Imprimir desglose
print(f"1. Media Pre:                            {media_pre:.4f}")
print(f"2. Media Post:                           {media_post:.4f}")
print(f"3. Media de la Diferencias (d_bar):      {media_diferencia:.4f}")
print(f"4. Diferencia de Medias (Post - Pre):    {diferencia_medias:.4f}")
print(f"5. Desviación Estándar de la Dif (s_d):  {s_d:.4f}")
print(f"6. Error Estándar de la Dif (SE_d):      {se_d:.4f}")
print(f"7. Valor t Calculado (Fórmula Manual):   {t_calc_manual:.4f}")
print(f"8. Valor t Calculado (SciPy / Jamovi):   {t_stat_scipy:.4f}")

print(pre)
print("-"*10)
print(post)