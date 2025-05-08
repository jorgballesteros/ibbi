import time
import os
import json
import random

from dotenv import load_dotenv
from paho.mqtt.client import Client, MQTTv311, CallbackAPIVersion

# Cargar variables del archivo .env
load_dotenv()

# Configuración
mqtt_broker = os.getenv("MQTT_BROKER", "broker.hivemq.com")
mqtt_port = int(os.getenv("MQTT_PORT", 1883))
mqtt_user = os.getenv("MQTT_USER")
mqtt_pass = os.getenv("MQTT_PASS")

topic = "ibbi/agua"

print(mqtt_broker)
print(mqtt_port)
print(mqtt_user)
print(mqtt_pass)
print(topic)


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
    protocol=MQTTv311
)
client.on_connect = on_connect

# Conectar al broker y arrancar loop
client.connect(mqtt_broker, mqtt_port)
time.sleep(5)  # Esperar un segundo para asegurar la conexión
try:
    client.loop_start()

    # Publicar datos periódicamente
    while True:
        payload = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "sensor_id": "sensor-agua-01",
            "caudal_L_min": round(random.uniform(5.0, 15.0), 2)
        }
        client.publish(topic, json.dumps(payload))
        print("📤 Publicado:", payload)
        time.sleep(5)
except KeyboardInterrupt:
    print("Desconectando...")
    client.disconnect()
    client.loop_stop()