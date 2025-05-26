# Módulo 2: Acceso Automatizado a Fuentes de Datos y APIs

## 📅 Sesión 1 (Online): Introducción al Acceso Automatizado a Datos

**Duración:** 3 horas  
**Objetivo:** Capacitar a los participantes en el uso de interfaces de datos (APIs) para la extracción automatizada de datos, centrándose en fuentes relevantes para la sostenibilidad, como el consumo de agua, energía y datos meteorológicos.

---

### **Estructura de la sesión:**

1. **Introducción (15 minutos):**
   - Presentación del objetivo del módulo: cómo utilizar APIs para automatizar la obtención de datos y su importancia en la monitorización de recursos.
   - Introducción a conceptos clave:
     - ¿Qué es una API? ¿Por qué es útil en ciencia de datos?
     - Tipos de APIs (REST, SOAP) y formatos de datos (JSON, XML).

2. **Acceso a APIs y manejo de `requests` (45 minutos):**
   - **Introducción a la librería `requests`**:
     - Cómo instalarla y usarla para interactuar con APIs.
     - Realizar una solicitud HTTP GET a una API pública.
     - Interpretación de respuestas en formato JSON.
   - **Ejercicio práctico**:
     - Extraer datos de una API pública de energía o meteorología (e.g., OpenWeatherMap).
     - Conversión de respuestas JSON a DataFrames con `pandas`.
     - Limpieza y transformación básica para preparar los datos.
   - **Materiales:**
     - Ejemplos de código en notebooks para diferentes tipos de solicitudes (GET, POST).
     - Guía rápida sobre el uso de `requests` y manejo de errores.

3. **Autenticación y acceso a APIs protegidas (30 minutos):**
   - Explicación de métodos de autenticación (API Keys, tokens).
   - Ejemplo práctico: acceso a una API que requiere autenticación.
   - **Materiales:**
     - Tutorial sobre cómo registrarse y obtener una API Key.
     - Ejercicios guiados para realizar solicitudes autenticadas.

4. **Cierre y Ejercicio Final (15 minutos):**
   - Repaso de los conceptos vistos en la sesión.
   - Ejercicio de cierre: extraer datos de una API, cargarlos en un DataFrame y realizar un análisis exploratorio.
   - Resolución de dudas y consultas.

### **Tarea para casa:**

- Realizar una conexión a una API de su elección (puede ser relacionada con energía, agua o meteorología).
- Extraer un conjunto de datos, limpiarlo y cargarlo en un DataFrame para su análisis.
- Documentar el proceso y subir el notebook a Google Colab.

--

## 📅 Sesión 2: Adquisición Automatizada y Flujos de Datos

**Duración:** 3 horas  
**Objetivo:** Aprender a integrar los datos obtenidos mediante APIs en flujos de trabajo de análisis, incluyendo la automatización y el uso de Node-RED para la adquisición de datos en tiempo real.

---

### **Estructura de la sesión**

1. **Repaso y Conceptos Avanzados (15 minutos):**
   - **Repaso de la sesión anterior**: extracción y autenticación en APIs.
   - Introducción a conceptos avanzados:
     - Paginación en APIs (manejo de grandes volúmenes de datos).
     - Rate limits y cómo gestionarlos.

2. **Automatización de la Extracción de Datos (30 minutos):**

   - Uso de bucles y scripts en Python para la descarga periódica de datos.
   - Programación de tareas automatizadas (introducción a `cron` en sistemas Unix o `Task Scheduler` en Windows).
   - **Ejercicio práctico**:
     - Automatizar la descarga de datos meteorológicos cada hora y almacenarlos en un archivo CSV.
   - **Materiales**:
     - Ejemplos de scripts para automatización.
     - Tutorial para configurar tareas programadas.

3. **Introducción a Node-RED para la Adquisición de Datos (1 hora)**
   - **Conceptos básicos de Node-RED**:
     - ¿Qué es Node-RED? Instalación y configuración básica.
     - Cómo funciona el flujo de datos mediante nodos.
   - **Ejercicio guiado 1: Consulta a un API Abierto**:
     - Uso de nodos `http request` para realizar una solicitud a un API sin autenticación (por ejemplo, datos de calidad del aire).
     - Transformación de la respuesta JSON y visualización en un dashboard de Node-RED.
   - **Ejercicio guiado 2: Consulta a un API con Credenciales (OpenWeatherMap)**:
     - Configuración de un flujo para conectarse al API de OpenWeatherMap usando una API Key.
     - Manejo de credenciales mediante el nodo `http request` y tratamiento de la respuesta.
     - Visualización en tiempo real de los datos meteorológicos.
   - **Materiales**:
     - Guía de instalación de Node-RED y ejemplos de flujos exportables.
     - Tutorial en PDF sobre cómo obtener una API Key y configurarla en Node-RED.

4. **Análisis y Visualización de Datos Obtenidos (45 minutos)**
   - Exploración y análisis básico de los datos extraídos:
     - Limpieza de datos con `pandas`.
     - Análisis de tendencias en los datos obtenidos (p. ej., temperaturas, humedad).
   - Visualización con `matplotlib` y `seaborn`:
     - Creación de gráficos para visualizar patrones y correlaciones.
     - Ejemplo de gráficos de líneas y barras.
   - **Materiales**:
     - Ejemplos de notebooks para análisis y visualización.
     - Datasets generados a partir de las consultas realizadas con Node-RED.

5. **Cierre y Ejercicio Final (15 minutos):**
   - **Ejercicio de cierre**:
     - Utilizar Node-RED para extraer datos de un API de su elección, integrarlos en un flujo, y realizar un análisis básico en un notebook.
   - Resolución de dudas y consultas.

### Tarea para casa

- Configurar un flujo en Node-RED que consulte un API cada 3 horas, almacene los datos en un archivo CSV y los visualice en un dashboard.
- Importar el CSV a un notebook en Google Colab, analizar los datos y generar una visualización.
- Documentar el proceso y subir el notebook a la plataforma para su revisión.

---

### Recursos y Herramientas

- Presentación M2 iBBi [PDF](https://drive.google.com/file/d/1Ki3tllV-zYjNaTefe0mlgwlHHEoiSv8X/view?usp=sharing)
- Repositorio de materiales en [Github](https://github.com/jorgballesteros):  
  - Ejemplos de flujos y scripts para ejercicios prácticos.
  - Datasets en formato JSON y CSV generados en la sesión.
  - Ejercicios prácticos en notebooks.
  - Tutoriales y ayuda.
- Acceso a [Node-RED](https://nodered.org/docs/) (instalación local o en la nube).
- Acceso a [Google Colab](https://colab.research.google.com/) y [Jupyter Notebooks](https://jupyter.org/).
