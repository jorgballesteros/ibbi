# Tarea 3: Análisis de la Generación Fotovoltaica y Factores Meteorológicos

---

## **Contexto**:
Tienes un conjunto de datos que incluye registros diarios de **temperatura**, **radiación solar**, **humedad**, y **producción de energía fotovoltaica** durante un mes. El objetivo del análisis es identificar cómo las condiciones meteorológicas afectan la **generación de energía solar**.

## **Datos de Ejemplo**:
El conjunto de datos incluye las siguientes columnas:

- **Fecha**: La fecha de la observación.
- **Temperatura (°C)**: Temperatura media diaria.
- **Radiación Solar (W/m²)**: Radiación solar media diaria.
- **Humedad (%)**: Humedad relativa media diaria.
- **Generación Fotovoltaica (kWh)**: Energía generada por un sistema fotovoltaico.

---

## Generar un DataFrame Simulado con Datos

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generar datos simulados
np.random.seed(42)
fechas = pd.date_range(start="2024-10-01", periods=30)

datos = {
    "Fecha": fechas,
    "Temperatura (°C)": np.random.uniform(15, 35, size=30),
    "Radiación Solar (W/m²)": np.random.uniform(200, 1000, size=30),
    "Humedad (%)": np.random.uniform(30, 80, size=30),
    "Generación Fotovoltaica (kWh)": np.random.uniform(100, 500, size=30)
}

df = pd.DataFrame(datos)
df.set_index("Fecha", inplace=True)

# Mostrar las primeras filas del DataFrame
print("Datos Meteorológicos y de Generación Fotovoltaica:")
print(df.head())
```

---

## Instrucciones

**Objetivos del ejercicio**:

1. **Visualizar la evolución diaria** de la **temperatura, radiación solar y generación fotovoltaica** utilizando gráficos de líneas.
2. Calcular y **visualizar las correlaciones** entre las variables para entender su relación.
3. Utilizar un **gráfico de dispersión (scatter plot)** para analizar la relación entre:
   - Radiación solar y generación fotovoltaica.
   - Temperatura y generación fotovoltaica.
   - Humedad y generación fotovoltaica.
4. Crear un **mapa de calor (heatmap)** que muestre las correlaciones entre las variables.

---

**Resultados esperados**:

- El **mapa de calor** debería mostrar una correlación positiva fuerte entre **Radiación Solar** y **Generación Fotovoltaica**.
- Las **gráficas de dispersión** te ayudarán a identificar tendencias y relaciones no lineales, como el posible impacto negativo de **altas temperaturas** o **altos niveles de humedad** en la eficiencia de la generación solar.

## Solución del Ejercicio

```python
# 1. Visualizar la evolución diaria de las variables

```

```python
# 2. Calcular las correlaciones.

```

```python
# 3. Visualizar un mapa de calor de correlaciones
plt.figure(figsize=(8, 5))

```

```python
# 4. Gráficos de dispersión para analizar correlaciones específicas

# Relación entre Radiación Solar y Generación Fotovoltaica
plt.figure(figsize=(8, 5))

```

```python
# Relación entre Temperatura y Generación Fotovoltaica
plt.figure(figsize=(8, 5))

```

```python
# Relación entre Humedad y Generación Fotovoltaica
plt.figure(figsize=(8, 5))

```
---
