import random
import ssl
import json
import time
import os
import requests

from paho.mqtt.client import Client, MQTTv311, CallbackAPIVersion
from dotenv import load_dotenv

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
# Cargar variables de entorno
load_dotenv()

def leer_telemetria(key="p_total"):
    # Configuración de ThingsBoard
    tb_url = os.getenv("TB_API_URL")
    device_id = os.getenv("TB_DEVICE_ID")
    url = f"{tb_url}/api/plugins/telemetry/DEVICE/{device_id}/values/timeseries?limit=1&keys=p_total"

    headers = {
        "X-Authorization": f"Bearer {token}"
    }
    # print(headers)
    # Procesar la respuesta
    response = requests.get(url, headers=headers)
    data = response.json()
    print("📡 Telemetría recibida:", data)
    return data

# Obtener token de ThingsBoard
token_file = os.path.join(DIR_PATH, "tmp", "token.txt")
if os.path.exists(token_file):
    with open(token_file, "r") as f:
        token = f.read().strip()
else:
    print("❌ No se encontró el token. Asegúrate de haberlo generado previamente.")
    exit()

# Configuración de MQTT
mqtt_broker = os.getenv("MQTT_BROKER", "broker.hivemq.com")
mqtt_port = int(os.getenv("MQTT_PORT", 1883))
mqtt_user = os.getenv("MQTT_USER")
mqtt_pass = os.getenv("MQTT_PASS")
mqtt_topic = os.getenv("MQTT_TOPIC")

# Callback al conectar
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado al broker MQTT")
    else:
        print(f"❌ Error al conectar. Código: {rc}")

client_id = f"ibbi-{random.randint(0, 10000)}"

# Crear cliente con versión moderna del API
client = Client(
    client_id=client_id,
    clean_session=True,
    protocol=MQTTv311,
    callback_api_version=CallbackAPIVersion.VERSION2
)
client.on_connect = on_connect
client.username_pw_set(username=mqtt_user, password=mqtt_pass)
# Configuración TLS (opcional)
client.tls_set(cert_reqs=ssl.CERT_NONE)
# Conectar al broker
print("Conectando al broker MQTT...")
client.connect(mqtt_broker, mqtt_port)
time.sleep(10)  # Esperar unos segundos para asegurar la conexión

try:
    client.loop_start()

    # Publicar datos periódicamente
    while True:
        # Generar datos aleatorios (opcional)
        # ts = round(time.time() * 1000)
        # payload = {'p_total': [{'ts': ts, 'value': round(random.uniform(5.0, 15.0), 2)}]}
        
        # Leer telemetría de ThingsBoard
        payload = leer_telemetria()

        client.publish(mqtt_topic, json.dumps(payload))
        print("📤 Publicado:", payload)
        time.sleep(5)

except KeyboardInterrupt:
    print("Desconectando...")
    client.disconnect()
    client.loop_stop()
