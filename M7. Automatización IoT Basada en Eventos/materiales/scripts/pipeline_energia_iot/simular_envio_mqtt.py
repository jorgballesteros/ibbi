import pandas as pd
import time
import json
import random
import ssl
import os

from datetime import datetime

from dotenv import load_dotenv
from paho.mqtt.client import Client, MQTTv311, CallbackAPIVersion

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# Callback para confirmar conexión
def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("✅ Conexión establecida con el broker MQTT")
    else:
        print(f"❌ Error al conectar. Código: {rc}")

# Cargar variables del archivo .env
load_dotenv()

# Configuración
mqtt_broker = os.getenv("MQTT_BROKER", "broker.hivemq.com")
mqtt_port = int(os.getenv("MQTT_PORT", 1883))
mqtt_user = os.getenv("MQTT_USER")
mqtt_pass = os.getenv("MQTT_PASS")

topic = "ibbi/edificio/energia"

print(mqtt_broker)
print(mqtt_port)
print(topic)

# Cargar dataset
df = pd.read_csv(DIR_PATH+"/data/consumo_potencia_min_limpio.csv", parse_dates=["dt"])

# Opcional: Enviar a partir de una fecha específica
# df = df[df["dt"] >= "2025-05-05 04:50:00"]

print(df.head())

client = Client(client_id=f"ibbi-{random.randint(0, 10000)}", clean_session=True, protocol=MQTTv311, callback_api_version=CallbackAPIVersion.VERSION2)
client.username_pw_set(username=mqtt_user, password=mqtt_pass)
client.on_connect = on_connect
# Configuración TLS (opcional)
client.tls_set(cert_reqs=ssl.CERT_NONE)
# client.tls_insecure_set(True)  # ⚠️ Aceptar certificados sin verificar (solo para pruebas)
# Conectar al broker
print("Conectando al broker MQTT...")
client.connect(mqtt_broker, mqtt_port)
time.sleep(10)  # Esperar unos segundos para asegurar la conexión

try:
    client.loop_start()

    print("📡 Iniciando simulación de envío MQTT cada 10s...")

    # Recorrer las filas del dataset
    for _, fila in df.iterrows():
        payload = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # tiempo actual
            "dt": fila["dt"], # marca de tiempo del dataset
            "potencia": fila["potencia"],
            "potencia_norm": fila["potencia_norm"]
        }
        mensaje = json.dumps(payload)
        client.publish(topic, mensaje)
        print("📤 Publicado:", mensaje)
        time.sleep(5)  # espera 5s

except KeyboardInterrupt:
    print("Desconectando...")
    client.disconnect()
    client.loop_stop()
