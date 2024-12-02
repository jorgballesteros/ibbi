# Ejercicio 3. Librerías para Visualización Avanzada de Datos
En este ejercicio, exploraremos el uso de **Seaborn**, una potente biblioteca de visualización de datos en Python, para crear gráficos avanzados que permitan analizar y comunicar patrones, relaciones y distribuciones en los datos.

Compararemos su funcionalidad con Matplotlib para destacar las ventajas de Seaborn en el análisis exploratorio de datos. Este ejercicio te permitirá comprender cuándo y cómo aplicar las herramientas de Seaborn en tus proyectos de análisis de datos, garantizando visualizaciones atractivas y efectivas.

También profundizaremos en buenas prácticas de uso, como la integración con Pandas, el uso de paletas predefinidas y la personalización de gráficos para garantizar la claridad y efectividad. 

Por último, exploraremos otras herramientas populares en Python para visualización, como Plotly (gráficos interactivos), Bokeh (visualización para grandes datos), y Altair (gráficos declarativos), permitiéndote elegir la herramienta más adecuada según el contexto y la audiencia.

## Introducción a Seaborn

### ¿Qué es Seaborn?
Seaborn es una biblioteca de visualización de datos en Python basada en Matplotlib. Fue desarrollada para simplificar la creación de gráficos estadísticos y mejorar su estética, integrando automáticamente características como estilos predeterminados, paletas de colores y gráficos complejos. 

### ¿Por qué surge Seaborn?
Matplotlib es poderoso y altamente personalizable, pero requiere muchas configuraciones para obtener gráficos visualmente atractivos. Seaborn surge para abordar esta limitación, permitiendo generar gráficos más elegantes y con configuraciones predeterminadas minimalistas, ahorrando tiempo y esfuerzo. 

### ¿En qué complementa Matplotlib?
- Estilos predeterminados y consistentes.
- Integración automática con estructuras de datos como DataFrames de Pandas.
- Gráficos estadísticos avanzados (e.g., distribuciones, relaciones entre variables, heatmaps).
- Funcionalidades simplificadas para trabajar con múltiples categorías y dimensiones.

### ¿Cuándo usar Seaborn en lugar de Matplotlib?
- **Seaborn**: Para análisis exploratorio, gráficos estadísticos y comparaciones categóricas o relacionales.
- **Matplotlib**: Para gráficos personalizados, diseño detallado y cuando se necesitan elementos específicos que Seaborn no ofrece.

---

## Tipos de Visualización en Seaborn

Seaborn permite crear diversos tipos de gráficos según el tipo de datos y el objetivo:

1. **Distribuciones de Datos**:
   - Histogramas, KDEs, gráficos de violín, y gráficos de caja y bigotes.
   - Ejemplo: Comparar la distribución de edades en un grupo.

2. **Relaciones entre Variables**:
   - Diagramas de dispersión, gráficos lineales y gráficos de regresión.
   - Ejemplo: Identificar la correlación entre temperatura y consumo energético.

3. **Comparaciones Categóricas**:
   - Gráficos de barras, puntos, cajas y violines categóricos.
   - Ejemplo: Comparar ingresos promedio por departamento.

4. **Matrices y Mapas de Calor**:
   - Mapas de calor (heatmaps) y visualización de correlaciones.
   - Ejemplo: Analizar relaciones entre múltiples variables numéricas.

5. **Series Temporales**:
   - Gráficos de líneas con múltiples categorías.
   - Ejemplo: Visualizar tendencias mensuales de ventas.

---

## Ejemplos de Uso

### **Ejercicio: Visualización Avanzada con Seaborn**

---

### **1. Contexto del Ejercicio**

En este ejercicio, exploraremos el potencial de **Seaborn** para crear visualizaciones avanzadas de datos, enfocándonos en la representación de tendencias, relaciones y distribuciones. Vamos a trabajar con un conjunto de datos que incluye **consumo energético**, **generación fotovoltaica** y **variables meteorológicas**. Ampliaremos el uso de **Seaborn** explorando funcionalidades como el uso del parámetro `hue`, la representación de rangos de valores (mínimos y máximos), y gráficos avanzados de líneas y distribuciones.

---

### **2. Objetivos del Ejercicio**

1. **Comprender y aplicar** las funcionalidades de Seaborn para representar relaciones complejas entre variables.
2. **Utilizar `hue`** para diferenciar categorías o grupos en gráficos.
3. Representar **rangos de valores** en gráficos de líneas para mostrar variabilidad o incertidumbre.
4. **Combinar múltiples tipos de gráficos** para obtener insights más completos.

---

### **3. Desarrollo del Ejercicio**

#### **Paso 1: Preparación del Conjunto de Datos**

Simularemos un conjunto de datos con las siguientes características:
- **Consumo energético (kWh)** diario de un edificio.
- **Generación fotovoltaica (kWh)** de una instalación de 40 kW.
- **Variables meteorológicas**: temperatura, radiación solar, humedad.
- Datos generados para **un año completo** con estacionalidad y variabilidad diaria.

```python
import pandas as pd
import numpy as np

# Configuración inicial
np.random.seed(42)
fechas = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

# Generar variables con estacionalidad
consumo_energia = 300 + 20 * np.sin(2 * np.pi * fechas.dayofyear / 365) + np.random.normal(0, 10, len(fechas))
generacion_fv = 200 + 30 * np.sin(2 * np.pi * (fechas.dayofyear -90)/ 365) + np.random.normal(0, 15, len(fechas))
temperatura = 20 + 5 * np.sin(2 * np.pi * fechas.dayofyear / 365) + np.random.normal(0, 2, len(fechas))
radiacion_solar = 600 + 100 * np.sin(2 * np.pi * (fechas.dayofyear -90) / 365) + np.random.normal(0, 50, len(fechas))

# Crear DataFrame
df = pd.DataFrame({
    "Fecha": fechas,
    "Consumo Energía (kWh)": consumo_energia,
    "Generación FV (kWh)": generacion_fv,
    "Temperatura (°C)": temperatura,
    "Radiación Solar (W/m²)": radiacion_solar,
    "Mes": fechas.month,
    "Día de la Semana": fechas.day_name()
})
```

```python
# Guardamos datos en local
df.to_csv("data/m3_e3_datos_energia_canarias.csv")
```

```python
import matplotlib.pyplot as plt
plt.plot(df['Fecha'], df["Consumo Energía (kWh)"], label="Consumo")
# Configuramos títulos y leyendas
plt.title('Evolución del Consumo de Energía')
plt.xlabel('Fecha')
plt.ylabel('Consumo (kW)')
plt.show()
```

---

#### **Paso 2: Gráficos de Líneas con `hue`**

Visualicemos el **consumo energético** y la **generación fotovoltaica** diferenciando los meses con el parámetro `hue`.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Gráfico de líneas con `hue`
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Fecha", y="Consumo Energía (kWh)", hue="Mes", palette="viridis")
plt.title("Consumo Energético Diario Diferenciado por Mes")
plt.xlabel("Fecha")
plt.ylabel("Consumo Energía (kWh)")
plt.legend(title="Mes", loc="upper right")
plt.grid(True)
plt.show()
```

**¿Por qué usar `hue`?**
- Permite diferenciar grupos o categorías en un gráfico continuo, mostrando cómo cambian los valores según una dimensión adicional (e.g., mes, categoría).

---

#### **Paso 3: Representación de Rangos (Mínimo y Máximo)**

Supongamos que queremos mostrar el rango de generación fotovoltaica para cada mes. Calcularemos los valores mínimos, máximos y promedio para graficarlos.

```python
# Calcular promedios, mínimos y máximos por mes
df_mes = df.groupby("Mes").agg({
    "Generación FV (kWh)": ["mean", "min", "max"]
}).reset_index()
df_mes.columns = ["Mes", "Generación Media (kWh)", "Generación Mínima (kWh)", "Generación Máxima (kWh)"]

# Gráfico de líneas con banda de rango
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_mes, x="Mes", y="Generación Media (kWh)", label="Media", color="green")
plt.fill_between(df_mes["Mes"], 
                 df_mes["Generación Mínima (kWh)"], 
                 df_mes["Generación Máxima (kWh)"], 
                 color="green", 
                 alpha=0.2, 
                 label="Rango (Min-Max)")
plt.title("Generación Fotovoltaica Mensual con Rango Min-Max")
plt.xlabel("Mes")
plt.ylabel("Generación FV (kWh)")
plt.legend()
plt.grid(True)
plt.show()
```

**¿Por qué representar rangos?**
- Ayuda a visualizar la variabilidad de los datos, resaltando periodos de mayor o menor incertidumbre.

---

#### **Paso 4: Combinación de Relación y Distribución**

Visualicemos la relación entre la **radiación solar** y la **generación fotovoltaica**, incluyendo distribuciones marginales.

```python
# Gráfico de dispersión con distribuciones marginales
sns.jointplot(data=df, x="Radiación Solar (W/m²)", y="Generación FV (kWh)", kind="scatter", hue="Mes", palette="cool")
plt.suptitle("Relación entre Radiación Solar y Generación FV", y=1.02)
plt.show()
```

**¿Por qué usar gráficos combinados?**
- Facilitan el análisis detallado de relaciones, proporcionando una visión completa de las distribuciones y tendencias.

---

#### **Paso 5: Distribuciones Categorizadas**

Analicemos cómo varía el consumo energético según el día de la semana.

```python
# Gráfico de violín para consumo energético por día de la semana
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x="Día de la Semana", y="Consumo Energía (kWh)", palette="pastel")
plt.title("Distribución de Consumo Energético por Día de la Semana")
plt.xlabel("Día de la Semana")
plt.ylabel("Consumo Energía (kWh)")
plt.grid(True)
plt.show()
```

**¿Por qué usar gráficos de violín?**
- Combina información de distribución (histograma) y resumen estadístico (boxplot) en un solo gráfico.

---

#### Comparativa: Seaborn vs Matplotlib (Gráficos de Distribución)
Con Matplotlib:
```python
import matplotlib.pyplot as plt
import numpy as np

# Datos simulados
# datos = np.random.normal(size=100)
datos = df["Generación FV (kWh)"]

plt.hist(datos, bins=20, color="blue", alpha=0.7)
plt.title("Distribución con Matplotlib")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
```

Con Seaborn:
```python
import seaborn as sns

# Distribución con Seaborn
sns.histplot(datos, bins=20, kde=True, color="crimson", alpha=0.6, line_kws={'color': 'crimson', 'lw': 5, 'ls': ':'})
plt.title("Distribución con Seaborn")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
```

### Gráficos Relacionales
```python
# Datos simulados de consumos de aga y energía e tres edificios
import pandas as pd
np.random.seed(42)
cat_df = pd.DataFrame({
    "Consumo Energía": np.random.normal(300, 20, 100),
    "Consumo Agua": np.random.normal(30, 5, 100),
    "Edificio": np.random.choice(["A", "B", "C"], 100)
})

# Relación con Seaborn
sns.scatterplot(data=cat_df, x="Consumo Energía", y="Consumo Agua", hue="Edificio", style="Edificio", palette="cool")
plt.title("Relación entre Consumos")
plt.show()
```

### Mapa de Calor
```python
# Mapa de calor de correlaciones
cols = ["Consumo Energía (kWh)", "Generación FV (kWh)", "Temperatura (°C)", "Radiación Solar (W/m²)"]
correlaciones = df[cols].corr()
sns.heatmap(correlaciones, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Mapa de Calor de Correlaciones")
plt.show()
```

---

## Buenas Prácticas de Uso

1. **Integración con Pandas**:
   - Trabaja directamente con DataFrames para facilitar el manejo de datos categóricos y numéricos.
  
2. **Paletas de Colores**:
   - Usa paletas predefinidas de Seaborn (`deep`, `muted`, `cool`) para gráficos consistentes y estéticamente agradables.

3. **Ajuste de Ejes y Títulos**:
   - Aunque Seaborn configura automáticamente muchos aspectos, personaliza los ejes y títulos según el contexto.

4. **Uso de Facetas**:
   - Aprovecha funciones como `sns.FacetGrid` para dividir gráficos por categorías.

5. **Exploración de Datos**:
   - Utiliza gráficos de distribución y correlación para obtener insights iniciales antes de profundizar en el análisis.

---

## Otras Herramientas/Librerías para Visualización

1. **Plotly**:
   - Para gráficos interactivos y dashboards.
   - Ideal para exploración visual avanzada y aplicaciones dinámicas.

2. **Bokeh**:
   - Centrada en gráficos interactivos para grandes conjuntos de datos.

3. **Altair**:
   - Declarativa, fácil de usar y bien integrada con Pandas.

4. **ggplot (Python)**:
   - Inspirada en ggplot2 de R, orientada a gráficos estadísticos.

5. **Dash**:
   - Construcción de aplicaciones web interactivas con visualizaciones.

6. **Streamlit**:
   - Creación aplicaciones web interactivas de forma rápida y sencilla para visualizar, explorar y analizar datos.

---

## Conclusión

Seaborn es una herramienta que complementa a Matplotlib, facilitando la creación de gráficos estadísticos elegantes con configuraciones mínimas. Su integración con Pandas y sus estilos predefinidos lo hacen ideal para análisis exploratorio y comparativo. Aunque no reemplaza completamente a Matplotlib, Seaborn simplifica tareas comunes y destaca en la visualización de relaciones complejas y distribuciones, ofreciendo una experiencia eficiente y visualmente atractiva.
