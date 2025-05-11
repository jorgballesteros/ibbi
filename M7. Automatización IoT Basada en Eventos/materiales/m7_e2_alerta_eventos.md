# 🧪 Ejercicio 2 – *Alerta por Telegram ante evento de caudal excesivo*

---

## 🎯 Objetivo

Simular la lectura periódica de caudal de agua y, cuando el valor supere un umbral definido, **enviar una alerta automática mediante un bot de Telegram**.

---

# 📄 `.env` — Configuración de entorno

```env
THRESHOLD=12.0

TELEGRAM_BOT_TOKEN=123456789:ABCdefGhIjKlmNoPQRstuVwxyz1234567890
TELEGRAM_CHAT_ID=987654321
```

---

# 🐍 `alerta_telegram.py` — Código fuente

```python
import os
import time
import json
import random
import requests
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables del entorno
load_dotenv()

# Parámetros desde .env
threshold = float(os.getenv("THRESHOLD", 12.0))
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

# Función para enviar alerta a Telegram
def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensaje
    }
    response = requests.post(url, json=payload)
    print(f"📨 Telegram → {response.status_code} | {mensaje}")

# Bucle de simulación
print("🚿 Iniciando monitor de caudal...")

try:
    while True:
        caudal = round(random.uniform(0, 20), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if caudal > threshold:
            mensaje = (
                f"🚨 *ALERTA DE CAUDAL EXCESIVO*\n"
                f"🕒 {timestamp}\n"
                f"💧 Sensor: contador-agua-01\n"
                f"📈 Caudal: {caudal} L/min\n"
                f"🔺 Umbral: {threshold} L/min"
            )
            enviar_alerta(mensaje)
        else:
            print(f"✅ {timestamp} | Caudal normal: {caudal} L/min")
        
        time.sleep(5)

except KeyboardInterrupt:
    print("\n⛔ Monitor detenido por el usuario.")
```

---

# ✅ Resultado esperado

En consola:

```bash
✅ 2025-05-07 17:45:00 | Caudal normal: 10.43 L/min
📨 Telegram → 200 | 🚨 ALERTA DE CAUDAL EXCESIVO...
```

En tu móvil (Telegram):

```
🚨 ALERTA DE CAUDAL EXCESIVO
🕒 2025-05-07 17:46:12
💧 Sensor: contador-agua-01
📈 Caudal: 14.78 L/min
🔺 Umbral: 12.0 L/min
```

---

Se ha implementado un script ejecutable y automatizable en la carpeta [scripts](scripts/telegram_send.py).

# 🧩 Extensiones opcionales

* Añadir imagen o botón al mensaje.
* Agrupar alertas si ocurren muchas seguidas.
* Añadir un sistema de “reintentos” si falla Telegram.