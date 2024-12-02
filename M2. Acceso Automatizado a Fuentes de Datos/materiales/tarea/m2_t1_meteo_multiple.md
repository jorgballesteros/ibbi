# Tarea 1. Análisis Comparativo de Datos Meteorológicos en Múltiples Ubicaciones

En este ejercicio, practicarás cómo acceder a datos meteorológicos para **múltiples ubicaciones** utilizando una **API con credenciales** y realizarás un análisis comparativo entre las ciudades seleccionadas. Además, visualizarás las **series temporales** y generarás **gráficos comparativos** para entender mejor cómo las condiciones meteorológicas varían entre ubicaciones.

---

## Objetivos de la tarea

1. **Acceder a la API** para obtener datos meteorológicos (temperatura, radiación solar y humedad) para **tres ubicaciones**.
2. **Visualizar las series temporales** de las variables meteorológicas para cada ciudad.
3. Comparar las mismas series temporales (por ejemplo, temperatura) entre las **tres ciudades** en un solo gráfico.
4. Generar un **histograma combinado** para analizar la distribución de la **temperatura** en cada ciudad.

---

## Solución del ejercicio

### 1. Acceder a la API y consultar datos
Aquí tienes un **código inicial** que te ayudará a obtener los datos para **tres ciudades** y a realizar las visualizaciones solicitadas.

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Parámetros para la consulta a la API
API_KEY = 'TU_CLAVE_API'  # Reemplaza con tu API Key
CIUDADES = ['Santa Cruz de Tenerife,ES', 'Las Palmas de Gran Canaria,ES', 'Madrid,ES']
URL_BASE = "http://api.openweathermap.org/data/2.5/forecast"
```
### Función para obtener datos de la API para una ciudad

```python

```
### Combinar datos para todas las ciudades y mostrar `head()`

```python

```

---

### 2. Visualización de las Series Temporales por Ciudad

1. **Visualiza las series temporales** de **temperatura, humedad y radiación solar** para cada ciudad de forma independiente.

```python

```

---

2. **Visualiza las series temporales para cada variable** (Temperatura, Humedad, Radiación Solar) **en una sola ciudad**.

```python

```

---

### 3. Comparación de Temperatura entre Ciudades

Genera un gráfico de **barras o líneas** para comparar la temperatura media de las tres ciudades.

```python

```

---

### 4. Histograma Combinado de la Temperatura en Cada Ciudad

Genera un **histograma combinado** para analizar la **distribución de la temperatura** en cada ciudad.

```python

```