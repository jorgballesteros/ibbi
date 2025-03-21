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
def obtener_datos_meteorologicos(ciudad):
    url = f"{URL_BASE}?q={ciudad}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        fechas, temp, humedad, radiacion = [], [], [], []
        for entry in datos['list']:
            fechas.append(entry['dt_txt'])
            temp.append(entry['main']['temp'])
            humedad.append(entry['main']['humidity'])
            # Usamos el porcentaje de nubes como aproximación inversa de la radiación solar
            radiacion.append(100 - entry['clouds']['all'])
        return pd.DataFrame({
            "Fecha": pd.to_datetime(fechas),
            "Temperatura (°C)": temp,
            "Humedad (%)": humedad,
            "Radiación Solar (%)": radiacion,
            "Ciudad": ciudad
        })
    else:
        print(f"Error al obtener datos para {ciudad}")
        return None
```
### Combinar datos para todas las ciudades y mostrar `head()`

```python
dfs = [obtener_datos_meteorologicos(ciudad) for ciudad in CIUDADES]
df_combined = pd.concat(dfs).set_index("Fecha")

# Mostrar las primeras filas del DataFrame combinado
print("\nDatos combinados:")
print(df_combined.head())
```

---

### 2. Visualización de las Series Temporales por Ciudad

1. **Visualiza las series temporales** de **temperatura, humedad y radiación solar** para cada ciudad de forma independiente.

```python
plt.figure(figsize=(12, 6))
for ciudad in CIUDADES:
    df_ciudad = df_combined[df_combined['Ciudad'] == ciudad]
    plt.plot(df_ciudad.index, df_ciudad["Temperatura (°C)"], label=f"Temperatura en {ciudad}")

plt.title("Serie Temporal de Temperatura por Ciudad")
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

2. **Visualiza las series temporales para cada variable** (Temperatura, Humedad, Radiación Solar) **en una sola ciudad**.

```python
ciudad_seleccionada = 'Santa Cruz de Tenerife,ES'
df_tenerife = df_combined[df_combined['Ciudad'] == ciudad_seleccionada]

plt.figure(figsize=(12, 6))
plt.plot(df_tenerife.index, df_tenerife["Temperatura (°C)"], label="Temperatura (°C)", color='red')
plt.plot(df_tenerife.index, df_tenerife["Humedad (%)"], label="Humedad (%)", color='blue')
plt.plot(df_tenerife.index, df_tenerife["Radiación Solar (%)"], label="Radiación Solar (%)", color='orange')

plt.title(f"Serie Temporal de Variables Meteorológicas en {ciudad_seleccionada}")
plt.xlabel("Fecha")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

```

---

### 3. Comparación de Temperatura entre Ciudades

Genera un gráfico de **barras o líneas** para comparar la temperatura media de las tres ciudades.

```python
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_combined, x=df_combined.index, y="Temperatura (°C)", hue="Ciudad")
plt.title("Comparación de Temperatura entre Ciudades")
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

### 4. Histograma Combinado de la Temperatura en Cada Ciudad

Genera un **histograma combinado** para analizar la **distribución de la temperatura** en cada ciudad.

```python
plt.figure(figsize=(10, 6))
sns.histplot(data=df_combined, x="Temperatura (°C)", hue="Ciudad", bins=15, palette="viridis")
plt.title("Distribución de la Temperatura en Diferentes Ciudades")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.tight_layout()
plt.show()
```