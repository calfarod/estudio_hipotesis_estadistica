import numpy as np
import pandas as pd
from scipy import stats

# 1. Simulación de los 30 datos de ejemplo (semilla para reproducibilidad)
# np.random.seed(42)
# intencion_pre = np.random.normal(loc=45, scale=10, size=30).round().astype(int)
intencion_pre = [50, 44, 51, 60, 43, 43, 61, 53, 40, 50, 40, 40, 47, 26, 28, 39, 35, 48, 36, 31, 60, 43, 46, 31, 40, 46, 33, 49, 39, 42]
# Se simula un incremento real promedio de +3.5 puntos con variabilidad
# intencion_post = intencion_pre + np.random.normal(loc=3.5, scale=8, size=30).round().astype(int)
intencion_post = [50, 63, 55, 56, 54, 38, 67, 42, 34, 56, 50, 46, 51, 28, 21, 38, 36, 61, 43, 21, 67, 44, 45, 40, 53, 58, 31, 51, 46, 54]

df = pd.DataFrame({"Pre": intencion_pre, "Post": intencion_post})

# 2. Formulación de hipótesis
print("Ho: d_media <= 0 (La campaña no aumentó la intención de compra, no hay cambio significativo.)")
print("Ha: d_media > 0 (La campaña Sí aumentó la intención de compra.)")

# 3. Resumen descriptivas
df['Diferencia'] = df['Post'] - df['Pre']
d_media = df['Diferencia'].mean()
s_d = df['Diferencia'].std(ddof=1)
n = len(df)

# 4. Cálculo del Error Estándar de la Diferencia
se_d = s_d / np.sqrt(n)

# 5. Imprimir resultados descriptivos
print("--- RESUMEN DESCRIPTIVO ---")
print(f"🌈  Media Pre:                  {df['Pre'].mean():.2f}")
print(f"🌈  Media Post:                 {df['Post'].mean():.2f}")
print(f"🌈  Diferencia Media (d_bar):   {d_media:.2f}")
print(f"Desviación Estándar (s_d):  {s_d:.2f}")
print(f"Error Estándar (SE_d):      {se_d:.4f}")

# 6. Prueba t para Muestras Emparejadas (scipy.stats)
# Nota: 'alternative="greater"' evalúa si Post es estrictamente mayor que Pre
# greater le indica a Python que ejecute una prueba de hipótesis unilateral (de una sola cola a la derecha)
t_stat, p_val = stats.ttest_rel(df["Post"], df["Pre"], alternative="greater")
t_calc_manual = (d_media - 0) / se_d

# 7. Impresión de resultados
print(df)
print("--- PRUEBA T MUESTRAS EMPAREJADAS (CASO 5) ---")
print(f"❤️Diferencia Media (Post - Pre): {d_media:.2f}")
print(f"Desviación Estándar Dif.     : {s_d:.2f}")
print(f"Estadístico t calculado      : {t_stat:.4f}")
print(f"Estadístico t_calc_manual    : {t_calc_manual:.4f}")
print(f"Grados de libertad (df)      : {len(df) - 1}")
print(f"Valor p (unilateral)         : {p_val:.5f}")

if p_val < 0.05:
    print(
        "\nDecisión: Se RECHAZA H0. La campaña Sí aumentó la intención de compra."
    )
else:
    print("\nDecisión: NO se rechaza H0. No hay cambio significativo.")