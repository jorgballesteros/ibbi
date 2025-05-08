import random
from dotenv import load_dotenv
import os

import paho.mqtt.client as mqtt

# Cargar variables del archivo .env
load_dotenv()

# Leer usuario y contraseña
mqtt_broker = os.getenv("MQTT_BROKER")
mqtt_port = int(os.getenv("MQTT_PORT"))
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
        client.subscribe(topic)  # Suscripción al topic concreto
    else:
        print(f"❌ Error al conectar. Código: {rc}")

def on_message(client, userdata, msg):
    print(f"📥 Mensaje recibido: {msg.payload.decode()} en el tema {msg.topic}")

client_id = f"ibbi-{random.randint(0, 10000)}"

client_sub = mqtt.Client(client_id=client_id, clean_session=True, protocol=mqtt.MQTTv311)
client_sub.username_pw_set(username=mqtt_user, password=mqtt_pass)
client_sub.on_connect = on_connect
client_sub.on_message = on_message

client_sub.connect(mqtt_broker, mqtt_port, 60)

try:
    client_sub.loop_forever()

except KeyboardInterrupt:
    print("Desconectando...")
    client_sub.disconnect()
    client_sub.loop_stop()
