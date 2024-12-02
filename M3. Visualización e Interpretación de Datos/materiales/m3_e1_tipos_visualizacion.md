# Ejercicio 1. Tipos de Visualización de Datos 

---

## Introducción a la Visualización de Datos

La visualización de datos es una herramienta esencial para comprender patrones, tendencias y relaciones en un conjunto de datos. Existen diversos tipos de datos que podemos representar, y para cada tipo, ciertos gráficos son más adecuados:

### Tipos de Datos
1. **Datos Temporales**: Fechas u horas (e.g., consumo diario, tendencias de ventas).
   - **Gráficos recomendados**: Líneas, áreas, barras.
2. **Datos Categóricos**: Agrupados en categorías (e.g., tipo de producto, estaciones).
   - **Gráficos recomendados**: Barras, caja y bigotes, violines.
3. **Datos Continuos**: Valores numéricos (e.g., temperatura, ingresos).
   - **Gráficos recomendados**: Histogramas, diagramas de dispersión.
4. **Datos Relacionales**: Relaciones entre variables (e.g., correlaciones).
   - **Gráficos recomendados**: Mapas de calor, diagramas de dispersión.

**Pregunta clave antes de elegir un gráfico:**
¿Qué queremos comunicar? Tendencias, distribuciones, relaciones o variaciones.
Antes de elegir un gráfico, es fundamental preguntarse: **¿Qué queremos comunicar con los datos?** Esto ayuda a seleccionar el tipo de gráfico más adecuado según el propósito del análisis. Aquí tienes una breve explicación de las categorías principales:

#### **1. Tendencias**
- **¿Qué representan?**
  - Muestran cómo cambia una variable a lo largo del tiempo o en relación a otra dimensión.
- **Cuándo usarlos:**
  - Para datos temporales o secuenciales, como el consumo energético diario o la temperatura a lo largo de los meses.
- **Gráficos recomendados:**
  - Líneas, áreas, barras.

#### **2. Distribuciones**
- **¿Qué representan?**
  - Visualizan cómo se distribuyen los valores de una variable, resaltando patrones como concentraciones, dispersiones y outliers.
- **Cuándo usarlos:**
  - Para analizar la frecuencia y dispersión de datos continuos, como el rango de temperaturas o la variabilidad del consumo.
- **Gráficos recomendados:**
  - Histogramas, boxplots, violines.

### **3. Relaciones**
- **¿Qué representan?**
  - Muestran cómo dos o más variables están conectadas entre sí.
- **Cuándo usarlos:**
  - Para identificar correlaciones o dependencias entre variables, como la relación entre la radiación solar y el consumo energético.
- **Gráficos recomendados:**
  - Diagramas de dispersión, mapas de calor.

### **4. Variaciones**
- **¿Qué representan?**
  - Resaltan cambios y diferencias entre categorías o grupos.
- **Cuándo usarlos:**
  - Para comparar valores agrupados, como el consumo promedio de diferentes edificios o meses.
- **Gráficos recomendados:**
  - Barras, boxplots.

La clave está en la **historia que queremos contar**. Si buscas mostrar cambios a lo largo del tiempo, usaremos gráficos de tendencia; si queremos entender relaciones, enfócate en gráficos relacionales. Tener clara esta pregunta nos permitirá elegir el gráfico más impactante y efectivo para el análisis.

---

## Creación de Gráficos con Matplotlib y Seaborn

Trabajaremos con un dataset simulado que contiene datos diarios de consumo energético y de agua en un edificio ubicado en Canarias durante un año.

```python
import pandas as pd
import numpy as np

# Generar datos simulados
np.random.seed(42)
fechas = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
consumo_energia = 300 + 20 * np.sin(2 * np.pi * fechas.dayofyear / 365) + np.random.normal(0, 10, len(fechas))
consumo_agua = 25 + 5 * np.cos(2 * np.pi * fechas.dayofyear / 365) + np.random.normal(0, 2, len(fechas))

# Crear DataFrame
df = pd.DataFrame({
    "Fecha": fechas,
    "Consumo Energía (kWh)": consumo_energia,
    "Consumo Agua (m³)": consumo_agua
})
```

### Gráficos de Series Temporales

#### **Gráfico de Líneas**
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(df["Fecha"], df["Consumo Energía (kWh)"], label="Energía (kWh)", color="blue")
plt.plot(df["Fecha"], df["Consumo Agua (m³)"], label="Agua (m³)", color="green")
plt.title("Consumo Diario de Energía y Agua")
plt.xlabel("Fecha")
plt.ylabel("Consumo")
plt.legend()
plt.grid(True)
plt.show()
```

**Cuándo usarlo:** Para mostrar tendencias a lo largo del tiempo.

#### **Gráfico de Barras**
```python
df["Mes"] = df["Fecha"].dt.strftime("%B")
df_mensual = df.groupby("Mes").mean().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(df_mensual.index, df_mensual["Consumo Energía (kWh)"], label="Energía", alpha=0.7, color="blue")
plt.bar(df_mensual.index, df_mensual["Consumo Agua (m³)"], label="Agua", alpha=0.7, color="green")
plt.title("Consumo Promedio Mensual")
plt.xlabel("Mes")
plt.ylabel("Consumo")
plt.legend()
plt.show()
```

**Cuándo usarlo:** Para comparar cantidades agrupadas por categorías.

#### **Gráfico de Áreas**
```python
plt.figure(figsize=(10, 5))
plt.fill_between(df["Fecha"], df["Consumo Energía (kWh)"], color="blue", alpha=0.4, label="Energía")
plt.fill_between(df["Fecha"], df["Consumo Agua (m³)"], color="green", alpha=0.4, label="Agua")
plt.title("Consumo Diario de Energía y Agua (Áreas)")
plt.xlabel("Fecha")
plt.ylabel("Consumo")
plt.legend()
plt.show()
```

**Cuándo usarlo:** Para visualizar proporciones acumulativas o totales a lo largo del tiempo.

### Distribuciones y Variaciones

#### **Histograma**
```python
plt.figure(figsize=(10, 5))
plt.hist(df["Consumo Energía (kWh)"], bins=20, alpha=0.7, label="Energía", color="blue")
plt.hist(df["Consumo Agua (m³)"], bins=20, alpha=0.7, label="Agua", color="green")
plt.title("Distribución del Consumo")
plt.xlabel("Consumo")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()
```

**Cuándo usarlo:** Para mostrar la distribución de datos continuos.

#### Gráficos de caja y violín
```python
import seaborn as sns

plt.figure(figsize=(10, 5))
sns.boxplot(data=df[["Consumo Energía (kWh)", "Consumo Agua (m³)"]])
plt.title("Variación en el Consumo")
plt.xlabel("Tipo de Consumo")
plt.ylabel("Consumo")
plt.show()

plt.figure(figsize=(10, 5))
sns.violinplot(data=df[["Consumo Energía (kWh)", "Consumo Agua (m³)"]])
plt.title("Distribución del Consumo (Violín)")
plt.xlabel("Tipo de Consumo")
plt.ylabel("Consumo")
plt.show()
```

**Cuándo usarlo:** Para visualizar variaciones, outliers y distribuciones.

### Relación entre Variables

#### **Gráfico de Dispersión**
```python
plt.figure(figsize=(10, 5))
plt.scatter(df["Consumo Energía (kWh)"], df["Consumo Agua (m³)"], alpha=0.6, color="purple")
plt.title("Relación entre Consumo de Energía y Agua")
plt.xlabel("Consumo Energía (kWh)")
plt.ylabel("Consumo Agua (m³)")
plt.grid(True)
plt.show()
```

**Cuándo usarlo:** Para explorar relaciones entre dos variables continuas.

#### **Mapa de Calor**
```python
correlaciones = df[["Consumo Energía (kWh)", "Consumo Agua (m³)"]].corr()

plt.figure(figsize=(8, 5))
sns.heatmap(correlaciones, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlaciones entre Variables")
plt.show()
```

**Cuándo usarlo:** Para analizar correlaciones entre múltiples variables.

---

## Conclusiones
1. Los **gráficos de líneas y áreas** son ideales para representar tendencias en series temporales.
2. **Histogramas y boxplots** muestran distribuciones y outliers.
3. Los **diagramas de dispersión** y **mapas de calor** ayudan a entender relaciones entre variables.
4. Matplotlib ofrece flexibilidad detallada, mientras que Seaborn simplifica la creación de gráficos más complejos con estilos predefinidos.