# Ejercicio 1b – Monitorizar estado de conexión en tiempo real con Node-RED Dashboard

Visualizar en tiempo real el estado de distintos topics MQTT, utilizando **indicadores de color** según el tiempo desde el último mensaje recibido:

* 🟢 **Verde:** menos de 10 segundos
* 🟡 **Amarillo:** entre 10 y 30 segundos
* 🔴 **Rojo:** más de 60 segundos

---

## Estructura general del flujo

### Componentes:

1. **Nodos `mqtt in`** (uno por cada topic que se quiera monitorizar)
2. **Nodos `function`** para registrar el `timestamp` del último mensaje recibido
3. **Un bucle `inject` cada 5s** para verificar los tiempos
4. **Indicadores visuales `ui_text` o `ui_led`** en el dashboard (1 por topic)

---

## Paso a paso

### 1. Nodo `mqtt in`

* Topic: por ejemplo, `edificio/sensor1`
* Conéctalo a un nodo `function`:

```javascript
// Guarda el timestamp actual
flow.set("ultimo_sensor1", Date.now());
return null;  // No pasa nada hacia adelante
```

### 2. Nodo `inject` (cada 5 segundos)

* Genera un trigger periódico
* Conéctalo a un nodo `function` llamado `"Evaluar estado sensor1"`:

```javascript
let ultimo = flow.get("ultimo_sensor1") || 0;
let ahora = Date.now();
let diff = (ahora - ultimo) / 1000; // segundos

let estado = "";
let color = "";

if (diff < 10) {
    estado = "🟢 ACTIVO";
} else if (diff < 30) {
    estado = "🟡 RETRASO";
} else if (diff < 60) {
    estado = "🔴 INACTIVO";
} else {
    estado = "❌ SIN RESPUESTA";
}

msg.payload = `Sensor 1: ${estado} (${Math.round(diff)}s)`;
return msg;
```

### 3. Nodo `ui_text` (o `ui_led`)

* Muestra el mensaje en el dashboard

---

## Escalado a múltiples topics

Repite el mismo patrón para cada topic:

* `mqtt in` → `function` para guardar timestamp
* `function` evaluador → `ui_text` para visualización

---

## Alternativas visuales

* Usa `ui_led` del paquete `node-red-contrib-ui-led` para una representación más gráfica

  ```bash
  npm install node-red-contrib-ui-led
  ```
* Usa `ui_template` con HTML + CSS para hacer tarjetas con estilo si quieres una vista más compacta
