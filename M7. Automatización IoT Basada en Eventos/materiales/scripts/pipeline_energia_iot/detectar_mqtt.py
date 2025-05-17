import joblib
import json
import os
import requests
from dotenv import load_dotenv
import numpy as np
import time
import random
import ssl

from datetime import datetime
from paho.mqtt.client import Client, MQTTv311, CallbackAPIVersion

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# Cargar modelo y scaler
model = joblib.load(DIR_PATH+"/models/isolationforest.pkl")
# scaler = joblib.load(DIR_PATH+"/models/scaler.pkl")

load_dotenv()
# Cargar variables del archivo .env
mqtt_broker = os.getenv("MQTT_BROKER", "broker.hivemq.com")
mqtt_port = int(os.getenv("MQTT_PORT", 1883))
mqtt_user = os.getenv("MQTT_USER")
mqtt_pass = os.getenv("MQTT_PASS")

topic = "ibbi/edificio/energia"

print(mqtt_broker)
print(mqtt_port)
print(topic)

# Cargar credenciales Telegram
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

# Función para enviar alerta
def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": mensaje}
    r = requests.post(url, json=data)
    print(f"📨 Alerta enviada a Telegram: {r.status_code}")

# Callback para confirmar conexión
def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("✅ Conexión establecida con el broker MQTT")
    else:
        print(f"❌ Error al conectar. Código: {rc}")

# Función de callback cuando llega un mensaje
def on_message(client, userdata, msg):
    try:
        # Preprocesamiento
        payload = json.loads(msg.payload.decode())
        potencia_norm = float(payload["potencia_norm"])
        potencia = float(payload["potencia"])
        ts = payload.get("dt", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Modelo IA Predicción
        X = np.array([[potencia_norm]])
        pred = model.predict(X)[0]  # -1 = anomalía

        # Decisión
        if pred == -1:
            mensaje = (
                f"🚨 ANOMALÍA DETECTADA 🚨\n"
                f"🕒 {ts}\n"
                f"💡 Consumo normalizado: {potencia_norm:.2f}"
                f"💡 Consumo real: {potencia:.2f}"
            )
            # Acción
            enviar_alerta(mensaje)
        else:
            print(f"✅ Normal | {ts} | {potencia_norm:.2f}")

    except Exception as e:
        print("❌ Error procesando mensaje:", e)

# Configurar cliente MQTT
client = Client(client_id=f"ibbi-{random.randint(0, 10000)}", clean_session=True, protocol=MQTTv311, callback_api_version=CallbackAPIVersion.VERSION2)
client.username_pw_set(username=mqtt_user, password=mqtt_pass)
client.on_connect = on_connect
client.on_message = on_message
# Configuración TLS (opcional)
client.tls_set(cert_reqs=ssl.CERT_NONE)
# client.tls_insecure_set(True)  # ⚠️ Aceptar certificados sin verificar (solo para pruebas)
# Conectar al broker
print("Conectando al broker MQTT...")
client.connect(mqtt_broker, mqtt_port)
time.sleep(10)  # Esperar unos segundos para asegurar la conexión

print(f"📡 Escuchando el topic '{topic}'...")
client.subscribe(topic)
client.loop_forever()