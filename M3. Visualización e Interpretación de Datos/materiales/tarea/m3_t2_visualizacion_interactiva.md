# Tarea 2. Visualización Interactiva de Datos de Consumos y Generación en Edificio

En este ejercicio, exploraremos un conjunto de datos con registros horarios del año 2023 que incluyen información clave sobre el consumo de recursos, generación de energía y factores climáticos. El objetivo principal es generar visualizaciones interactivas que permitan analizar patrones y comparativas entre diferentes meses y variables.

Los datos se presentan con las siguientes columnas:

- **Fecha**: Registro temporal de las observaciones (en formato `YYYY-MM-DD HH:mm`).
- **Consumo Agua (L)**: Cantidad de agua consumida, medida en litros.
- **Consumo Energía (kWh)**: Energía consumida, medida en kilovatios hora.
- **Generación FV (kWh)**: Energía generada mediante fotovoltaica, medida en kilovatios hora.
- **Temperatura (°C)**: Temperatura registrada en grados Celsius.
- **Radiación Solar (W/m²)**: Radiación solar medida en vatios por metro cuadrado.
- **Mes**: Mes del año correspondiente a cada registro (1 a 12).
- **Día de la Semana**: Nombre o índice del día (por ejemplo, Monday, Tuesday...).

---

## **1. Objetivo de la Tarea**
1. **Visualizar datos de consumo y generación de recursos en dos meses diferentes (abril y agosto)**.
2. Generar gráficos de líneas interactivos para:
   - Comparar los **consumos** de agua y energía.
   - Comparar la **generación fotovoltaica** y la **radiación solar**.
3. Representar todas las series en un único gráfico para cada mes (abril y agosto).
4. Crear un gráfico comparativo de todas las series, compartiendo el eje X, y realizar zoom en intervalos específicos:
   - **Del 5 al 11 de abril.**
   - **Del 20 al 26 de agosto.**

---

## **2. Pasos a Seguir**

### **Paso 1: Cargar y Explorar los Datos**
1. Carga el archivo `m3_t2_datos_edificio_canarias.csv` utilizando **Pandas**.
2. Inspecciona las primeras filas para comprender la estructura de los datos.
3. Obtén un resumen estadístico de las columnas numéricas para identificar rangos, medias y valores extremos.
4. Verifica la existencia de datos faltantes o inconsistencias.

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Supongamos que los datos están en un archivo CSV
# Puedes reemplazar "datos.csv" con la ubicación de tu archivo
df = pd.read_csv("../data/m3_t2_datos_edificio_canarias.csv")

# Convertir la columna Fecha a tipo datetime
df["Fecha"] = pd.to_datetime(df["Fecha"])
```

```python
# Mostra información básica del dfframe

```

```python
# Muestra las 10 primeras filas

```

```python
# Resumen estadítico de las columnas

```

```python
# Comprobar que no faltan datos en ninguna fila

```

### **Paso 2: Generar Subconjuntos de Datos**
1. Construir 2 dataframes diferentes, uno para le mes de Abril y otro para el mes de Agosto

```python
# Filtrar datos por mes y generar subconjuntos de datos

```

**Paso 3. Generar Gráficos de Líneas por Temática**
1. Usa `plotly.express` para graficar las series `Consumo Agua (L)` y `Consumo Energía (kWh)`.
2. Genera un gráfico para abril y otro para agosto:

```python
import plotly.express as px

# Gráfico de consumos en Abril

```

```python
# Gráfico de consumos en Agosto

```

3. Usa `plotly.express` para graficar las series `Genración FV (kWh)` y `Radiació Solar (W/m2)`.
4. Genera un gráfico para abril y otro para agosto
5. Haz un zoom manual para las fechas y genera una captura:
    - 5 al 11 de abril.
    - 20 al 26 de agosto.

```python
# Gráfico de Generación y Radiación en Abril

```

```python
# Gráfico de Generación y Radiación en Agosto

```

6. Genera un gráfico con todas las series para abril y otro para agosto

```python
# Gráfico de Series en Abril
series = [
        "Consumo Agua (L)", 
        "Consumo Energía (kWh)", 
        "Generación FV (kWh)", 
        "Radiación Solar (W/m²)"
    ]
```

```python
# Gráfico de Series en Agosto

```

**Paso 4. Generar Gráficos Comparativo por Mes**
1. Agregar datos por día usando el promedio como función de agregación
2. Represntar en una sola figura cada serie en una gráfica diferente comparando diferencias entre ambos conjuntos.
3. El eje x debe ser compartido por todas las gráficas.
4. Aplicar un zoom a la figura para los primeros 10 días de cada mes.


```python
# Generar serie con día del mes a partir de Fecha

```

```python
# Agrupar por día

```

```python
# --- Gráfico 4: Comparativa de todas las series en gráficas diferentes-
import plotly.graph_objects as go
from plotly.subplots import make_subplots

titulos = [
        "Consumo Agua (L)", 
        "Consumo Energía (kWh)", 
        "Generación FV (kWh)", 
        "Radiación Solar (W/m²)"
    ]

# Usa make_subplots para generar multiples graficas en una sola figura

# Añadir trazas de cada serie y mes a la figura

# Actualizar el layout

```

```python
# Aplicar zoom en fechas específicas (update_axes)

```

---

### **Entregables**
Un informe en formato notebook que incluya:
1. Gráficos individuales para los consumos (agua y energía).
2. Gráficos individuales para generación fotovoltaica y radiación solar.
3. Gráficos combinados para todas las series por mes.
4. Gráfico comparativo interactivo con zoom en los intervalos especificados.
