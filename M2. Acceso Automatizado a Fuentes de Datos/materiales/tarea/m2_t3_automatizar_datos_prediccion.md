### **Tarea 3: Programar un Script para Recopilar Datos de Predicción de Open-Meteo**

---

### **Objetivo**
1. Crear un script en Python que obtenga datos de predicción del tiempo (forecast) para una localización específica desde la API de **Open-Meteo**.
2. Guardar los datos en un archivo CSV.
3. Programar el script para que se ejecute automáticamente todos los días a las **6:30 AM** utilizando `crontab`.

---

### **Paso 1: Desarrollo del Script**

#### **1. Crear el archivo Python**
Guarda el siguiente código en un archivo llamado `recopilar_prediccion_om.py`.

```python
import requests
import pandas as pd
from datetime import datetime

# Configuración
LAT, LON = 28.4161, -16.5446  # Coordenadas de Puerto de la Cruz
URL = "https://api.open-meteo.com/v1/forecast"
OUTPUT_FILE = "datos_prediccion_om.csv"

# Obtener datos de predicción
def recopilar_datos(lat, lon):
    try:
        # Construir request

        # Comprobar status
        
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return None

# Guardar datos en un archivo CSV
def guardar_datos(datos):
    try:
        # Procesar los datos
        
        # Guardar en CSV
        print(f"Datos guardados en {OUTPUT_FILE}")
    except KeyError as e:
        print(f"Error al procesar los datos: {e}")

# Ejecutar las funciones
if __name__ == "__main__":
    datos = recopilar_datos(LAT, LON)
    if datos:
        guardar_datos(datos)
```

---

### **Paso 2: Probar el Script**
1. Ejecuta el script manualmente para verificar que funciona correctamente:
   ```bash
   python3 recopilar_prediccion_om.py
   ```
2. Verifica que el archivo `datos_prediccion_om.csv` se haya creado con datos similares a:

```csv
time,temperature_2m_max,temperature_2m_min,precipitation_sum
2024-11-25,22.5,15.2,0.0
2024-11-26,23.0,16.1,0.1
2024-11-27,24.2,17.3,0.2
```

---

### **Paso 3: Programar la Ejecución Automática con `crontab`**

#### **1. Abrir el archivo crontab**
En la terminal, abre el editor de `crontab`:
```bash
crontab -e
```

#### **2. Añadir la tarea**
Añade la siguiente línea para programar el script a las 6:30 AM diariamente:
```bash
30 6 * * * /usr/bin/python3 /ruta/completa/recopilar_prediccion_om.py >> /ruta/completa/recopilar_prediccion_om.log 2>&1
```

- **`30 6 * * *`**: Programa la tarea a las 6:30 AM todos los días.
- **`/usr/bin/python3`**: Ruta al ejecutable de Python (puedes verificarla con `which python3`).
- **`/ruta/completa/recopilar_prediccion_om.py`**: Ruta completa al script Python.
- **`>> /ruta/completa/recopilar_prediccion_om.log 2>&1`**: Guarda la salida (y errores) en un archivo de log para depuración.

#### **3. Guardar y salir**
Guarda y cierra el archivo. La tarea se programará automáticamente.

---

### **Paso 4: Verificar la Tarea Programada**
1. Listar las tareas programadas:
   ```bash
   crontab -l
   ```
   Deberías ver la tarea registrada.

2. Verifica los logs (`recopilar_prediccion_om.log`) después de la hora programada para confirmar que el script se ejecutó correctamente.

---

### **Notas Finales**
- Si necesitas ajustar la ubicación, cambia las coordenadas (`LAT, LON`) en el script.
- Revisa el archivo de log regularmente para asegurarte de que no haya errores.
- Puedes extender la funcionalidad para enviar notificaciones o realizar análisis adicionales sobre los datos.
