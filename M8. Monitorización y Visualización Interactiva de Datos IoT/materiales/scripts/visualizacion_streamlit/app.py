
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import random
import ssl
import time
import json
import threading
import requests

from datetime import datetime
from collections import deque
from paho.mqtt.client import Client, MQTTv311, CallbackAPIVersion
from dotenv import load_dotenv

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# --- CONFIGURACIÓN ---
load_dotenv()

# Configuración de MQTT
mqtt_broker = os.getenv("MQTT_BROKER", "broker.hivemq.com")
mqtt_port = int(os.getenv("MQTT_PORT", 1883))
mqtt_user = os.getenv("MQTT_USER")
mqtt_pass = os.getenv("MQTT_PASS")
mqtt_topic = os.getenv("MQTT_TOPIC")

# Obtener token de ThingsBoard
tmp_folder = os.path.join(DIR_PATH, "tmp")
if not os.path.exists(tmp_folder):
    os.makedirs(tmp_folder)

token_file = os.path.join(DIR_PATH, "tmp", "token.txt")
if os.path.exists(token_file):
    with open(token_file, "r") as f:
        token = f.read().strip()
else:
    print("❌ No se encontró el token. Asegúrate de haberlo generado previamente.")
    exit()

device_names = ["cocina", "pasteleria", "cafeteria"]
if "datos_mqtt" not in st.session_state:
    mqtt_data = {
        name: {
            "values": deque(maxlen=50),
            "last_ts": 0,
            "fuente": "MQTT"  # o "API"
        } for name in device_names
    }
    st.session_state["datos_mqtt"] = mqtt_data

mqtt_data = st.session_state["datos_mqtt"]

# --- ThingsBoard REST ---
def leer_desde_api(device, token):
    url = f"https://thingsboard.url/api/plugins/telemetry/DEVICE/{device}/values/timeseries?keys=potencia"
    headers = {"X-Authorization": f"Bearer {token}"}
    try:
        r = requests.get(url, headers=headers, timeout=2)
        if r.status_code == 200:
            data = r.json()
            valor = float(data["potencia"][0]["value"])
            ts = int(data["potencia"][0]["ts"])
            mqtt_data[device]["values"].append({
                                                "ts": datetime.now(),
                                                "valor": potencia
                                            })
            mqtt_data[device]["last_ts"] = time.time()
            mqtt_data[device]["fuente"] = "API"
    except Exception as e:
        print(f"Error en API para {device}: {e}")

# --- MQTT SETUP ---
# Inicializar conexión MQTT
def iniciar_mqtt():
    if "mqtt_thread" not in st.session_state:
        def mqtt_loop():
            try:
                client_id = f"ibbi-{random.randint(0, 10000)}"
                # print(client_id, mqtt_user, mqtt_pass, mqtt_broker, mqtt_port, mqtt_topic)
                # Crear cliente con versión moderna del API
                client = Client(
                    client_id=client_id,
                    clean_session=True,
                    protocol=MQTTv311,
                    callback_api_version=CallbackAPIVersion.VERSION2
                )
                client.on_connect = on_connect
                client.on_message = on_message
                client.username_pw_set(username=mqtt_user, password=mqtt_pass)
                # Configuración TLS (opcional)
                client.tls_set(cert_reqs=ssl.CERT_NONE)
                # Conectar al broker
                print("🟡 Conectando al broker MQTT...")
                client.connect(mqtt_broker, mqtt_port)
                time.sleep(1)  # Esperar unos segundos para asegurar la conexión
                client.subscribe(mqtt_topic)
                client.loop_forever()
            except Exception as e:
                print(f"Error al conectar al broker MQTT: {e}")
                return
            
        t = threading.Thread(target=mqtt_loop, daemon=True)
        t.start()
        st.session_state["mqtt_thread"] = t  

# Callback al conectar
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado al broker MQTT")
    else:
        print(f"❌ Error al conectar. Código: {rc}")

# Callback al recibir un mensaje
def on_message(client, userdata, msg):
    global mqtt_data
    device = msg.topic.split("/")[-1]
    if device in mqtt_data:
        try:
            payload = json.loads(msg.payload.decode())
            # Formato de datos esperado (TB)
            # potencia = float(payload["potencia"][0]["value"])
            # ts = int(payload["potencia"][0]["ts"])
            potencia = float(payload["p_total"])
            mqtt_data[device]["values"].append({
                                                "ts": datetime.now(),
                                                "valor": potencia
                                            })
            mqtt_data[device]["last_ts"] = time.time()
        except Exception as e:
            print(f"Error en lectura MQTT: {e}")


# --- INICIO MQTT (en segundo plano) ---
iniciar_mqtt()

# --- INTERFAZ STREAMLIT ---
st.set_page_config(layout="wide")
st.title("Monitor de Energía - iBBi")

now_ts = time.time()
# Visualización por device
st.subheader("📊 Datos de potencia en tiempo real")
for device_name in device_names:
    st.markdown(f"### {device_name.capitalize()}")
    ts = mqtt_data[device_name]["last_ts"]
    last_dt = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    delta = now_ts - ts
    if delta < 15:
        estado = "🟢 ACTIVO"
    elif delta < 30:
        estado = "🟡 RETRASADO"
    else:
        estado = "🔴 DESCONECTADO"
    datos = list(mqtt_data[device_name]["values"])
    if datos:
        df = pd.DataFrame(datos)
        # Calcular media y límites
        media = df["valor"].mean()
        min_threshold = media * 0.50
        max_threshold = media * 1.50
        # Añadir valores
        fig = px.line(df, x="ts", y="valor", labels={"ts": "Hora", "valor": "Potencia (kW)"})
        fig.update_layout(xaxis=dict(tickformat="%H:%M:%S"))
        # Añadir líneas de referencia
        fig.add_hline(y=media, line_dash="dot", line_color="cyan", annotation_text="Media", annotation_position="top left")
        fig.add_hline(y=min_threshold, line_dash="dash", line_color="orange", annotation_text="-50%", annotation_position="bottom left")
        fig.add_hline(y=max_threshold, line_dash="dash", line_color="orange", annotation_text="+50%", annotation_position="top left")

        col1, col2 = st.columns([3, 1])
        with col1:
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.metric(label=device_name.upper(), value=estado, delta=f"{int(delta)} s")
            col3, col4 = st.columns([1, 1])
            with col3:
                st.metric("Último valor", f"{df['valor'].iloc[-1]:.2f} kW")
                st.metric("Media", f"{df['valor'].mean():.2f} kW")
            with col4:
                st.metric("Máximo", f"{df['valor'].max():.2f} kW")
                st.metric("Mínimo", f"{df['valor'].min():.2f} kW")

        # Comprobar si hay anomalías (siempre que haya al menos 10 valores registrados)
        if delta < 10 and df["valor"].iloc[-1] < min_threshold or df["valor"].iloc[-1] > max_threshold:
            st.toast(f"{last_dt} Anomalía detectada en {device_name}!", icon="🚨")
            print(f"🚨 Anomalía detectada en {device_name} ({last_dt})")
            # Aquí puedes añadir lógica para enviar alertas o notificaciones
    else:
        st.info("Sin datos disponibles aún.")

# Refresco automático
time.sleep(5)
st.rerun()