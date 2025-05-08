# Alternativas de webhooks

## 🌐 **1. IFTTT (If This Then That)**

### 🧩 ¿Qué permite?

* Conectar sensores o scripts con servicios como **Gmail, Google Sheets, Telegram, Discord, Alexa, etc.**
* Enviar correos, notificaciones, activar dispositivos inteligentes.

### 🔧 Ejemplo:

Tu script de Python llama a un **webhook de IFTTT**, que activa una acción como:

* Enviar un correo
* Registrar datos en Google Sheets
* Encender una lámpara inteligente

### 🛠 Cómo usar:

1. Crea una cuenta en [https://ifttt.com](https://ifttt.com)
2. Crea una applet del tipo “**Webhooks → Gmail**” (u otro)
3. Obtén tu URL de webhook en:

   ```
   https://maker.ifttt.com/trigger/{event_name}/json/with/key/{your_key}
   ```

---

## ⚙️ **2. Zapier**

### 🧩 ¿Qué permite?

* Automatizar flujos complejos entre cientos de servicios: Slack, Gmail, Trello, Airtable...
* Usar filtros, delays y transformaciones intermedias.

### 🛠 Cómo usar:

* Crea una cuenta en [https://zapier.com](https://zapier.com)
* Activa el trigger "Webhook → Zap"
* En tu script, haz un `POST` al webhook de Zapier con los datos

---

## 💬 **3. Discord Webhooks**

### 🧩 ¿Qué permite?

* Enviar mensajes a un canal de Discord (como si fuera un bot) sin autenticar usuario.
* Perfecto para grupos de trabajo o formación.

### 🛠 Cómo usar:

1. Crea un canal en tu servidor Discord
2. Activa “**Integraciones → Webhooks**” y crea uno
3. Copia la URL del webhook y úsala en tu script:

```python
requests.post(discord_webhook_url, json={"content": "⚠️ Caudal excesivo detectado"})
```

---

## 📊 **4. Google Sheets vía App Script + Webhook**

### 🧩 ¿Qué permite?

* Crear una hoja de cálculo que **recibe datos automáticamente desde tu script**.

### 🛠 Cómo usar:

1. Abre una hoja de Google
2. Abre `Extensiones → Apps Script`
3. Escribe un endpoint `doPost(e)` que reciba y guarde datos
4. Publica como "Web App"
5. Usa la URL en tu script con `requests.post(...)`

---

## 🖥 **5. Webhook.site**

### 🧩 ¿Qué permite?

* Visualizar mensajes webhook en tiempo real.
* Ideal para **probar y depurar** antes de enviar a un sistema real.

---

## 📦 ¿Quieres algo más robusto?

### 🧠 **6. Home Assistant (self-hosted)**

Sistema domótico completo, ideal para controlar dispositivos físicos en red local (válvulas, luces, etc.), con soporte para webhooks y MQTT.

---

¿Quieres que prepare una tabla comparativa con estas opciones para entregar al alumnado o para incluir en la guía del módulo 7?
