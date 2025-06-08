**Caso Práctico – Monitorización en tiempo real de consumo energético con Streamlit y MQTT**

## Descripción general del caso práctico

Este panel permite monitorizar en tiempo real el consumo energético de tres zonas (`Zona Alta`, `Zona Media`, `Zona Baja`) de un centro educativo. Utiliza:

* **MQTT** para recibir datos en tiempo real
* **Plotly** para visualizaciones interactivas
* **Streamlit** para construir la interfaz web
* **`session_state`** para mantener los datos entre recargas
* **Detección básica de anomalías** con notificación

Enlace a la carpeta: [iBBi Energía](apps/ibbi_energia/)
---

## Estructura y explicación paso a paso

### 1. Carga de configuración y variables de entorno

```python
load_dotenv()
```

Se obtienen valores como el broker MQTT, usuario, contraseña, puerto y tópico desde un archivo `.env`, facilitando la configuración en producción.

---

### 2. Mapeo de dispositivos y umbrales

```python
device_map = { "zonaalta": "Zona Alta", ... }
device_thresholds = {"zonaalta": {"min": 0, "max": 1.5}, ... }
```

Permite:

* Mostrar nombres amigables en la interfaz
* Establecer los umbrales de detección de anomalías por zona

---

### 3. Inicialización de `session_state` para almacenamiento en tiempo real

```python
if "datos_mqtt" not in st.session_state:
    ...
```

Se inicializa un diccionario con:

* Una `deque` por zona (para guardar hasta 120 registros)
* Un `last_ts` para comprobar la conectividad

---

### 4. Configuración y conexión al broker MQTT

```python
def iniciar_mqtt():
    ...
```

* Se lanza un hilo con `threading.Thread` para mantener la conexión abierta.
* Se utiliza `paho-mqtt` con TLS (sin validación de certificado).
* Al recibir datos (`on_message`), se decodifica el payload JSON, se extrae la potencia (`p_total`) y se guarda junto a la marca de tiempo.

---

### 5. Configuración de la interfaz

```python
st.set_page_config(layout="wide")
st.title("iBBi - Monitor de Energía IES San Marcos")
```

* Se activa el layout de ancho completo
* Se coloca un título identificativo del panel

---

### 6. Generación del gráfico de área (segunda fila visual)

```python
df_total = pd.DataFrame(...)
df_total["ts"] = df_total["ts"].dt.floor("15s")
fig = px.area(...)
```

* Se combina la información de todas las zonas en un único DataFrame.
* Se redondea el tiempo a bloques de 15 segundos para homogeneizar.
* Se genera un **gráfico de área** con `plotly.express`, que muestra la evolución conjunta por zonas.

---

### 7. Visualización de métricas y último valor

```python
col1, col2 = st.columns([3, 1])
```

* En la columna izquierda se muestra el gráfico de área.
* En la derecha:

  * Se muestran los **últimos valores de cada zona**.
  * Se calcula el **total combinado** de potencia.

---

### 8. Estado de conectividad de cada zona (primera fila)

```python
delta = now_ts - ts
if delta < 30: estado = "🟢 ACTIVO"
...
```

* Se calcula el tiempo desde el último mensaje recibido.
* Se muestra un estado visual (activo, retrasado o desconectado).

---

### 9. Detección de anomalías por zona (última fila)

```python
fig.add_hline(...)  # Media y límites
st.toast(...)       # Si hay anomalía
```

* Por cada zona se muestra un **gráfico individual de líneas** con:

  * La serie histórica
  * La media
  * Umbrales superiores e inferiores (±50% en este caso)
* Si el último valor recibido **está fuera de los límites**, se lanza un `st.toast()` con un icono 🚨

---

### 10. Refresco automático

```python
time.sleep(5)
st.rerun()
```

El panel se actualiza automáticamente cada 5 segundos, lo que permite mantener la monitorización en tiempo real.

---

## Funcionalidades destacadas

| Funcionalidad               | Implementación                                 |
| --------------------------- | ---------------------------------------------- |
| Lectura MQTT en tiempo real | `paho-mqtt` + hilo `threading`                 |
| Interfaz moderna            | `streamlit` + `plotly.express`                 |
| Estado de conectividad      | basado en tiempo desde último dato             |
| Visualización global        | gráfico de área combinado                      |
| Visualización por zona      | gráfico individual con líneas de referencia    |
| Análisis de anomalías       | límites ±50% de la media con alerta tipo toast |
| Persistencia de datos       | `st.session_state` con `deque`                 |
| Seguridad MQTT opcional     | `client.tls_set(cert_reqs=ssl.CERT_NONE)`      |

---

## Potenciales mejoras

* Añadir **persistencia en disco o base de datos** para guardar históricos
* Permitir **selección dinámica de zonas** o métricas desde la interfaz
* Incluir **notificaciones externas** (Telegram, email)
* Añadir un **modo oscuro** o selector de temas