# Tarea 1. Análisis Exploratorio de Datos (EDA) de Datos de Centro de Entrenamiento Deportivo

---

## **1. Objetivo de la Tarea**

El objetivo de esta tarea es realizar un **Análisis Exploratorio de Datos (EDA)** del conjunto de datos generado, que contiene información diaria sobre:
- Asistencia al centro de entrenamiento.
- Condiciones meteorológicas (temperatura y humedad).
- Consumo de agua y energía.

Tu misión será explorar y visualizar los datos para identificar patrones, relaciones, anomalías y posibles insights relacionados con el comportamiento del consumo y la asistencia al gimnasio.

---

## **2. Pasos a Seguir**

### **Paso 1: Cargar y Explorar los Datos**
1. Carga el archivo `m4_t1_datos_entrenamiento_deportivo.csv` utilizando **Pandas**.
2. Inspecciona las primeras filas para comprender la estructura de los datos.
3. Obtén un resumen estadístico de las columnas numéricas para identificar rangos, medias y valores extremos.
4. Verifica la existencia de datos faltantes o inconsistencias.
## **3. Código Base**

A continuación, un esquema para que comiences con el análisis:

```python
# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
ruta_csv = "../data/m3_t1_datos_entrenamiento_deportivo.csv"
df = pd.read_csv(ruta_csv)
# Convertimos columna Fecha a objeto tipo fecha
df['Fecha'] = pd.to_datetime(df['Fecha'])
```

### **Paso 2: Análisis Descriptivo**
1. Analiza la **distribución de asistencia**, **temperatura**, **humedad**, **consumo de agua** y **energía** mediante histogramas.
2. Examina cómo varía la asistencia y los consumos entre los **días laborables y fines de semana**.
3. Observa la **distribución estacional** (por meses) de las variables meteorológicas y los consumos.
```python
# Exploración inicial
print("Primeras filas del conjunto de datos:")

print("\nResumen estadístico:")

print("\nValores nulos por columna:")

```

```python
# Visualización: Distribuciones (usa sns.histplot)
plt.figure(figsize=(10, 6))

```
```python
# Variación de asistencia entre días laborables y fines de semana

# Crear una columna para identificar fines de semana
df["Es Fin de Semana"] = df["Día de la Semana"].isin(["Saturday", "Sunday"])
# Gráfico de barras: Asistencia media en días laborables y fines de semana (barplot)
plt.figure(figsize=(10, 6))
```
```python
# Distribución estacional por meses de temperatura, humedad y consumo de energía

# Generar columna de mes
df['Mes'] = df['Fecha'].dt.month

# Agrupa por mes usando el promedio

```

### **Paso 3: Visualización de Tendencias**
1. Crea gráficos de líneas para observar cómo evolucionan:
   - La asistencia a lo largo del año.
   - El consumo de agua y energía.
   - La temperatura y la humedad.
2. Identifica patrones o anomalías, especialmente en los meses con anomalías (abril, octubre y diciembre).

```python
import matplotlib.pyplot as plt

# Gráfico de líneas: Asistencia a lo largo del año (plt.plot())
plt.figure(figsize=(12, 6))

# Gráfico de líneas: Consumo de Agua y Energía

# Gráfico de líneas: Temperatura y Humedad

```

### **Paso 4: Relaciones Entre Variables**
1. Usa gráficos de dispersión para explorar la relación entre:
   - Temperatura, asistencia y día de la semana.
   - Temperatura y consumo de agua.
   - Asistencia y consumo de energía.
2. Calcula la matriz de correlación entre las variables numéricas y visualízala con un **heatmap**.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Gráfico de dispersión: Relación entre Temperatura y Consumo de Agua (scatterplot())
plt.figure(figsize=(10, 6))

# Gráfico de dispersión: Relación entre Asistencia y Consumo de Energía (scatterplot())

# Relación entre temperatura y consumo de agua y día de la semana (scatterplot() con hue)

```

```python
# Matriz de correlación (heatmap())
plt.figure(figsize=(10, 8))
# Selecciona solo columnas con valores numéricos

```

---

## **4. Resultados Esperados**

1. **Distribuciones**:
   - Identificar si la asistencia tiene picos o está equilibrada.
   - Ver cómo varían los consumos según las condiciones meteorológicas.

2. **Tendencias**:
   - Observar la estacionalidad en el consumo y asistencia.
   - Detectar patrones semanales (fines de semana vs laborables).

3. **Relaciones**:
   - Confirmar si los consumos son más elevados en días calurosos.
   - Ver cómo la asistencia afecta el consumo de agua y energía.

---

## **5. Entregables**

- Un informe que incluya:
  - Gráficos generados.
  - Conclusiones basadas en el análisis.
