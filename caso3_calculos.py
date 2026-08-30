import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

# 1. Parámetros del experimento
exitos = 72       # Usuarios que adoptaron el servicio
nobs = 200        # Muestra total
p_0 = 0.30        # Meta comercial (30%)

# 2. Ejecutar la Prueba Z para 1 Proporción (Una cola: 'larger')
z_stat, p_value = proportions_ztest(count=exitos, nobs=nobs, value=p_0, alternative='larger')

# 3. Nivel de confianza 95% (alpha = 0.05)
alpha = 0.05            # alpha = 5%

# 4. Prueba de Una Cola a la Derecha (H1: p > p0)
# Buscamos el valor de Z que deja un 5% de área a la derecha (95% a la izquierda)
z_critico_una_cola = stats.norm.ppf(1 - alpha)

# 4b. en otro caso, si Prueba de Dos Colas (H1: p ≠ p0)
# Dividimos alpha entre 2 (2.5% en cada cola)
# z_critico_dos_colas = stats.norm.ppf(1 - (alpha / 2))

# 5. Formulación hipótesis
print("\n")
print("="*45)
print("\n❄️ --- FORMULACIÓN DE LA HIPÓTESIS ---")
print("🧩 Ho: p <= 0.31")
print("🧩 Ha: p > 0.31")

# 6. Formatear y mostrar resultados
print("\n")
print("="*45)
print("❄️ --- RESULTADOS PRUEBA Z PARA 1 PROPORCIÓN ---")
print(f"Proporción Muestral (p_hat): {exitos/nobs:.2%}")
print(f"✅ Estadístico Z-calculado:     {z_stat:.4f}")
print(f"✅ Valor-p (p-value):           {p_value:.4f}\n")

# 7. Criterios de decisión
print("="*45)
print("\n❄️ --- CRITERIOS DE DECISIÓN ---")
print(f"Nivel de significancia (alpha): {alpha:.2%}")
print(f"✅ Valor-p (p-value):           {p_value:.4f}\n")

print(f"Valor Z-crítico (una cola):     {z_critico_una_cola:.4f}")
print(f"✅ Estadístico Z-calculado:     {z_stat:.4f}")

print("Si alpha >= p-value, se rechaza H0.")
print("Si Z calculado > Z crítico, se rechaza H0.")

# 8. Decisión
print("\n")
print("="*45)
print("\n❄️ --- DECISIÓN ---")
if p_value < alpha:
    print("\n❤️ Decisión: RECHAZAR H0 -> El producto supera la meta de adopción comercial.\n")
else:
    print("\n💛 Decisión: NO RECHAZAR H0 -> El producto no alcanza la meta suficiente.\n")

print("="*45)
print("\n")