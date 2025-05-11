# **Ejercicio 1 – Publicar y Suscribirse con MQTT**

## Objetivo

Que los participantes entiendan y experimenten el funcionamiento del modelo **Publicador/Suscriptor** usando MQTT, con sensores simulados y visualización del flujo de datos.

---

## **Materiales necesarios**

* Python 3 instalado (o Node-RED, alternativa visual).
* Un broker MQTT público (por ejemplo: `broker.hivemq.com`) o broker en [local](ayuda/mqtt-local.md).
* Cliente de prueba (opcional): MQTT Explorer ([http://mqtt-explorer.com](http://mqtt-explorer.com)).

---

## Opción 1: Con Python

### Instalación de librería MQTT

```bash
pip install paho-mqtt
```

### Script del Publicador (simula un sensor de agua)

```python
import paho.mqtt.client as mqtt
import time
import random

broker = "broker.hivemq.com"
topic = "ibbicurso/canarias/agua"

client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    caudal = round(random.uniform(5.0, 15.0), 2)
    mensaje = f"Caudal: {caudal} L/min"
    client.publish(topic, mensaje)
    print(f"Publicado → {mensaje}")
    time.sleep(5)
```

Se ha implementado un script ejecutable y automatizable en la carpeta [scripts](scripts/mqtt_pub.py).

### Script del Suscriptor (simula el sistema que actúa)

```python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Conectado con código:", rc)
    client.subscribe("ibbicurso/canarias/agua")

def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()} en el tema {msg.topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()
```

Se ha implementado un script ejecutable y automatizable en la carpeta [scripts](scripts/mqtt_sub.py).

---

## Opción 2: Visual y sin código – Usando Node-RED

###  Preparación

1. Accede a Node-RED (local o [https://fred.sensetecnic.com](https://fred.sensetecnic.com)).
2. Arrastra los nodos:

   * `mqtt in` (para suscribirse).
   * `mqtt out` (para publicar).
   * `inject` (para simular datos).
   * `debug` (para ver los mensajes).

### Configuración del broker

* Server: `broker.hivemq.com`
* Puerto: `1883`
* Tema de prueba: `ibbicurso/canarias/agua`

### Flujo típico:

* El nodo `inject` manda un valor simulado (ej. `"Caudal: 12.4"`).
* El nodo `mqtt out` lo publica.
* El nodo `mqtt in` lo recibe.
* Se visualiza con `debug`.

## 🧠 Actividades complementarias

* Cambiar el nombre del tema a algo personalizado (por grupo).
* Probar con múltiples suscriptores (ver cómo se recibe el mismo mensaje en varias consolas).
* Usar MQTT Explorer para visualizar los temas activos y mensajes.

---

## ✅ Cierre del ejercicio

* Preguntas para reflexión:

  * ¿Qué ventajas tiene este modelo frente al polling tradicional?
  * ¿Cómo podríamos usar este sistema para activar una respuesta automática?