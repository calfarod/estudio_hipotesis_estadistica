import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

# 1. Datos del experimento (Caso 4)
exitos = np.array([96, 69])
muestras = np.array([150, 150])

# 2. Cálculo exacto con precisión flotante (sin redondear manualmente)
z_stat, _ = proportions_ztest(count=exitos, nobs=muestras, alternative='larger')

# Tabla de contingencia 2x2 para Chi-cuadrado
tabla_contingencia = np.array([[96, 54], 
                               [69, 81]])

chi2, _, _, _ = stats.chi2_contingency(tabla_contingencia, correction=False)

# 3. Comparación con precisión completa
z_al_cuadrado = z_stat ** 2

print(f"Z calculado (precisión completa): {z_stat}")
print(f"Z² exacto:                       {z_al_cuadrado}")
print(f"Chi² exacto (Jamovi):            {chi2}")

# Verificación directa
es_idéntico = np.isclose(z_al_cuadrado, chi2)
print(f"¿Son matemáticamente iguales?:    {es_idéntico}")