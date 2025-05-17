# **Módulo 7: Automatización basada en eventos y detección con IA**

**Objetivo:** Configurar e implementar sistemas de automatización que respondan en tiempo real a eventos detectados mediante sensores IoT, aplicando lógica basada en reglas o modelos de inteligencia artificial para generar alertas o activar dispositivos.

---

## 📅 Sesión 1 (3h): Fundamentos y preparación de la automatización
**Objetivo**: Comprender los mecanismos de comunicación en sistemas IoT, aprender a integrar dispositivos mediante MQTT y Webhooks, y desarrollar automatizaciones simples ante eventos.

**Contenidos**:
- Conceptos clave de automatización en IoT.
- Arquitectura de un sistema IoT con respuesta automática.
- Introducción al protocolo MQTT y comparación con Webhooks.
- Visualización del ciclo Sensor → Evento → Acción.
- Publicación y suscripción con MQTT en Python y Node-RED.
- Envío de alertas mediante Webhooks y Telegram.

Enlace: [m7_e0_intro.md](materiales/m7_e0_intro.md)

### Ejercicio 1 – Publicar y suscribirse con MQTT
Los participantes aprenden el modelo de comunicación Publish/Subscribe usando MQTT. Simulan sensores que publican datos periódicos y crean suscriptores para visualizar o procesar la información.

Enlace: [m7_e1_mqtt.md](materiales/m7_e1_mqtt.md)

### Ejercicio 2 – Alerta por Telegram ante evento de caudal excesivo
Se genera un flujo de datos de caudal y se configura una alerta automática vía bot de Telegram cuando se supera un umbral de caudal definido, integrando notificación instantánea en tiempo real.

Enlace: [m7_e2_alerta_eventos.md](materiales/m7_e2_alerta_eventos.md)

### Ejercicio 3 – Agrupación de eventos
Se desarrolla una lógica para agrupar múltiples eventos o alertas dentro de un intervalo de tiempo (por ejemplo, 10 minutos), evitando notificaciones redundantes y facilitando la supervisión.

Enlace: [m7_e3_agregar_eventos.md](materiales/m7_e3_agregar_eventos.md)

### Ejercicio 4 – Pipelines en IoT para automatización inteligente
A través de un ejemplo guiado, los participantes exploran cómo estructurar un pipeline completo de automatización IoT con toma de decisiones. Se introduce la detección de eventos mediante reglas o IA y se representa el flujo completo desde el sensor hasta la acción.

Enlace: [m7_e4_pipelines_iot.md](materiales/m7_e4_pipelines_iot.md)

### Recapitulación y tarea para casa (15 min)

* Lectura complementaria: diferencias clave entre protocolos.
* Trabajo en casa: buscar un caso real en su centro educativo donde se podría aplicar una automatización (respuesta automática a fuga, exceso de consumo, etc.).

---

## 📅 Sesión 2 (3h): IA para detección y caso práctico de automatización

**Objetivo**: Integrar modelos simples de IA en el pipeline de decisión en IoT, implementando detección de anomalías con Python en tiempo real, y automatización de alarmas o respuestas.

**Contenidos**:
- ¿Qué aporta la IA en automatización? Introducción a detección de anomalías.
- Concepto de pipeline inteligente: Sensor → Datos → IA → Decisión → Acción.
- Modelos sencillos de detección: Isolation Forest y umbrales adaptativos.
- Estructura de buffer, análisis dinámico y activación de alarmas.
- Integración de análisis en tiempo real sobre mensajes MQTT.

### Ejercicio 5 – Pipeline IoT para detección de anomalía en consumo de potencia
A partir de un dataset real de consumo energético en un edificio de oficinas, se construye un pipeline completo:

- Realizar un análisis exploratorio (EDA)
- Entrenar modelos de detección de anomalías (Isolation Forest)
- Simular el envío de datos históricos por MQTT
- Detectar anomalías en tiempo real
- Activar y enviar una alerta por Telegram

Enlace: [m7_e5_pipeline_energia_iot.md](materiales/m7_e5_pipeline_energia_iot.md)

### Ejercicio 6 – Detección de anomalías en potencia en tiempo real con ThingsBoard, MQTT y Python
Se implementa un sistema que:

- Leer la telemetría desde la API REST de un dispositivo en ThingsBoard
- Reenviar estos datos a un broker MQTT
- Evaluar en tiempo real las muestras de potencia, acumulando un buffer de 20 valores
- Calcular umbrales dinámicos (±20%) y detecta si una muestra se desvía significativamente
- Generar una alarma en ThingsBoard si se detecta una anomalía

Enlace: [m7_e6_thingsboard_eventos.md](materiales/m7_e6_thingsboard_eventos.md)

---

## 🏠 Trabajo en casa (3h)

* Desarrollar un mini-prototipo o esquema funcional adaptado a una situación concreta del entorno educativo del profesorado.
* Incluir: fuente de datos, evento disparador, acción automatizada.
* Entregable: pequeño informe (diagrama + descripción de funcionamiento).
