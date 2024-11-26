### **Tarea: Programar Consultas a OpenWeatherMap y OpenMeteo para Variables Meteorológicas Actuales**

---

### **Objetivo:**
Desarrollar **dos scripts independientes** para realizar consultas automáticas a las APIs de **OpenWeatherMap** y **OpenMeteo** cada 15 minutos, obteniendo las siguientes variables meteorológicas actuales para una ubicación específica:

- **Temperatura**
- **Humedad**
- **Nubes**
- **Velocidad del viento**
- **Dirección del viento**
- **Precipitación**

Además, los datos deben almacenarse en archivos **CSV** separados para cada API.

---

### **Requisitos previos**

1. **Obtén tu API Key de OpenWeatherMap**: [https://openweathermap.org/](https://openweathermap.org/).
2. **Instala las librerías necesarias**:

```bash
pip install requests pandas
```

---

### **Paso 1: Script para OpenWeatherMap**

Guarda este código en un archivo llamado, por ejemplo, `recopilacion_owm.py`:

```python
import requests
import pandas as pd
from datetime import datetime

# API Key y URL para OpenWeatherMap
API_KEY = "TU_CLAVE_API"
URL = "https://api.openweathermap.org/data/2.5/weather"

# Parámetros de la consulta 
params = {
    "lat": 28.4138,  # Latitud
    "lon": -16.5448,  # Longitud
    "appid": API_KEY,
    "units": "metric"  # Unidades métricas
}

# Función para realizar la consulta y guardar los datos
def consulta_openweathermap():
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        # Comprobar que los datos son devueltos
        
        # Extraer las variables y generar una marca de timepo para guardado
        
        # Guardar en un CSV añadiendo datos al final del archivo

        print(f"Datos guardados en {archivo_csv}")
    else:
        print(f"Error en la consulta a OpenWeatherMap: {response.status_code}")

# Ejecutar la consulta
if __name__ == "__main__":
    consulta_openweathermap()
```

---

### **Paso 2: Script para OpenMeteo**

Guarda este código en un archivo llamado, por ejemplo, `recopilacion_om.py`:

```python
import json
import requests
import pandas as pd
from datetime import datetime

# URL para OpenMeteo
URL = "https://api.open-meteo.com/v1/forecast"

# Parámetros de la consulta 
params = {
    "latitude": 28.4138,
    "longitude": -16.5448,
    "current": "temperature_2m,relative_humidity_2m,precipitation,cloud_cover,wind_speed_10m,wind_direction_10m"
}
# Función para realizar la consulta y guardar los datos
def consulta_openmeteo():
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        # Comprobar que los datos son devueltos
        
        # Extraer las variables y generar una marca de timepo para guardado
        
        # Guardar en un CSV añadiendo datos al final del archivo
        print(f"Datos guardados en {archivo_csv}")
    else:
        print(f"Error en la consulta a OpenMeteo: {response.status_code}")

# Ejecutar la consulta
if __name__ == "__main__":
    consulta_openmeteo()
```

---

### **Paso 3: Automatización de la Ejecución**

Para ejecutar los scripts cada 15 minutos, puedes usar una **tarea programada** en tu sistema operativo:

#### En Linux / macOS:
1. Abre el crontab para editar:
   ```bash
   crontab -e
   ```

2. Añade las siguientes líneas para ejecutar ambos scripts cada 15 minutos:
   ```bash
   */15 * * * * /usr/bin/python3 /ruta/a/tu/recopilacion_owm.py
   */15 * * * * /usr/bin/python3 /ruta/a/tu/recopilacion_om.py
   ```

#### En Windows:
1. Abre el **Programador de tareas**.
2. Crea dos tareas independientes:
   - Una para ejecutar `recopilacion_owm.py`.
   - Otra para ejecutar `recopilacion_om.py`.
3. Configura la ejecución de cada tarea cada 15 minutos.

---

### **Resultados Esperados**

- **Archivos CSV generados**:
  - `datos_owm.csv`: Contendrá las variables meteorológicas actuales proporcionadas por OpenWeatherMap.
  - `datos_om.csv`: Contendrá las variables meteorológicas actuales proporcionadas por OpenMeteo.

- **Contenido del CSV**: Cada fila representará un registro de tiempo actual, con columnas para temperatura, humedad, nubes, velocidad del viento, dirección del viento, y precipitación.

---

### **Extensiones Opcionales**

1. **Análisis de datos históricos**: Puedes leer ambos CSVs y comparar las variables entre las dos APIs para identificar discrepancias.
2. **Visualización en tiempo real**: Usa **Matplotlib** o **Dash** para graficar las variables en tiempo real.
3. **Dashboard Automatizado**: Integra los datos en un flujo de trabajo con **Node-RED** o una aplicación web.
