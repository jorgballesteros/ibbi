# Tarea 5: Alta y acceso a Google Colab
## Introducción a Google Colab
Google Colab es una plataforma gratuita que permite ejecutar código Python en un entorno basado en Jupyter Notebooks, sin necesidad de instalar nada en tu computadora. Está especialmente diseñada para tareas de ciencia de datos, aprendizaje automático e inteligencia artificial, aprovechando recursos como GPU y TPU para acelerar los cálculos.

Google Colab es ideal para proyectos colaborativos y educativos, ya que facilita compartir, ejecutar y modificar notebooks directamente desde un navegador. Además, está completamente integrado con Google Drive, lo que simplifica el almacenamiento y el acceso a tus archivos.

---

## **Instrucciones para Crear una Cuenta y Usar Google Colab**

### **1. Registro en Google Colab**
1. **Accede a Google Colab**:
   - Ve a [Google Colab](https://colab.research.google.com/).
   - Asegúrate de **iniciar sesión** con tu cuenta de Google.
   - Si aún no tienes una cuenta de Google, crea una en [Google Account](https://accounts.google.com/).

### **2. Crear un Nuevo Notebook**
1. Una vez dentro de Google Colab, haz clic en **"Nuevo notebook"** (New Notebook).
2. Se abrirá una nueva pestaña con un entorno de Jupyter Notebook listo para usar.
3. El notebook estará automáticamente guardado en tu Google Drive (puedes encontrarlo en la carpeta `Colab Notebooks`).

---

## **Ejemplo Práctico: Hola Mundo en Google Colab**

1. En tu nuevo notebook, en la celda de código, escribe:
   ```python
   print("¡Hola, mundo desde Google Colab!")
   ```
2. Ejecuta la celda haciendo clic en el ícono de **play** o presionando `Shift + Enter`.
3. Verás el resultado debajo de la celda:

   ```
   ¡Hola, mundo desde Google Colab!
   ```

---

## **Conectar Google Drive con Google Colab**
Si necesitas acceder a archivos desde tu Google Drive, puedes montarlo en tu notebook de Colab:

1. Ejecuta el siguiente código en una celda:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
2. Aparecerá un enlace para autorizar el acceso a tu Google Drive. Haz clic, selecciona tu cuenta y copia el código que te proporcionan.
3. Pega el código en la celda para completar la conexión. Ahora podrás acceder a tus archivos en `/content/drive`.

---

## **Ejemplo: Importar un Dataset desde Google Drive**

Supongamos que tienes un archivo `datos.csv` en tu Google Drive. Puedes leerlo directamente en Colab usando `pandas`:

```python
import pandas as pd

# Accede al archivo desde tu Drive
ruta = '/content/drive/MyDrive/datos.csv'
df = pd.read_csv(ruta)

# Mostrar las primeras filas
print(df.head())
```

---

## **Recursos Adicionales (Video Tutoriales)**
1. [Introducción a Google Colab (YouTube)](https://www.youtube.com/watch?v=inN8seMm7UI) - Un tutorial detallado para principiantes.
2. [Curso rápido de Google Colab (YouTube)](https://www.youtube.com/watch?v=xl8zdCY-abw) - Aprende cómo sacar el máximo provecho a Colab.

Con estos pasos y ejemplos, estarás listo para empezar a usar Google Colab en tus proyectos de ciencia de datos y aprendizaje automático.