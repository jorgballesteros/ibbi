# **Ejercicio 6: Detección de anomalías en potencia en tiempo real con ThingsBoard, MQTT y Python**

## 1. Introducción

Este ejercicio integra múltiples tecnologías para simular un sistema IoT con capacidad de análisis inteligente en tiempo real. Su objetivo es **monitorizar la variable `potencia`** de un dispositivo de ThingsBoard, detectar comportamientos anómalos y generar una **alarma automatizada** si se detecta una desviación significativa.

## 2. Estructura y flujo de trabajo

```text
[1] ThingsBoard (dispositivo virtual)
       ↓ (API REST)
[2] Python obtiene telemetría
       ↓
[3] Reenvía los datos al broker MQTT
       ↓
[4] Python suscriptor MQTT recibe datos → analiza la potencia
       ↓
[5] Acumula un buffer de 20 muestras
       ↓
[6] Calcula media y umbrales ±20%
       ↓
[7] Si el nuevo valor excede los umbrales → alarma vía API ThingsBoard
```

---

## 3. Implementación

Se ha implementado un conjunto de scripts y archivos de confguración en [thingsboard_monitor.](scripts/thingsboard_monitor)

---

### `validar_usuario.py`

**Función**: Autenticarse contra ThingsBoard mediante usuario y contraseña.

**Conceptos clave**:

* `POST /api/auth/login` → devuelve un token JWT.

**Código clave**:

```python
auth_payload = { "username": tb_user, "password": tb_pass }
token = requests.post(auth_url, json=auth_payload).json().get("token")
```

---

### `leer_telemetria.py`

**Función**: Lee telemtería de Thingsboard y reenvía periódicamente los datos de potencia al broker MQTT.

**Conceptos clave**:

* `GET /api/plugins/telemetry/.../values/timeseries` → obtiene la última telemetría.
* MQTT topic personalizado.
* Simulación de dispositivo emisor (publisher).

**Código clave**:

```python
client.publish("ibbi/energia/dispositivo", json.dumps(payload))
```

---

### `detectar_anomalia.py`

**Función**: Suscribirse al topic MQTT, leer valores de potencia, acumular un buffer de 20 muestras y detectar anomalías.

**Conceptos clave**:

* `deque(maxlen=20)` como buffer circular.
* Cálculo de media y umbrales dinámicos.
* Generación de alarma solo cuando la muestra supera ±20%.

**Código clave**:

```python
if len(buffer) == 20:
    media = sum(buffer) / 20
    lower = media * 0.75
    upper = media * 1.25
    if potencia < lower or potencia > upper:
        run(["python", "publicar_alarma.py", str(potencia)])
```

---

### `publicar_alarma.py`

**Función**: Enviar una **alarma personalizada al dispositivo** de ThingsBoard usando el token JWT

**Conceptos clave**:

* Uso de `POST /api/alarm` para registrar una alarma en el dispositivo.
* Alternativamente, se puede usar `/api/plugins/telemetry/...` para eventos.

**Código clave**:

```python
payload = { "alarma": f"Potencia anómala detectada: {valor}" }
requests.post(tb_url + "/api/v1/<token>/attributes", json=payload)
```

---

## Archivos adicionales

* `.env`: centraliza configuración sensible (URLs, claves, topics, IDs).
* `tb_token.txt`: almacena el token JWT si se quiere evitar múltiples logins.

---

## Conclusiones del ejercicio

Este ejercicio permite al alumnado:

* Comprender cómo se integran sistemas IoT con lógica de negocio.
* Aplicar conceptos de procesamiento en tiempo real.
* Usar buffers, umbrales dinámicos y lógica condicional en Python.
* Interactuar con APIs REST reales y brokers MQTT.
* Desarrollar automatismos inteligentes y personalizables para la gestión energética.