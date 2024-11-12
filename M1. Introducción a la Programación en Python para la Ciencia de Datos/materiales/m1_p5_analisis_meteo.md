### **Caso Práctico 5: Análisis de Datos Meteorológicos en Canarias**

---

### **Contexto**:
Supongamos que tienes datos meteorológicos de las islas Canarias que incluyen **temperatura, humedad, velocidad del viento, y precipitaciones** registradas diariamente en varias islas durante el último mes. El objetivo de este ejercicio es analizar y visualizar las tendencias para entender mejor las condiciones climáticas en la región.

---

### **Datos de Ejemplo**
Los datos que vamos a utilizar incluyen:

- **Fecha**: La fecha de la observación.
- **Isla**: La isla donde se realizó la medición.
- **Temperatura (°C)**: Temperatura media diaria.
- **Humedad (%)**: Humedad relativa media diaria.
- **Velocidad del Viento (km/h)**: Velocidad promedio del viento.
- **Precipitación (mm)**: Cantidad de precipitación diaria.

Vamos a crear un DataFrame con estos datos para simular el análisis.

---

### Generar un DataFrame Simulado con Datos Meteorológicos

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios simulados para 5 islas en Canarias durante un mes
np.random.seed(42)
fechas = pd.date_range(start="2024-10-01", periods=30)

islas = ["Tenerife", "Gran Canaria", "Lanzarote", "Fuerteventura", "La Palma"]
datos = {
    "Fecha": np.tile(fechas, len(islas)),
    "Isla": np.repeat(islas, len(fechas)),
    "Temperatura (°C)": np.random.uniform(20, 30, size=len(fechas) * len(islas)),
    "Humedad (%)": np.random.uniform(50, 80, size=len(fechas) * len(islas)),
    "Velocidad del Viento (km/h)": np.random.uniform(10, 30, size=len(fechas) * len(islas)),
    "Precipitación (mm)": np.random.uniform(0, 10, size=len(fechas) * len(islas))
}

df = pd.DataFrame(datos)
df.set_index("Fecha", inplace=True)
```

```python
# Mostrar las primeras filas del DataFrame
print("Datos Meteorológicos de Canarias:")
print(df.head())
```

```python
# Mostrar las últimas filas del DataFrame
print(df.tail())
```

---

### Instrucciones

**Instrucciones**:

1. Calcula la **temperatura promedio** por isla para el mes y ordénalas de mayor a menor.
2. Crea un gráfico de **líneas** que muestre la evolución de la temperatura diaria para las islas Tenerife y Gran Canaria.
3. Visualiza un gráfico de **barras** que compare la **precipitación total** acumulada por cada isla.
4. Crea un gráfico de **área apilada** para mostrar la distribución de la **velocidad del viento** en todas las islas.

**Resultados esperados**:
Estos gráficos te permitirán obtener **insights clave** sobre el clima en las Islas Canarias, como qué isla tiene las temperaturas más altas, la relación entre temperatura y humedad, y cómo varía la velocidad del viento entre las islas.

---

### Solución del Ejercicio

```python
# 1. Calcular la temperatura promedio por isla. Usa groupby para agrupar por isla

```

```python
# 2. Gráfico de líneas para la evolución de la temperatura en Tenerife y Gran Canaria
plt.figure(figsize=(10, 5))
for isla in ["Tenerife", "Gran Canaria"]:
    print(isla)

```

```python
# 3. Gráfico de barras para la precipitación total por isla. Usa groupby para agrupar por isla

plt.figure(figsize=(10, 6))
# Usamos la funcion bar de matplotlib
```

```python
# 4. Gráfico de área apilada para la velocidad del viento en todas las islas
df_viento = df.pivot_table(index=df.index, columns="Isla", values="Velocidad del Viento (km/h)", aggfunc="mean")

plt.figure(figsize=(10, 6))
# Usamos la funcion stackplot de matplotlib

```