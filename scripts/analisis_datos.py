import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer los datos de la carpeta datos
df = pd.read_csv('datos/ventas.csv')

# 2. Multiplicar Cantidad x Precio para saber el total de cada fila
df['Total'] = df['cantidad_vendida'] * df['precio_unitario']

# 3. Calcular los Indicadores que pide el TP
total_general = df['Total'].sum()
producto_mas_vendido = df.groupby('producto')['cantidad_vendida'].sum().idxmax()
ventas_por_mes = df.groupby('sales_date')['Total'].sum() # Agrupado directo por fecha

# 4. Mostrar los resultados en la pantalla de Colab
print("--- RESULTADOS ---")
print(f"Ventas Totales: ${total_general}")
print(f"Producto más vendido: {producto_mas_vendido}")
print("\nVentas por fecha:")
print(ventas_por_mes)

# 5. Hacer el gráfico de barras y guardarlo en la carpeta resultados
ventas_por_mes.plot(kind='bar')
plt.title('Ventas de la Empresa')
plt.tight_layout()
plt.savefig('resultados/evolucion_ventas.png')
print("\n[OK] Gráfico guardado en resultados/evolucion_ventas.png")