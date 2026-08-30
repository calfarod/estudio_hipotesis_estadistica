import numpy as np
from scipy import stats

# 1. Datos e hiperparámetros de la prueba
datos = [
    78, 82, 85, 71, 79, 83, 74, 88, 76, 80, 
    81, 73, 87, 72, 77, 84, 79, 75, 82, 78, 
    86, 70, 81, 79, 83, 77, 80, 75, 82, 76
]

mu_0 = 80
alpha = 0.05
n = len(datos)
df = n - 1

# 2. Estadísticos muestrales
media = np.mean(datos)
desviacion = np.std(datos, ddof=1)
error_estandar = desviacion / np.sqrt(n)

# 3. Estadístico de prueba t y valor p
t_calc = (media - mu_0) / error_estandar
p_value = 2 * stats.t.sf(abs(t_calc), df)

# 4. Cálculo del Valor Crítico (Dos Colas)
t_critico = stats.t.ppf(1 - alpha / 2, df)

# 5. Salida de resultados
print(f"Estadístico t calculado: {t_calc:.4f}")
print(f"Valor crítico (±):        ±{t_critico:.4f}")
print(f"Región de rechazo:        t < -{t_critico:.4f}  o  t > +{t_critico:.4f}")
print(f"Valor p:                  {p_value:.4f}")

# Criterio de decisión usando el valor crítico
if abs(t_calc) > t_critico:
    print("Decisión: Se RECHAZA H0 (El estadístico cae en la región crítica).")
else:
    print("Decisión: NO se rechaza H0 (El estadístico cae dentro del intervalo de aceptación).")