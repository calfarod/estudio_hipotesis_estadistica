import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. Parámetros del experimento (Caso 3)
alpha = 0.05
z_critico = stats.norm.ppf(1 - alpha)  # 1.6449
z_calculado = 1.7678                   # Resultado de statsmodels

# 2. Generar datos de la distribución normal estándar N(0,1)
x = np.linspace(-3.5, 3.5, 1000)
y = stats.norm.pdf(x)

# 3. Configuración de figura responsiva
# Usamos un DPI estándar para pantalla (100) y ajustamos la figura a 9x4.5 pulgadas
plt.rcParams['figure.autolayout'] = True
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=100)

# Dibujar la curva principal
ax.plot(x, y, color='#1d3557', linewidth=2, label='Distribución Nula N(0,1)')

# Sombrear Región de Rechazo (Z > Z_crítico)
x_rechazo = np.linspace(z_critico, 3.5, 200)
y_rechazo = stats.norm.pdf(x_rechazo)
ax.fill_between(x_rechazo, y_rechazo, color='#e63946', alpha=0.3, label=f'Zona de Rechazo (α = {alpha})')

# Líneas verticales
ax.axvline(x=z_critico, color='#e63946', linestyle='--', linewidth=1.5, label=f'Z-Crítico ({z_critico:.4f})')
ax.axvline(x=z_calculado, color='#2a9d8f', linestyle='-', linewidth=2, label=f'Z-Calculado ({z_calculado:.4f})')

# Anotaciones con coordenadas ajustadas para evitar solapamiento
ax.annotate(f'Z-Crítico\n{z_critico:.4f}', 
            xy=(z_critico, stats.norm.pdf(z_critico)), 
            xytext=(z_critico - 1.1, 0.18),
            arrowprops=dict(facecolor='#e63946', edgecolor='#e63946', arrowstyle='->', lw=1.2),
            fontsize=8.5, fontweight='bold', color='#e63946', 
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff0f0', edgecolor='#e63946'))

ax.annotate(f'Z-Calculado (Muestra)\n{z_calculado:.4f} (p = 0.0385)', 
            xy=(z_calculado, stats.norm.pdf(z_calculado)), 
            xytext=(z_calculado + 0.2, 0.28),
            arrowprops=dict(facecolor='#2a9d8f', edgecolor='#2a9d8f', arrowstyle='->', lw=1.2),
            fontsize=8.5, fontweight='bold', color='#2a9d8f', 
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f5e9', edgecolor='#2a9d8f'))

# Títulos y formato limpio
ax.set_title("Prueba Z de 1 Proporción: Adopción 'Viaje Silencioso'", fontsize=11, fontweight='bold', pad=12, color='#1d3557')
ax.set_xlabel("Estadístico Z", fontsize=9, labelpad=6)
ax.set_ylabel("Densidad de Probabilidad", fontsize=9, labelpad=6)

ax.set_xlim(-3.5, 3.5)
ax.set_ylim(0, 0.45)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')

ax.legend(loc='upper left', fontsize=8, frameon=True, facecolor='#ffffff', edgecolor='#e9ecef')
ax.grid(axis='x', linestyle=':', alpha=0.5)

# Guardar en ALTA RESOLUCIÓN para producción/reportes (sin afectar la pantalla)
plt.savefig("grafico_caso3_export.png", dpi=300, bbox_inches='tight')

# Mostrar en pantalla ajustado
plt.show()