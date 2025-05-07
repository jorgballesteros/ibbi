from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Leer usuario y contraseña
mqtt_broker = os.getenv("MQTT_BROKER")
mqtt_port = int(os.getenv("MQTT_PORT"))
mqtt_user = os.getenv("MQTT_USER")
mqtt_pass = os.getenv("MQTT_PASS")

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Conectado con código:", rc)
    client_sub.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()} en el tema {msg.topic}")

client_sub = mqtt.Client(protocol=mqtt.MQTTv311)
client_sub.username_pw_set(username=mqtt_user, password=mqtt_pass)
client_sub.on_connect = on_connect
client_sub.on_message = on_message

client_sub.connect(mqtt_broker, mqtt_port, 60)
client_sub.loop_forever()
