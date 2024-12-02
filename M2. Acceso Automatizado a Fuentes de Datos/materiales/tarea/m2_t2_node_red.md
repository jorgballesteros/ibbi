# Tarea para casa. Introdución a Node-RED

## ¿Que es Node-RED?
Node-RED es una herramienta de desarrollo basada en flujo, ideal para conectar dispositivos, servicios y API de forma visual. Creado por IBM, permite a los usuarios diseñar flujos que integran datos y automatizan procesos mediante una interfaz intuitiva. Esto lo hace perfecto para proyectos de Internet de las Cosas (IoT), automatización, y aplicaciones en tiempo real.

Node-RED está construido sobre Node.js, por lo que es necesario tenerlo instalado antes de usar Node-RED. A continuación, te explico cómo instalar y configurar Node-RED en tu sistema.

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

## **1. Instalación de Node.js y npm**

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

## **2. Instalación de Node-RED**

Una vez que Node.js y npm están instalados, sigue estos pasos para instalar Node-RED:

```bash
sudo npm install -g --unsafe-perm node-red
```

### **Verificar la instalación**
Para asegurarte de que Node-RED se ha instalado correctamente, ejecuta:

```bash
node-red
```

Esto iniciará Node-RED en tu terminal y deberías ver un mensaje indicando que está funcionando en `http://127.0.0.1:1880`.

---

## **3. Ejecutar Node-RED**
1. Abre tu navegador y ve a la dirección:
   ```
   http://localhost:1880
   ```
2. Verás la interfaz de Node-RED. Aquí puedes empezar a crear flujos.

---

## **4. Ejemplo: Crear un Flujo Simple**

### **Crear un Flujo de "Hola Mundo"**
1. Arrastra un nodo **inject** y un nodo **debug** al área de trabajo.
2. Conéctalos arrastrando una línea entre ellos.
3. Haz doble clic en el nodo `inject`, establece el **payload** como `string` y escribe:
   ```
   ¡Hola, mundo!
   ```
4. Haz clic en **Deploy**.
5. Haz clic en el botón junto al nodo `inject` y observa el resultado en la pestaña **debug** (en la parte derecha).

---

## **Recursos Adicionales (Video Tutoriales)**
1. [Introducción a Node-RED (YouTube)](https://www.youtube.com/watch?v=4J1I4eE7Y6Y) - Tutorial básico para principiantes.
2. [Automatización con Node-RED (YouTube)](https://www.youtube.com/watch?v=6a61YYwot8w) - Cómo crear flujos automatizados.