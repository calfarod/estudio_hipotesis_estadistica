import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

# 1. Datos resumidos del experimento
exitos = np.array([96, 69])  # [Corporativo, Estandar]
muestras = np.array([150, 150])

# Proporciones observadas
p1_hat = exitos[0] / muestras[0]  # 64.0%
p2_hat = exitos[1] / muestras[1]  # 46.0%

alpha = 0.05

# 2. Prueba Z para 2 Proporciones (Una cola: 'larger' -> p1 > p2)
z_stat, p_value = proportions_ztest(count=exitos, nobs=muestras, alternative='larger')
z_critico = stats.norm.ppf(1 - alpha)

# 3. Hipótesis
print("👑 \n")
print("="*50)
print("\n❄️ --- HIPÓTESIS ---")
print("\n")
print("Hipótesis Nula (Ho): p1 <= p2 (La proporción de adopción del segmento Corporativo es menor o igual a la del segmento Estándar).")
print("Hipótesis Alternativa (Ha): p1 > p2 (La proporción de adopción del segmento Corporativo es mayor que la del segmento Estándar).")

# 4. Formateo de Resultados
print("\n")
print("="*50)
print("\n")

print("❄️ --- RESULTADOS PRUEBA Z PARA 2 PROPORCIONES INDEPENDIENTES ---")
print(f"Proporción Corporativo (p1_hat): {p1_hat:.2%}")
print(f"Proporción Estándar    (p2_hat): {p2_hat:.2%}")
print(f"Diferencia observada           : {(p1_hat - p2_hat):.2%}")
print(f"Estadístico Z-calculado:       : {z_stat:.4f}")
print(f"Valor Z-Crítico (alpha={alpha}): {z_critico:.4f}")
print(f"Valor-p (p-value)              : {p_value:.4f}")

# 5. Regla de Decisión
print("\n")
print("="*50)
print("\n❄️ --- REGLA DE DECISIÓN ---")
print("\nSi Valor-p < alpha entonces Rechazar Ho")
print("Si Z-calculado < Z-crítico: entonces Rechazar Ho")

# 6. Conclusión
print("\n")
print("="*50)
print("\n❄️ --- CONCLUSIÓN ---")

if p_value < alpha:
    print("✅ RECHAZAR H0: Los usuarios Corporativos adoptan el Autopago a una tasa significativamente mayor.")
else:
    print("❌ NO RECHAZAR H0: No hay diferencia significativa en la adopción entre segmentos.")


print("="*50)
print("\n")
