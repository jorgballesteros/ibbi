import random
import json
import time
import os
import ssl

from dotenv import load_dotenv
from collections import deque
from subprocess import run
from paho.mqtt.client import Client, MQTTv311, CallbackAPIVersion

load_dotenv()

# Cargar variables del archivo .env
mqtt_broker = os.getenv("MQTT_BROKER")
mqtt_port = int(os.getenv("MQTT_PORT"))
mqtt_user = os.getenv("MQTT_USER")
mqtt_pass = os.getenv("MQTT_PASS")
mqtt_topic = os.getenv("MQTT_TOPIC")

# Configuración del buffer
buffer_size = 10
buffer = deque(maxlen=buffer_size)

# Configuración de la alarma
umbral = 0.25
alert_script = "publicar_alarma.py"

# Callback al conectar
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado al broker MQTT")
    else:
        print(f"❌ Error al conectar. Código: {rc}")

# Callback al recibir un mensaje
def on_message(client, userdata, msg):
    global buffer

    data = json.loads(msg.payload.decode())

    try:
        potencia = float(data['p_total'][0]['value'])
        buffer.append(potencia)

        print(f"⚡ Potencia recibida: {potencia} | buffer={len(buffer)}")

        if len(buffer) == buffer_size:
            # Calcular el rango esperado  
            media = sum(buffer) / len(buffer)
            lower = media * (1-umbral)
            upper = media * (1+umbral)

            print(f"📏 Rango esperado: [{lower:.2f} - {upper:.2f}]")

            # Comprobar si la potencia está fuera del rango esperado
            if potencia < lower or potencia > upper:
                print("🚨 Anomalía detectada, enviando alarma...")
                run(["python", alert_script, str(potencia)])

    except Exception as e:
        print("❌ Error al procesar mensaje:", e)

# Crear id de cliente único
client_id = f"ibbi-{random.randint(0, 10000)}"

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
print("Conectando al broker MQTT...")
client.connect(mqtt_broker, mqtt_port)
time.sleep(10)  # Esperar unos segundos para asegurar la conexión
# Iniciar el loop
client.subscribe(mqtt_topic)
client.loop_forever()
