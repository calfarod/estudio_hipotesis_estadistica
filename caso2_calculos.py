import pandas as pd
import numpy as np
from scipy import stats

# 1. Crear el Dataset
edades = (['Joven'] * 50) + (['Adulto'] * 50) + (['Adulto_Mayor'] * 50)
medios_joven = ['App_Movil']*24 + ['Efectivo']*8 + ['Tarjeta']*18
medios_adulto = ['App_Movil']*7 + ['Efectivo']*14 + ['Tarjeta']*29
medios_mayor = ['App_Movil']*5 + ['Efectivo']*30 + ['Tarjeta']*15

medios = medios_joven + medios_adulto + medios_mayor

df = pd.DataFrame({'Edad': edades, 'MedioPago': medios})

# 2. Tabla de contingencia (Frecuencias Observadas)
tabla_contingencia = pd.crosstab(df['Edad'], df['MedioPago'])

# 3. Prueba Chi-Cuadrado de Independencia
chi2_stat, p_val, dof, expected = stats.chi2_contingency(tabla_contingencia)

# 4. Valor Crítico para alpha = 0.05
alpha = 0.05
chi2_critico = stats.chi2.ppf(1 - alpha, dof)

# 5. Salida de Resultados
print("\n")
print("="*45)
print("❄️ --- FORMULACIÓN DE LA HIPÓTESIS ---")
print("🧩 Ho: Medio de pago (Son Independientes de) Edad")
print("🧩 Ha: Medio de pago (Son Dependiente de) Edad")
print("\n❄️ --- TABLA DE CONTINGENCIA (OBSERVADOS) ---")
print(tabla_contingencia)
print("\n❄️ --- RESULTADOS PRUEBA CHI-CUADRADO ---")
print(f"✅ Estadístico Chi2 calculado: {chi2_stat:.4f}")
print(f"Valor p (p-value):          {p_val:.4e}")
print(f"Grados de libertad (df):    {dof}")
print(f"✅ Valor crítico (alpha 0.05): {chi2_critico:.4f}")


print("\n❄️ --- REGLA DE DECISIÓN ---")
print("🤔 Si 'Estadístico Chi2 calculado' > 'Valor crítico', se rechaza H0.")
print("🤔 Si 'Valor p' < 0.05, se rechaza H0.")

if chi2_stat > chi2_critico:
    print("\n❤️ Decisión: Se RECHAZA H0 (Las variables están asociadas).")
else:
    print("\n💛 Decisión: NO se rechaza H0 (Las variables son independientes).")

print("\n")
print("="*45)

print(expected)