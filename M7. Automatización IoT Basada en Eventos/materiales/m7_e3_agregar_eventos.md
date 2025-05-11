# Ejercicio 3. Agrupación de eventos

## 🧩 Objetivo

Agrupar múltiples alertas en un solo mensaje si ocurren dentro de un intervalo de tiempo definido (por ejemplo, 10 minutos), en lugar de enviar una notificación por cada evento detectado.

---

## 🛠️ Implementación en Python

A continuación, se presenta una estrategia utilizando Python para agrupar alertas:

1. **Variables de control:**

   * `alertas_pendientes`: lista para almacenar las alertas detectadas.
   * `ultimo_envio`: marca de tiempo del último envío de alertas.
   * `intervalo_agrupacion`: tiempo en segundos para agrupar alertas (por ejemplo, 600 segundos para 10 minutos).

2. **Lógica de agrupación:**

   * Cada vez que se detecta una alerta, se agrega a `alertas_pendientes`.
   * Si el tiempo transcurrido desde `ultimo_envio` supera `intervalo_agrupacion`, se envían todas las alertas agrupadas y se actualiza `ultimo_envio`.

3. **Código de ejemplo:**

   ```python
   import time
   import random
   from datetime import datetime

   # Configuración
   umbral = 12.0
   intervalo_agrupacion = 300  # 5 minutos
   alertas_pendientes = []
   ultimo_envio = time.time()

   def enviar_alerta_telegram(mensaje):
       # Función para enviar mensaje a Telegram
       # Implementa aquí la lógica para enviar el mensaje utilizando tu bot
       print(f"Enviando alerta:\n{mensaje}")

   while True:
       caudal = round(random.uniform(0, 20), 2)
       timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

       if caudal > umbral:
           alerta = f"🚨 {timestamp} | Caudal: {caudal} L/min"
           alertas_pendientes.append(alerta)

       # Verificar si es momento de enviar alertas agrupadas
       if time.time() - ultimo_envio >= intervalo_agrupacion and alertas_pendientes:
           mensaje = "🔔 Alertas de caudal excesivo:\n" + "\n".join(alertas_pendientes)
           enviar_alerta_telegram(mensaje)
           alertas_pendientes.clear()
           ultimo_envio = time.time()

       time.sleep(5)
   ```

Se ha implementado un script ejecutable y automatizable en la carpeta [scripts](scripts/telegram_agg_send.py).

---

## ✅ Beneficios

* **Reducción de notificaciones:** Se evita enviar múltiples mensajes en un corto período.
* **Mayor claridad:** Las alertas agrupadas proporcionan una visión consolidada de los eventos.
* **Flexibilidad:** El intervalo de agrupación puede ajustarse según las necesidades.
