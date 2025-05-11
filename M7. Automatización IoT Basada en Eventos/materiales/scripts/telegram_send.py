import random
import os
import requests
import time

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

# print(bot_token)
# print(chat_id)

def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensaje
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("📤 Mensaje enviado correctamente")
    else:
        print("❌ Error al enviar el mensaje")
        print(f"Error: {response.text}")

threshold = 15.0  # Ejemplo de umbral

while True:
    caudal = round(random.uniform(0, 20), 2)
    print(f"Caudal simulado: {caudal} L/min")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    evento = {
        "sensor_id": "sensor-agua-01",
        "caudal_L_min":caudal  # Ejemplo de caudal
    }

    if caudal > threshold:
        # Después de detectar evento
        mensaje = f"🚨 CAUDAL EXCESIVO 🚨\n" \
            f"Hora: {timestamp}\n" \
            f"Sensor: {evento['sensor_id']}\n" \
            f"Caudal: {caudal} L/min (umbral: {threshold})"
        enviar_alerta(mensaje)
    else:
        print("✅ Caudal dentro de los límites")
    time.sleep(10)