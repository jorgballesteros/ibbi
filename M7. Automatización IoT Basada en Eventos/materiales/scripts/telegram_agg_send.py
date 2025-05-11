import time
import os
import random
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

# Configuración
umbral = 15
intervalo_agrupacion = 30  # 5 minutos
alertas_pendientes = []
ultimo_envio = time.time()

def enviar_alerta_telegram(mensaje):
    # Función para enviar mensaje a Telegram
    # Implementa aquí la lógica para enviar el mensaje utilizando tu bot
    print(f"Enviando alerta:\n{mensaje}")
    
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

while True:
    caudal = round(random.uniform(0, 20), 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if caudal > umbral:
        alerta = f"🚨 {timestamp} | Caudal: {caudal} L/min"
        print(alerta)
        alertas_pendientes.append(alerta)

    # Verificar si es momento de enviar alertas agrupadas
    if time.time() - ultimo_envio >= intervalo_agrupacion and alertas_pendientes:
        mensaje = "🔔 Alertas de caudal excesivo:\n" + "\n".join(alertas_pendientes)
        enviar_alerta_telegram(mensaje)
        alertas_pendientes.clear()
        ultimo_envio = time.time()

    time.sleep(1)