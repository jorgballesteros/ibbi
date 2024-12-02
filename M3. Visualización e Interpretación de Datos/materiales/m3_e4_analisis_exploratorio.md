# Ejercicio 4. Análisis Exploratorio de Datos (EDA)

## Contexto del Ejercicio

Trabajaremos con un conjunto de datos de **consumo energético** y **generación fotovoltaica** de un edificio en Canarias, complementado con variables meteorológicas como temperatura, radiación solar, humedad y velocidad del viento. Este ejercicio avanzado incluye no solo un análisis descriptivo básico, sino también la **detección de anomalías**, la **segmentación de datos** y el análisis detallado de relaciones entre variables para obtener ***insights*** accionables.

## Objetivos del Ejercicio

1. Realizar un análisis descriptivo y visual de los datos.
2. Detectar **anomalías** en el consumo y la generación.
3. Analizar relaciones entre variables meteorológicas y energéticas.
4. **Segmentar datos temporalmente** (e.g., un mes específico) para un análisis detallado.
5. Evaluar patrones estacionales y diferenciar entre días laborables y fines de semana.

## Desarrollo del Ejercicio

### **Paso 1: Cargar y Explorar los Datos**

Cargamos los datos y realizamos una exploración inicial.

```python
import pandas as pd

# Cargar el conjunto de datos
ruta_csv = "data/m3_e4_datos_energia_canarias.csv"
df = pd.read_csv(ruta_csv,index_col=0)

# Inspección inicial
print("Primeras filas del conjunto de datos:")
print(df.head())
```

```python
# Información básica
print("\nInformación del conjunto de datos:")
print(df.info())
```

```python
# Resumen estadístico
print("\nResumen estadístico:")
print(df.describe())
```

**Preguntas iniciales**:
- ¿Qué variables tenemos?
- ¿Hay valores nulos o inconsistencias?
- ¿Son las fechas interpretadas correctamente?

---

### **Paso 2: Limpiar y Preparar los Datos**

1. Convertir fechas al formato `datetime`.
2. Detectar y gestionar valores nulos.
3. Crear nuevas columnas para análisis segmentado:
   - Mes, día de la semana (laborable o fin de semana).
   - Categorías climáticas (e.g., "Alta radiación" según umbrales).

```python
# Convertir la columna de fecha
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Detectar y manejar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())
df = df.dropna()  # Eliminamos filas con valores nulos
```

```python
# Crear columnas derivadas
df["Mes"] = df["Fecha"].dt.month
df["Día Semana"] = df["Fecha"].dt.day_name()
df["Es Fin de Semana"] = df["Día Semana"].isin(["Saturday", "Sunday"])
df["Categoría Radiación"] = pd.cut(df["Radiación Solar (W/m²)"],
                                    bins=[0, 500, 700, 1000],
                                    labels=["Baja", "Media", "Alta"])
```

---

### **Paso 3: Análisis Descriptivo y Visualización**

1. **Distribuciones de Consumo y Generación**:
   - Histogramas y gráficos de violín para detectar patrones y outliers.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Distribución de consumo energético
sns.histplot(df["Consumo Energía (kWh)"], kde=True, color="blue")
plt.title("Distribución del Consumo Energético")
plt.xlabel("Consumo Energía (kWh)")
plt.ylabel("Frecuencia")
plt.show()

```

```python
# Distribución de generación FV por categoría de radiación
sns.violinplot(data=df, x="Categoría Radiación", y="Generación FV (kWh)", palette="viridis", hue="Categoría Radiación")
plt.title("Distribución de Generación FV por Categoría de Radiación")
plt.xlabel("Categoría de Radiación")
plt.ylabel("Generación FV (kWh)")
plt.show()
```

---

2. **Tendencias Temporales y Segmentación**:
   - Visualización por meses o días específicos.

```python
# Filtrar datos de un mes específico (e.g., Enero)
df_enero = df[df["Mes"] == 1]

# Tendencias diarias en enero
plt.plot(df_enero["Fecha"], df_enero["Consumo Energía (kWh)"], label="Consumo Energético", color="blue")
plt.plot(df_enero["Fecha"], df_enero["Generación FV (kWh)"], label="Generación FV", color="green")
plt.title("Tendencias Diarias en Enero")
plt.xlabel("Fecha")
plt.ylabel("Energía (kWh)")
plt.legend()
plt.grid()
plt.show()
```

---

### **Paso 4: Detección de Anomalías**

1. Identificar días con consumos o generación fuera de lo esperado mediante **percentiles** o **reglas estadísticas**.

```python
# Detección de outliers basada en percentiles
p10 = df["Consumo Energía (kWh)"].quantile(0.10)
p90 = df["Consumo Energía (kWh)"].quantile(0.90)

# Marcar valores fuera del rango esperado
df["Es Anómalo"] = (df["Consumo Energía (kWh)"] < p10) | (df["Consumo Energía (kWh)"] > p90)

# Visualizar anomalías
plt.figure(figsize=(12, 6))
plt.plot(df["Fecha"], df["Consumo Energía (kWh)"], label="Consumo Energético", color="blue")
plt.scatter(df[df["Es Anómalo"]]["Fecha"], df[df["Es Anómalo"]]["Consumo Energía (kWh)"], color="red", label="Anomalías")
plt.title("Detección de Anomalías en Consumo Energético")
plt.xlabel("Fecha")
plt.ylabel("Consumo Energía (kWh)")
plt.legend()
plt.show()
```

---

### **Paso 5: Relaciones Entre Variables**

Visualizar y analizar correlaciones para detectar dependencias entre consumo, generación y variables meteorológicas.

```python
# Matriz de correlación
correlaciones = df[["Consumo Energía (kWh)", "Generación FV (kWh)", "Temperatura (°C)", "Radiación Solar (W/m²)"]].corr()
sns.heatmap(correlaciones, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Matriz de Correlación")
plt.show()
```

```python
# Relación entre radiación solar y generación
sns.scatterplot(data=df, x="Radiación Solar (W/m²)", y="Generación FV (kWh)", hue="Categoría Radiación", palette="viridis")
plt.title("Relación entre Radiación Solar y Generación FV")
plt.xlabel("Radiación Solar (W/m²)")
plt.ylabel("Generación FV (kWh)")
plt.show()
```

---

### **Conclusión**

Este ejercicio avanzado de EDA hemos analizado datos energéticos y meteorológicos para identificar patrones, detectar anomalías y explorar relaciones clave. A través de técnicas visuales y estadísticas, obtenemos ***insights*** críticos sobre estacionalidad, días atípicos y factores que afectan el consumo y la generación de energía. Esta metodología es esencial para optimizar recursos y tomar decisiones basadas en datos en sistemas energéticos reales.
