# Automatización de consulta en Node-RED
Vamos a trabajar con Node-RED para replicar el proceso de la consulta de datos históricos sobre Open-Meteo.

## Introducción a Node-RED
Node-RED es una herramienta de desarrollo basada en flujo, ideal para conectar dispositivos, servicios y API de forma visual. Creado por IBM, permite a los usuarios diseñar flujos que integran datos y automatizan procesos mediante una interfaz intuitiva. Esto lo hace perfecto para proyectos de Internet de las Cosas (IoT), automatización, y aplicaciones en tiempo real.

Node-RED está construido sobre Node.js, por lo que es necesario tenerlo instalado antes de usar Node-RED.

---

## **Requisitos Previos**
Antes de instalar Node-RED, necesitas:

- **Node.js** (versión 14.x o superior).
- **npm** (Node Package Manager, que viene con Node.js).
  
Verifica si ya tienes Node.js y npm instalados ejecutando en la terminal:
```bash
node -v
npm -v
```

Si no están instalados, sigue las instrucciones para tu sistema operativo.

---

## Instalación de Node.js y npm**

### **Windows**
1. Descarga el instalador de Node.js desde [nodejs.org](https://nodejs.org/).
2. Ejecuta el archivo `.msi` y sigue los pasos del asistente.
3. Una vez completada la instalación, abre la **PowerShell** y verifica la instalación:
   ```bash
   node -v
   npm -v
   ```

### **macOS**
1. Abre una terminal y ejecuta:
   ```bash
   brew install node
   ```
   (Requiere tener [Homebrew](https://brew.sh/) instalado).
2. Verifica que Node.js y npm estén instalados:
   ```bash
   node -v
   npm -v
   ```

### **Linux (Debian/Ubuntu)**
1. Actualiza tu sistema e instala Node.js:
   ```bash
   sudo apt update
   sudo apt install -y nodejs npm
   ```
2. Verifica la instalación:
   ```bash
   node -v
   npm -v
   ```

---

## **Paso 1: Configuración de Node-RED**
1. **Instalación de Node-RED** (si aún no lo tienes):
   - Si usas `npm`:
     ```bash
     npm install -g node-red
     ```
   - Luego, inicia Node-RED:
     ```bash
     node-red
     ```
   - Abre el navegador y accede a: `http://localhost:1880`.

2. **Añadir nodos adicionales**:
   - En la esquina superior derecha, haz clic en el menú desplegable y selecciona **Manage palette**.
   - Busca e instala los siguientes módulos:
     - **`node-red-contrib-http-request`**: Para realizar solicitudes HTTP.
     - **`node-red-contrib-cron-plus`**: Para programar tareas.
     - **`node-red-contrib-json`**: Para procesar datos JSON.

---

## **Paso 2: Crear el flujo para recopilar datos**

1. **Nodo `cron-plus`: Programar la tarea**
   - Arrastra un nodo `cron-plus` al flujo.
   - Configura la programación para ejecutar diariamente a las 6:00 AM:
     - Haz doble clic en el nodo.
     - Selecciona **Add new cron job** y define:
       - **Nombre del trabajo**: `Recopilación Open-Meteo`.
       - **Programación**: `0 6 * * *` (CRON para las 6:00 AM).
   - Conecta este nodo al flujo principal.

2. **Nodo `function`: Generar fechas dinámicas**
   - Arrastra un nodo `function` al flujo.
   - Configura el código para calcular las fechas dinámicas:
     ```javascript
     const now = new Date();
     const endDate = new Date(now.setDate(now.getDate() - 1)); // Fecha final
     const startDate = new Date(endDate);
     startDate.setDate(endDate.getDate() - 15); // Últimos 15 días

     msg.payload = {
         startDate: startDate.toISOString().split('T')[0],
         endDate: endDate.toISOString().split('T')[0]
     };
     return msg;
     ```
   - Conecta la salida del nodo `inject` a la entrda de este nodo.

3. **Nodo `http request`: Obtener datos de Open-Meteo**
   - Arrastra un nodo `http request` al flujo y colócalo antes del nodo `function`.
   - Conecta la salida del nodo `function` a a la entrada de este.
   - Configura este nodo para realizar una solicitud HTTP GET a la API de Open-Meteo:
     - Haz doble clic en el nodo.
     - Introduce la URL:
       ```
       https://archive-api.open-meteo.com/v1/archive?latitude=28.4161&longitude=-16.5446&start_date={{startDate}}&end_date={{endDate}}&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m
       ```
     - Sustituye `{{startDate}}` y `{{endDate}}` por las fechas dinámicas quese calculan en el nodo function. `startDate` -> `payload.startDate` y `endDate` -> `payload.endDate`.

4. **Nodo `json`: Procesar respuesta**
   - Arrastra un nodo `json` al flujo.
   - Este nodo convierte la respuesta JSON de Open-Meteo en un objeto JavaScript manejable.

5. **Nodo `file`: Guardar datos**
   - Arrastra un nodo `file` al flujo.
   - Configúralo para guardar los datos en un archivo CSV:
     - Haz doble clic en el nodo.
     - Introduce la ruta del archivo, por ejemplo:
       ```
       /ruta/a/logs/open_meteo_data.csv
       ```
     - Selecciona **Overwrite file**.

6. **Conectar nodos**:
   - Conecta todos los nodos en el siguiente orden:
     - `cron-plus` → `function` → `http request` → `json` → `file`.

---

## **Paso 3: Probar el flujo**
1. Haz clic en **Deploy** para implementar el flujo.
2. Ejecuta manualmente el flujo haciendo clic en el nodo `cron-plus`.
3. Verifica si los datos se guardaron correctamente en el archivo CSV.

---

## **Posibles mejoras**
1. Cambiar el nombre del archivo en función de la fecha con un nodo function
2. Transformar los datos en formato JSON y convertirlos a formato de lista de filas.
3. Guardar lista de filas en formato CSV.