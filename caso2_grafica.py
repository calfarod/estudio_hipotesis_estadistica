import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Reconstrucción del DataFrame del Caso 2
edades = (["Joven"] * 50) + (["Adulto"] * 50) + (["Adulto_Mayor"] * 50)
medios_joven = ["App_Movil"] * 24 + ["Tarjeta"] * 17 + ["Efectivo"] * 9
medios_adulto = ["App_Movil"] * 7 + ["Tarjeta"] * 29 + ["Efectivo"] * 14
medios_mayor = ["App_Movil"] * 6 + ["Tarjeta"] * 12 + ["Efectivo"] * 32

df = pd.DataFrame(
    {
        "Edad": edades,
        "MedioPago": medios_joven + medios_adulto + medios_mayor,
    }
)

# 2. Configuración del estilo visual (estilo minimalista)
sns.set_theme(style="ticks")
plt.figure(figsize=(7, 6))

# Paleta de colores parecida a la imagen
paleta = {
    "App_Movil": "#A0C4FF",
    "Tarjeta": "#C4C4C4",
    "Efectivo": "#E8C88B",
}

# 3. Creación del gráfico de barras agrupadas
ax = sns.countplot(
    data=df,
    x="Edad",
    hue="MedioPago",
    palette=paleta,
    hue_order=["App_Movil", "Tarjeta", "Efectivo"],
)

# 4. Ajustes de títulos y ejes
plt.title(
    "Gráficos",
    fontsize=16,
    fontweight="bold",
    loc="left",
    color="#33527A",
    pad=15,
)
plt.xlabel("Edad", fontsize=12, labelpad=10)
plt.ylabel("Frecuencias", fontsize=12)
plt.legend(title="MedioPago", frameon=False, bbox_to_anchor=(1.02, 0.6))

# Eliminar bordes superior e derecho
sns.despine()

plt.tight_layout()
plt.show()