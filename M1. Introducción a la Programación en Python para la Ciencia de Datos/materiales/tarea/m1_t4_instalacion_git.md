# Tarea 4: Instalación de `git` y descarga de repositorio
## Introducción a Git
Git es un sistema de control de versiones distribuido que permite gestionar y rastrear cambios en el código fuente de proyectos. Utilizado principalmente en entornos de desarrollo de software, Git facilita la colaboración entre equipos, ya que permite a múltiples desarrolladores trabajar en el mismo proyecto sin interferir entre sí. Además, mantiene un historial detallado de todas las modificaciones, permitiendo revertir a versiones anteriores si es necesario.

Uno de los usos más populares de Git es junto con GitHub, una plataforma que permite alojar repositorios en la nube. GitHub simplifica el intercambio de código, la colaboración en proyectos, y la integración de herramientas para automatizar procesos de desarrollo. A continuación, aprenderemos a instalar Git y a clonar un repositorio desde GitHub.

---

## Instrucciones de Instalación de Git

### **1. Instalación en Windows**
1. **Descarga** el instalador desde [git-scm.com](https://git-scm.com/download/win).
2. **Ejecuta el instalador** (`.exe`) y sigue los pasos del asistente.
   - Acepta los términos de la licencia.
   - En la sección "Select Components", asegúrate de que las opciones "Git Bash" y "Git GUI" estén seleccionadas.
   - Usa la configuración por defecto en las demás opciones.
3. Tras la instalación, abre la terminal **Git Bash** (puedes buscarla en el menú de inicio) y ejecuta el siguiente comando para verificar la instalación:
   ```bash
   git --version
   ```

### **2. Instalación en Unix (Linux y macOS)**
#### En Linux (Debian/Ubuntu)
1. Abre una terminal y ejecuta:
   ```bash
   sudo apt update
   sudo apt install git
   ```
2. Verifica que se instaló correctamente con:
   ```bash
   git --version
   ```

#### En macOS
1. Abre una terminal y ejecuta:
   ```bash
   brew install git
   ```
   (Requiere que tengas [Homebrew](https://brew.sh/) instalado).
2. Verifica la instalación:
   ```bash
   git --version
   ```

---

## **Configuración Inicial de Git**
Antes de empezar a usar Git, configura tu nombre y correo electrónico para asociar tus cambios con tu identidad:
```bash
git config --global user.name "TuNombre"
git config --global user.email "TuCorreo@example.com"
```

---

## **Clonar un Repositorio desde GitHub**
1. Abre **Git Bash** (en Windows) o una terminal (en Unix).
2. Ve al directorio de trabajo del curso:
   ```bash
   cd /ruta/del/directorio
   ```
3. Clona el repositorio usando su URL:
   ```bash
   git clone https://github.com/jorgballesteros/ibbi.git
   ```
4. Accede al directorio clonado:
   ```bash
   cd nombre-del-repositorio
   ```
5. Comprueba que todo esté bien:
   ```bash
   git status
   ```

---

## **Recursos Adicionales (Video Tutoriales)**
1. [Git y GitHub desde cero (YouTube)](https://www.youtube.com/watch?v=HiXLkL42tMU) - Un tutorial detallado para principiantes que explica desde la instalación hasta el uso básico de Git.
2. [Curso Git y GitHub para principiantes (YouTube)](https://www.youtube.com/watch?v=RGOj5yH7evk) - Explica cómo trabajar con Git y GitHub de manera práctica.