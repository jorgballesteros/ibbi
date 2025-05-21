# Ejercicio 2: Visualización avnazada y monitorización de conectividad con Streamlit

## Introducción: ¿Qué es Streamlit?

**Streamlit** es un framework en Python que permite crear **interfaces web interactivas** para análisis de datos, dashboards y prototipos de forma muy rápida y sencilla. Está orientado a usuarios de Python que no tienen experiencia en desarrollo web.

### Ventajas

* Muy fácil de usar: similar a escribir un script de análisis en Jupyter.
* Interactivo y en tiempo real.
* No requiere conocimientos de HTML, CSS o JS.
* Ideal para prototipos rápidos y visualización de datos en entornos de IoT y ciencia de datos.

### Limitaciones

* No está diseñado para sistemas web complejos o multiusuario.
* No tiene control avanzado de autenticación (aunque se puede integrar).
* Rendimiento limitado si hay muchos usuarios simultáneos.

### Aprender más
En este enlace podrás consultar un programa de formación streamlit. Está dividio en pequeñas sesiones par completarlo en 30 días. [30 Días de Streamlit](https://30days.streamlit.app/)
---

## Explicación paso a paso

### Importación de librerías y configuración

```python
import streamlit as st
import time
import json
import threading
import paho.mqtt.client as mqtt
import requests
from collections import deque

DISPOSITIVOS = ["cocina", "pasteleria", "cafeteria"]
```

**¿Qué hace esto?**

* Carga las librerías necesarias:

  * `paho.mqtt.client` para conexión MQTT
  * `requests` para consultar la API REST de ThingsBoard
  * `streamlit` para construir la interfaz
  * `deque` para almacenar los últimos 10 valores por dispositivo

---

### Estructura de datos para almacenar estados

```python
datos_dispositivos = {
    nombre: {
        "valores": deque(maxlen=10),
        "ultimo_ts": 0,
        "fuente": "MQTT"
    } for nombre in DISPOSITIVOS
}
```
 
**¿Qué hace esto?**

* Crea una estructura que guarda los últimos 10 valores (`deque`) y el timestamp del último mensaje recibido por dispositivo.

---

### Cliente MQTT para recepción de datos

```python
def on_message(client, userdata, msg):
    dispositivo = msg.topic.split("/")[-1]
    if dispositivo in datos_dispositivos:
        payload = json.loads(msg.payload.decode())
        potencia = float(payload["potencia"][0]["value"])
        datos_dispositivos[dispositivo]["valores"].append(potencia)
        datos_dispositivos[dispositivo]["ultimo_ts"] = time.time()

def iniciar_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("mqtt.broker.url", 1883)
    client.subscribe("ibbi/energia/+")
    client.loop_start()
```

**¿Qué hace esto?**

* Escucha mensajes de MQTT en los tópicos `ibbi/energia/dispositivo`.
* Extrae la potencia y la guarda junto al timestamp actual.

---

### Función para consultar datos desde ThingsBoard por REST

```python
def leer_desde_api(dispositivo, token):
    url = f"https://thingsboard.url/api/plugins/telemetry/DEVICE/{dispositivo}/values/timeseries?keys=potencia"
    headers = {"X-Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers, timeout=2)
    if r.status_code == 200:
        data = r.json()
        valor = float(data["potencia"][0]["value"])
        datos_dispositivos[dispositivo]["valores"].append(valor)
        datos_dispositivos[dispositivo]["ultimo_ts"] = time.time()
        datos_dispositivos[dispositivo]["fuente"] = "API"
```

**¿Qué hace esto?**

* Realiza una consulta HTTP GET a la API de ThingsBoard.
* Extrae el valor más reciente de potencia del dispositivo y lo almacena.

---

### 5Inicio del cliente MQTT en un hilo en segundo plano

```python
threading.Thread(target=iniciar_mqtt, daemon=True).start()
```

**¿Qué hace esto?**

* Ejecuta el cliente MQTT sin bloquear la ejecución de Streamlit.

---

### Interfaz Streamlit: conectividad de los dispositivos

```python
st.set_page_config(layout="wide")
st.title("📡 Monitor de Energía - Dispositivos IoT")

modo_api = st.sidebar.checkbox("Usar API de ThingsBoard")
api_token = st.sidebar.text_input("Token de acceso API", type="password")

if modo_api and api_token:
    for disp in DISPOSITIVOS:
        leer_desde_api(disp, api_token)

st.subheader("🔌 Estado de conectividad")
cols = st.columns(len(DISPOSITIVOS))
ahora = time.time()
for i, disp in enumerate(DISPOSITIVOS):
    ts = datos_dispositivos[disp]["ultimo_ts"]
    delta = ahora - ts
    if delta < 10:
        estado = "🟢 ACTIVO"
    elif delta < 30:
        estado = "🟡 RETRASADO"
    else:
        estado = "🔴 DESCONECTADO"
    cols[i].metric(label=disp.upper(), value=estado, delta=f\"{int(delta)} s\")
```

📌 **¿Qué hace esto?**

* Añade controles para cambiar entre adquisición MQTT o REST.
* Muestra una métrica de estado por cada dispositivo en base al tiempo transcurrido desde el último mensaje.

---

### Visualización de datos: gráficos y estadísticas

```python
st.subheader("📊 Datos de energía en tiempo real")
for disp in DISPOSITIVOS:
    st.markdown(f"### {disp.capitalize()}")
    datos = list(datos_dispositivos[disp]["valores"])
    if datos:
        col1, col2 = st.columns([2, 1])
        col1.line_chart(datos)
        col2.metric("Último valor", f"{datos[-1]} W")
        col2.metric("Media", f"{sum(datos)/len(datos):.2f} W")
        col2.metric("Máximo", f"{max(datos):.2f} W")
        col2.metric("Mínimo", f"{min(datos):.2f} W")
    else:
        st.info("Sin datos disponibles aún.")
```

**¿Qué hace esto?**

* Para cada dispositivo:

  * Muestra un gráfico de líneas con los últimos 10 valores
  * Presenta los valores estadísticos clave

---

### Refresco automático del dashboard

```python
time.sleep(2)
st.experimental_rerun()
```

**¿Qué hace esto?**

* Refresca automáticamente la interfaz cada 2 segundos para mostrar los datos en tiempo real.

---

## 💡 Otras visualizaciones útiles que podrías añadir

| Visualización                         | Tipo                          | Descripción                                             |
| ------------------------------------- | ----------------------------- | ------------------------------------------------------- |
| Mapa de calor                         | `st.pyplot` + seaborn         | Para mostrar intensidad de consumo por horas/días       |
| Gráfico de barras por zonas           | `st.bar_chart`                | Comparar consumo entre áreas del edificio               |
| Indicador circular estilo velocímetro | `plotly.graph_objects`        | Para representar potencia instantánea en estilo “gauge” |
| Línea con bandas de confianza         | `plotly.line` + media ±25%    | Para ver si valores están dentro de un rango tolerable  |
| Alerta visual tipo tarjeta            | `st.warning()` o `st.error()` | Mostrar anomalías con contexto textual cuando ocurren   |