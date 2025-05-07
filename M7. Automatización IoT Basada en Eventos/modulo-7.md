# **Módulo 7: Automatización basada en eventos y detección con IA**

**Objetivo:** Configurar y automatizar la respuesta de dispositivos en función de eventos detectados en datos, combinando técnicas de IA con protocolos de comunicación IoT.

---

## 📅 **Sesión 1 (3h): Fundamentos y preparación de la automatización**

### 🕐 1. Introducción teórica (30–40 min)

* ¿Qué es la automatización basada en eventos?
* Flujo típico en un sistema IoT con respuesta automática.
* Comparativa de protocolos: MQTT vs Webhooks.
* Ejemplos reales en entornos de agua y energía.

### 🛠️ 2. Ejercicio práctico 1 (50–60 min) – *Publicar y suscribirse con MQTT*

* Instalación y uso de **Mosquitto** local o uso de broker público.
* Publicación de mensajes desde Python o Node-RED.
* Suscripción y visualización de mensajes desde otro cliente.

> Variación sin código: usar MQTT Explorer + Node-RED para quienes no programan.

### 🧪 3. Ejercicio práctico 2 (50–60 min) – *Simulación de evento e integración con webhook*

* Uso de Python o Node-RED para detectar evento (por ejemplo, un pico en el consumo de agua).
* Llamada automática a un webhook (Zapier, IFTTT o servidor local) para registrar el evento o activar respuesta.

### 📌 4. Recapitulación y asignación para casa (15 min)

* Lectura complementaria: diferencias clave entre protocolos.
* Trabajo en casa: buscar un caso real en su centro educativo donde se podría aplicar una automatización (respuesta automática a fuga, exceso de consumo, etc.).

---

## 📅 **Sesión 2 (3h): IA para detección y caso práctico de automatización**

### 🕐 1. Repaso breve + introducción IA + pipelines (30–40 min)

* Revisión de lo visto.
* Introducción a la detección de anomalías para activar dispositivos.
* Estructura de un pipeline automatizado con IA:

  * Ingesta → detección → respuesta

### 🧠 2. Ejercicio práctico 3 (60 min) – *Automatización con IA simple*

* Dataset sintético de consumo de agua.
* Modelo de detección de anomalías (Isolation Forest o umbral simple).
* Al detectar anomalía → enviar señal MQTT o webhook.

> Se facilitará un script base en Python y su equivalente visual en Node-RED.

### 🧪 3. Caso práctico final (60 min) – *Red de consumo de agua inteligente*

* Montaje de un pequeño sistema de automatización:

  * Simulación de red de sensores (lecturas periódicas).
  * Detección de anomalías en tiempo real.
  * Activación de actuador simulado (envío de alerta, cierre virtual de válvula, etc.).

> Puede desarrollarse en subgrupos con distintos roles: programación, configuración de nodos, diseño del flujo lógico.

---

## 📚 Trabajo en casa (3h)

* Desarrollar un mini-prototipo o esquema funcional adaptado a una situación concreta del entorno educativo del profesorado.
* Incluir: fuente de datos, evento disparador, acción automatizada.
* Entregable: pequeño informe (diagrama + descripción de funcionamiento).

---

¿Te gustaría que prepare también los notebooks, materiales de apoyo o plantillas base para Node-RED y Python?
