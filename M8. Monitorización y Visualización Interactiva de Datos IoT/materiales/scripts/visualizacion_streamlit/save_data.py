import csv
import os
import json
import random
import ssl
import time
from paho.mqtt.client import Client, MQTTv311, CallbackAPIVersion
from dotenv import load_dotenv
from datetime import datetime, date

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# --- CONFIGURACIÓN ---
load_dotenv()

# Configuración de MQTT
mqtt_broker = os.getenv("MQTT_BROKER", "broker.hivemq.com")
mqtt_port = int(os.getenv("MQTT_PORT", 1883))
mqtt_user = os.getenv("MQTT_USER")
mqtt_pass = os.getenv("MQTT_PASS")
mqtt_topic = os.getenv("MQTT_TOPIC")

topics = ["ibbi/energia/cocina", 
          "ibbi/energia/pasteleria", 
          "ibbi/energia/cafeteria", 
          "ibbi/energia/zonaalta",
          "ibbi/energia/zonabaja",
          "ibbi/energia/zonamedia"]

# Create directory for CSV files
os.makedirs("data", exist_ok=True)

# Store the current day
current_day = date.today()

# Cache of fieldnames per topic
fieldnames_cache = {}

def rotate_files_if_needed():
    global current_day
    today = date.today()

    if today != current_day:
        print("🔄 New day detected, rotating log files...")
        for topic in topics:
            filename = topic.replace("/", "_") + ".csv"
            filepath = os.path.join(DATA_DIR, filename)
            if os.path.exists(filepath):
                backup_name = f"{filename.rstrip('.csv')}_{current_day.isoformat()}.csv"
                backup_path = os.path.join(DATA_DIR, backup_name)
                shutil.move(filepath, backup_path)
                print(f"📦 Saved backup: {backup_name}")
        current_day = today
        fieldnames_cache.clear()

def save_to_csv(topic, data):
    rotate_files_if_needed()

    filename = topic.replace("/", "_") + ".csv"
    filepath = os.path.join("tmp", filename)

    if not isinstance(data, dict):
        print(f"❌ Dato inválido topic {topic}: {data}")
        return

    data["timestamp"] = datetime.now().isoformat()
    write_header = not os.path.exists(filepath)

    with open(filepath, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(data)

# Callback al conectar
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conectado al broker MQTT")
    else:
        print(f"❌ Error al conectar. Código: {rc}")
    
    for topic in topics:
        client.subscribe(topic)
        print(f"Suscrito a {topic}")

def on_message(client, userdata, msg):
    try:
        message_data = json.loads(msg.payload.decode())
        # print(f"📥 {msg.topic}: {message_data}")
        save_to_csv(msg.topic, message_data)
    except json.JSONDecodeError:
        print(f"❌ Fallo al leer JSON en {msg.topic}")

# MQTT client setup
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
client.loop_forever()
