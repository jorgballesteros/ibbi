## Ejercicio 5. Pipeline IoT para deteacción de anomalía en consumo de potencia
Este ejercicio guía al alumnado en la construcción de un pipeline completo de inteligencia artificial aplicado a IoT, cuyo objetivo es detectar anomalías en el consumo energético de un edificio de oficinas. 

A partir de un dataset histórico real, se realiza un análisis exploratorio, se identifican patrones anómalos, se preprocesan los datos y se entrena un modelo de detección basado en Isolation Forest. 

Luego, se simula el envío de datos en tiempo real a través de MQTT, y se implementa un sistema automático que, al detectar comportamientos anómalos, envía una alerta instantánea a un canal de Telegram. 

El ejercicio combina técnicas de ciencia de datos, automatización IoT y notificación inteligente, y está diseñado para ser replicable en contextos reales educativos o de gestión energética.
---

## 🔍 **Paso 1: Análisis Exploratorio de Datos (EDA)**

### 🧩 Suposición del dataset

Vamos a trabajar con un dataset que tiene una estructura similar a:

| dt           | potencia |
| ------------------- | ------------ |
| 2024-04-01 00:00:00 | 0.42         |
| 2024-04-01 00:15:00 | 0.38         |
| 2024-04-01 00:30:00 | 0.40         |
| ...                 | ...          |

Frecuencia: cada 15 minutos (puede ajustarse).

---

### 📊 1. Visualización inicial

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("consumo_potencia.csv", parse_dates=["dt"])
df.set_index("dt", inplace=True)

plt.figure(figsize=(12, 5))
df["potencia"].plot(title="Consumo energético")
plt.ylabel("kW")
plt.grid()
plt.show()
```

---

### 🧠 2. Tipos de anomalías frecuentes en consumo energético

| Tipo de anomalía                 | Descripción                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------ |
| 🔺 **Valores fuera de rango**    | picos inesperados muy por encima del valor típico. Ej: 10x el valor normal.    |
| 📉 **Caídas abruptas**           | valores casi nulos en horas donde debería haber actividad     |
| ⏰ **Actividad fuera de horario** | consumo alto durante la madrugada, cuando el edificio debería estar cerrada.     |
| 📈 **Tendencia inusual**         | consumo elevado sostenido que no corresponde con el patrón histórico.          |
| 🧍 **Lecturas repetidas**        | mismo valor constante durante mucho tiempo (sensor bloqueado o mal conectado). |
| 🕳 **Faltan datos (missing)**    | intervalos vacíos que pueden provocar errores en el modelo.                    |

---

### 📊 3. Estadísticas descriptivas y detección visual

```python
df.describe()
```

Luego puedes inspeccionar con:

```python
df["potencia"].plot(kind="hist", bins=50, title="Distribución del consumo")
```

Y un simple boxplot para ver outliers:

```python
df.boxplot(column="potencia", vert=False)
```

---

### 🔍 4. Ideas para detección manual de anomalías

* Si `potencia > Q3 + 1.5 * IQR` → posible pico anómalo
* Si `potencia < Q1 - 1.5 * IQR` → posible caída brusca
* Si `hora in [0, 4]` y `potencia > X` → actividad fuera de horario

Se ha implementado un notebook para realizar el análisis dispone en [m7_e5a_eda.](m7_e5a_eda.ipynb)

---

A continuación, preprocesaremos el dataset: detección y eliminación de valores nulos, normalización si es necesario y generación del dataset final para entrenamiento de un modelo de detección de anomalías.

## 🧽 **Paso 2: Limpieza y preprocesamiento**

### 📥 Suponemos un dataframe `df` con esta estructura:

```python
# Estructura típica
# dt, potencia

dt           potencia
2024-04-01 00:00    0.42
2024-04-01 00:15    0.38
...                ...
```

---

## ✅ 1. Eliminar valores nulos

```python
# Comprobar si hay nulos
print("Valores nulos:\n", df.isnull().sum())

# Eliminar filas con valores nulos
df_clean = df.dropna()
```

---

## ✅ 2. Visualizar la distribución antes de normalizar

```python
import matplotlib.pyplot as plt

df_clean["potencia"].hist(bins=50)
plt.title("Distribución de potencia antes de normalizar")
plt.xlabel("kW")
plt.show()
```

---

## ✅ 3. Normalización (opcional pero recomendable)

La mayoría de modelos de detección de anomalías requieren que los datos estén **escalados**. Usamos `MinMaxScaler` para llevar los valores a un rango \[0, 1].

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df_clean["potencia_norm"] = scaler.fit_transform(df_clean[["potencia"]])
```

✔️ Ahora `df_clean["potencia_norm"]` contiene la versión normalizada.

> 🔐 Guarda el scaler si quieres aplicar el mismo escalado a nuevos datos:

```python
import joblib
joblib.dump(scaler, "scaler_energia.pkl")
```

---

## ✅ 4. Resultado final

El dataframe listo para entrenamiento tiene esta forma:

| dt           | potencia | potencia\_norm |
| ------------------- | ------------ | ------------- |
| 2024-04-01 00:00:00 | 0.42         | 0.27          |
| 2024-04-01 00:15:00 | 0.38         | 0.22          |
| ...                 | ...          | ...           |

---

Vamos a entrenar un modelo de **detección de anomalías con Isolation Forest** usando el campo `potencia_norm` del dataset que ya preprocesamos.

---

## 🧠 Paso 3: Entrenamiento del modelo Isolation Forest

---

### ✅ 1. Preparar los datos

```python
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Usamos sólo la columna normalizada
X = df_clean[["potencia_norm"]]
```

---

### ✅ 2. Entrenar el modelo

```python
modelo = IsolationForest(contamination=0.01, random_state=42)
modelo.fit(X)
```

* `contamination=0.01`: estima que el 1% de los datos son anómalos.
* Puedes ajustar este valor según la sensibilidad deseada.

---

### ✅ 3. Añadir predicción al dataset

```python
df_clean["anomaly"] = modelo.predict(X)
```

* Resultado:

  * `-1` → Anomalía
  * `1` → Valor normal

---

### ✅ 4. Visualizar anomalías detectadas

```python
import matplotlib.pyplot as plt

df_clean["potencia"].plot(figsize=(12, 4), label="Consumo")
df_clean[df_clean["anomaly"] == -1]["potencia"].plot(
    style='ro', label="Anomalías"
)
plt.legend()
plt.title("Consumo energético y anomalías detectadas")
plt.show()
```

---

### ✅ 5. Guardar modelo para uso en tiempo real

```python
joblib.dump(modelo, "modelo_isolationforest.pkl")
```

Y también el scaler:

```python
joblib.dump(scaler, "scaler_energia.pkl")
```

---

### 📊 Resultado esperado

Visualmente podrás ver puntos rojos en momentos de consumo anómalo, típicamente:

* Durante la madrugada
* En picos de potencia fuera de rango
* En patrones que el modelo considera inusuales

---

Pasamos al **Paso 4: Simulación de lectura y envío de datos por MQTT cada 10 segundos** usando el dataset histórico que preprocesamos.

---

## 🚀 Paso 4: Simulación de datos históricos vía MQTT

El objetivo es simular una fuente de datos en tiempo real, publicando una lectura del dataset cada 10 segundos a un broker MQTT.

---

## 🛠️ Requisitos

* Broker MQTT en local (`localhost`) o público (`broker.hivemq.com`)
* Python con `paho-mqtt` y `pandas`

```bash
pip install paho-mqtt pandas
```

---

## 📄 Script: `simulador_envio_mqtt.py`

```python
import pandas as pd
import time
import json
import random
import paho.mqtt.client as mqtt
from datetime import datetime

# Cargar dataset
df = pd.read_csv("dataset_consumo_preprocesado.csv", parse_dates=["dt"])

# Configuración MQTT
broker = "localhost"  # o broker.hivemq.com si es público
port = 1883
topic = "ibbi/edificio/energia"

client = mqtt.Client()
client.connect(broker, port)
client.loop_start()

print("📡 Iniciando simulación de envío MQTT cada 10s...")

# Recorrer las filas del dataset
for _, fila in df.iterrows():
    payload = {
        "dt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # tiempo actual
        "potencia": fila["potencia"],
        "potencia_norm": fila["potencia_norm"]
    }
    mensaje = json.dumps(payload)
    client.publish(topic, mensaje)
    print("📤 Publicado:", mensaje)
    time.sleep(10)  # espera 10s

client.loop_stop()
client.disconnect()
```

---

## ✅ Resultado

Este script emite un mensaje JSON por MQTT como este cada 10 segundos:

```json
{
  "dt": "2025-05-07 19:20:30",
  "potencia": 0.42,
  "potencia_norm": 0.27
}
```

---

En este **Paso 5** vamos a construir el pipeline completo de detección en tiempo real:

> **Suscripción MQTT → Detección con modelo Isolation Forest → Notificación por Telegram**

---

## 🚀 Paso 5: Pipeline de detección + alerta Telegram

---

### 📂 Estructura de archivos esperada

Asegúrate de tener:

```bash
modelo_isolationforest.pkl     # modelo entrenado
scaler_energia.pkl             # escalador MinMax
.env                           # credenciales de Telegram
```

---

### 📄 `.env` (ya usado anteriormente)

```env
TELEGRAM_BOT_TOKEN=123456789:ABCdef...
TELEGRAM_CHAT_ID=987654321
```

---

## 🐍 `detector_mqtt_telegram.py` – Código completo

```python
import paho.mqtt.client as mqtt
import joblib
import json
import os
import requests
from dotenv import load_dotenv
import numpy as np
from datetime import datetime

# Cargar modelo y scaler
modelo = joblib.load("modelo_isolationforest.pkl")
scaler = joblib.load("scaler_energia.pkl")

# Cargar credenciales Telegram
load_dotenv()
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

# Función para enviar alerta
def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": mensaje}
    r = requests.post(url, json=data)
    print(f"📨 Alerta enviada a Telegram: {r.status_code}")

# Función de callback cuando llega un mensaje
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        potencia_norm = float(payload["potencia_norm"])
        ts = payload.get("dt", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Preprocesar y predecir
        X = np.array([[potencia_norm]])
        pred = modelo.predict(X)[0]  # -1 = anomalía

        if pred == -1:
            mensaje = (
                f"🚨 ANOMALÍA DETECTADA 🚨\n"
                f"🕒 {ts}\n"
                f"💡 Consumo normalizado: {potencia_norm:.2f}"
            )
            enviar_alerta(mensaje)
        else:
            print(f"✅ Normal | {ts} | {potencia_norm:.2f}")

    except Exception as e:
        print("❌ Error procesando mensaje:", e)

# Configurar cliente MQTT
broker = "localhost"  # o broker.hivemq.com
topic = "ibbi/edificio/energia"

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, 1883, 60)
client.subscribe(topic)

print(f"📡 Escuchando el topic '{topic}'...")

client.loop_forever()
```

---

## ✅ Resultado esperado

* Recibe un mensaje MQTT cada 10s desde el simulador.
* Si se detecta una anomalía → se envía **una alerta Telegram** con fecha y valor.

