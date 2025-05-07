## Ejecución MQTT en local

### ✅ ¿Por qué hacerlo en local?

* No dependes de conexión externa.
* Puedes simular todo el sistema en el aula o laboratorio.
* Es ideal para experimentar con varios dispositivos en una red local (LAN).

---

## 🐧🔧 **INSTALACIÓN EN UNIX (Ubuntu/Debian/macOS vía Homebrew)**

### 1. **Instalar Mosquitto**

#### En Ubuntu/Debian:

```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

#### En macOS (con Homebrew):

```bash
brew install mosquitto
brew services start mosquitto
```

### 2. **Verificar que funciona**

Abre dos terminales:

* **Terminal 1 (Suscriptor):**

```bash
mosquitto_sub -h localhost -t prueba/agua
```

* **Terminal 2 (Publicador):**

```bash
mosquitto_pub -h localhost -t prueba/agua -m "Mensaje de prueba desde local"
```

✔️ Si ves el mensaje en el primer terminal, ¡funciona!

---

## 🪟🔧 **INSTALACIÓN EN WINDOWS**

### 1. **Descargar Mosquitto**

* Página oficial: [https://mosquitto.org/download/](https://mosquitto.org/download/)
* Descarga el instalador `mosquitto-<versión>-install-windows-x64.exe`.

### 2. **Instalación y configuración**

* Instala con los valores por defecto.
* Asegúrate de marcar la casilla “Instalar como servicio” o inicia manualmente con:

```powershell
cd "C:\Program Files\mosquitto"
mosquitto.exe
```

### 3. **Probar conexión**

Abre dos terminales de comandos (CMD o PowerShell):

* **Suscripción:**

```cmd
mosquitto_sub -h localhost -t prueba/agua
```

* **Publicación:**

```cmd
mosquitto_pub -h localhost -t prueba/agua -m "Hola desde Mosquitto local"
```

✔️ Si ves el mensaje publicado en la consola suscriptora, ¡tu broker MQTT local funciona!

---

## 🧪 Reutilizar con Python (con tu broker local)

Solo tienes que cambiar esta línea en los scripts Python del ejercicio:

```python
broker = "localhost"
```

✅ Esto hará que Python se conecte a **tu propio broker Mosquitto local**, en vez de al broker público.

---

## 📌 Consejos prácticos

* Puedes ver el archivo de configuración de Mosquitto en `/etc/mosquitto/mosquitto.conf` (Linux/macOS) o en `C:\Program Files\mosquitto\mosquitto.conf` (Windows).
* Si quieres ver logs o cambiar puertos, ahí puedes editarlo.
* Para clases, puedes montar el broker en un solo PC y que todos se conecten por IP (en red local).
