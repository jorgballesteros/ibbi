# Telegram Bot

## ✅ Objetivo

Usar un bot de Telegram para recibir notificaciones cuando se detecte un evento, por ejemplo: *“Alerta: caudal excesivo detectado”*.

---

## 🧩 PASOS COMPLETOS

---

### 1. 🤖 Crear un bot en Telegram

1. Abre Telegram y busca el bot: `@BotFather`
2. Escribe: `/newbot`
3. Te pedirá:

   * Nombre del bot
   * Nombre de usuario del bot (debe terminar en `bot`)
4. Te devolverá un **token de acceso**, algo como:

```
123456789:ABCdefGhIjKlmNoPQRstuVwxyz1234567890
```

🔐 **Guárdalo en tu `.env`**:

```env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGh...
```

---

### 2. Obtén tu `chat_id`

1. Envíale un mensaje a tu bot (búscalo por su @username y escribe algo).
2. Ve a esta URL en el navegador (reemplaza `<TOKEN>` con el tuyo):

```
https://api.telegram.org/bot<TOKEN>/getUpdates
```

3. En la respuesta JSON, busca el campo:

```json
"chat": {
  "id": 987654321,
  ...
}
```

✅ Ese número es tu `chat_id`.

Guárdalo también en `.env`:

```env
TELEGRAM_CHAT_ID=987654321
```

---

### 3. 🧪 Enviar mensaje desde Python

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensaje
    }
    response = requests.post(url, json=payload)
    print(f"Telegram: {response.status_code}")
```

---

### 4. 🔁 Integrar con el detector de eventos

Modifica el código del **Ejercicio 2** para llamar a `enviar_alerta(...)`:

```python
# Después de detectar evento
mensaje = f"🚨 CAUDAL EXCESIVO 🚨\n" \
          f"Hora: {timestamp}\n" \
          f"Sensor: {evento['sensor_id']}\n" \
          f"Caudal: {caudal} L/min (umbral: {threshold})"

enviar_alerta(mensaje)
```

---

### ✅ Resultado

Cada vez que se detecte un caudal superior al umbral, recibirás un mensaje de Telegram en tu móvil con el detalle.
