# Ejercicio 8: Servicios de Visualización Autoalojados

---

## 1. Introducción

Los servicios de visualización **autoalojados** permiten a los usuarios crear dashboards y gráficos avanzados en sus propios servidores, sin depender de servicios en la nube. Esto asegura control total sobre los datos, configuraciones personalizadas y mayor privacidad. Ejemplos populares incluyen **RawGraphs**, **Metabase** y **Grafana**, que ofrecen distintas funcionalidades.

---

### Opciones Populares de Servicios Autoalojados
1. **RawGraphs**:
   - Ideal para crear visualizaciones complejas y menos comunes, como gráficos de flujo, matrices o diagramas de red.
   - Diseñado para análisis exploratorio y generación de gráficos únicos.

2. **Metabase**:
   - Enfocado en la creación de dashboards interactivos a partir de bases de datos.
   - Ofrece una interfaz simple y consultas automatizadas para usuarios no técnicos.

3. **Grafana**:
   - Especializado en la monitorización en tiempo real de métricas y series temporales.
   - Amplio soporte para integraciones con bases de datos y sistemas de métricas.

---

### Ventajas y Desventajas de Servicios Autoalojados

| Aspecto               | Ventajas                                          | Desventajas                                      |
|------------------------|--------------------------------------------------|-------------------------------------------------|
| **Privacidad**         | Datos alojados localmente, mayor control.        | Requiere administración del servidor.           |
| **Flexibilidad**       | Total personalización de gráficos y dashboards.  | Menos sencillo de usar que herramientas como Plotly/Dash. |
| **Costo**              | A menudo gratuitos o de bajo costo inicial.      | Costos asociados al mantenimiento del servidor. |
| **Interactividad**     | Interfaces más simples para usuarios no técnicos.| Menor interactividad comparada con Dash/Plotly. |
| **Integración**        | Conexión directa con bases de datos locales.     | Configuración inicial puede ser compleja.       |

---

## 2. Objetivo del Ejercicio

Utilizaremos **RawGraphs** para explorar un conjunto de datos relacionado con el consumo de recursos (energía, agua) y su variación según la localización y el tiempo. RawGraphs es ideal para crear visualizaciones avanzadas que destaquen patrones complejos.

---

## 3. Desarrollo del Ejercicio

### Paso 1: Preparar los Datos
Asegúrate de tener un archivo CSV con las siguientes columnas:
- `Fecha`: Fecha y hora de la medición.
- `Localización`: Ubicación de la medición.
- `Consumo Agua (L)`: Cantidad de agua consumida.
- `Consumo Energía (kWh)`: Cantidad de energía consumida.

Si no tienes un archivo, aquí está un ejemplo para simular los datos:

```python
import pandas as pd
import numpy as np

# Simular datos
np.random.seed(42)
fechas = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
localizaciones = ["Edificio A", "Edificio B", "Edificio C"]

data = {
    "Fecha": np.tile(fechas, len(localizaciones)),
    "Localización": np.repeat(localizaciones, len(fechas)),
    "Consumo Agua (L)": np.random.randint(100, 1000, len(fechas) * len(localizaciones)),
    "Consumo Energía (kWh)": np.random.randint(50, 300, len(fechas) * len(localizaciones)),
    "Generación FV (kWh)": np.random.randint(50, 90, len(fechas) * len(localizaciones)),
    "Temperatura (ºC)": np.random.randint(15, 35, len(fechas) * len(localizaciones)),
}

df = pd.DataFrame(data)

# Guardar en CSV
df.to_csv("consumo_recursos.csv", index=False)
```

---

Para ejecutar **RawGraphs** en tu máquina de forma local, debes clonar su repositorio oficial y ejecutarlo en un entorno controlado. A continuación, te muestro los pasos detallados para instalar y usar RawGraphs en local.

---

### Paso 2. Instalación Local de RawGraphs (Opcional)

1. Requisitos Previos;
    Antes de empezar, asegúrate de tener lo siguiente instalado en tu máquina:
    1. **Node.js** (v16 o superior): Descárgalo desde [Node.js Official Site](https://nodejs.org/).
    2. **Git**: Descárgalo desde [Git Official Site](https://git-scm.com/).

    Para verificar que tienes Node.js y Git instalados, ejecuta los siguientes comandos en tu terminal:

    ```bash
    node -v
    git --version
    ```

2. Clonar el Repositorio de RawGraphs
    Clona el repositorio oficial de **RawGraphs** desde GitHub:

    ```bash
    git clone https://github.com/rawgraphs/rawgraphs-app.git
    cd rawgraphs-app
    ```

2. Instalar Dependencias
    Instala las dependencias necesarias con **npm** (Node Package Manager):

    ```bash
    npm install
    ```
    Si se produce un error al instalar dependencias ejecutar el siguiente comando:
    ```bash
    npm install --legacy-peer-deps
    ```
4. Iniciar el Servidor de Desarrollo**
    Ejecuta el servidor de desarrollo para iniciar RawGraphs en tu máquina local:

    ```bash
    npm start
    ```

    Esto iniciará un servidor local y RawGraphs estará accesible en tu navegador en la dirección [http://localhost:3000](http://localhost:3000).


### Paso 3: Crear Visualizaciones con RawGraphs

1. **Acceso al servicio**:
    - En el caso de que hayas instalado el servicio en local, accede a [http://localhost:3000](http://localhost:3000) en tu navegador.
    - Si has optado por usar la versión online, accede a [https://app.rawgraphs.io/](https://app.rawgraphs.io/)

2. **Subir datos para análisis**
    - Sube el archivo `m3_e8_datos_edificio_canarias.csv` o copia su contenido y pégalo.
    ![Carga de Datos](/ibbi/M3.%20Visualización%20e%20Interpretación%20de%20Datos/materiales/ayuda/rawgraphs-carga.png)

3. **Gráfico de barras**:
    1. Seleccionar el tipo de gráfico:
        - Elige un **Multi-set bar Chart** para visualizar la distribución del consumo por localización y mes.

    2. Configurar las dimensiones:
        - `Sets`:
            - Usa `Mes` (extraído de la columna `Fecha`).
        - `Size`:
            - Usa `Consumo Agua (L)` y `Consumo Energía (kWh)` como valor de tamaño de barra.
            En este punto veremos los valores acumulados para los 3 edificios.
        - `Series`:
            - Usa `Localización` para segmentar consumos por edificios.
        
    3. **Personalizar el gráfico**:
        - Ajusta colores, etiquetas y estilo.
        - Fija el alto del gráfico a 800 pixeles.
        - Fija las series a 3 columnas.
        - Ajusta el ancho a 400 píxeles.

        ![Personalización de Gráfico de Barras](/ibbi/M3.%20Visualización%20e%20Interpretación%20de%20Datos/materiales/ayuda/rawgraphs-bar.png)

4. **Gráfico de línea**:
    1. Seleccionar el tipo de gráfico:
        - Elige un **Line Chart** para visualizar la evolución del consumo por localización y mes.

    2. Configurar las dimensiones:
        - `X Axis`:
            - Usa `Fecha`.
        - `Y Axis`:
            - Usa `Consumo Agua (L)` o `Consumo Energía (kWh)` como valor en eje Y.
        - `Lines`:
            - Usa `Localización` para segmentar consumos por edificios.
        - `Colors`:
            - Usa también `Localización` para representar líneas de diferentes colores por edificio.
        
    3. **Personalizar el gráfico**:
        - Ajusta colores, etiquetas y estilo.
        - Fija el alto del gráfico a 800 pixeles.
        - Ajusta el ancho a 500 píxeles.

        ![Personalización de Gráfico de Líneas](/ibbi/M3.%20Visualización%20e%20Interpretación%20de%20Datos/materiales/ayuda/rawgraphs-line.png)

4. **Gráfico de burbujas**:
    1. Seleccionar el tipo de gráfico:
        - Elige un **Bubble Chart** para visualizar la correlación entre Radiación Solar y Generación FV.

    2. Configurar las dimensiones:
        - `X Axis`:
            - Usa `Generación FV (kWh)`.
        - `Y Axis`:
            - Usa `Radiación Solar (W/m2)` como valor en eje Y.
        - `Color`:
            - Usa `Mes` para diferenciar visualmente por meses.
        - `Size`:
            - Si usamos `Radiación Solar (W/m2)` podremos aosciar el tamaño de las burbujas al nivel de radiación solar.
        
    3. **Personalizar el gráfico**:
        - Ajusta colores a secuencia de rojos.
        - Fija el alto del gráfico a 800 pixeles.
        - Ajusta el ancho a 600 píxeles.

        ![Personalización de Gráfico de Burbujas](/ibbi/M3.%20Visualización%20e%20Interpretación%20de%20Datos/materiales/ayuda/rawgraphs-bubble.png)

---

## 4. Conclusión

En este ejercicio, aprendimos a utilizar **RawGraphs**, una herramienta autoalojado potente, para visualizar relaciones complejas en datos. La capacidad de RawGraphs para manejar dimensiones múltiples lo convierte en una opción ideal para explorar patrones en datasets con varias categorías. Aunque su interactividad es menor que la de herramientas como Dash/Plotly, su enfoque en gráficos especializados y su facilidad de uso lo hacen destacar.

---

## 5. Referencias y Ayuda

1. **RawGraphs**: [https://rawgraphs.io/](https://rawgraphs.io/)
2. **Tutoriales de RawGraphs**: [https://www.rawgraphs.io/learning](https://www.rawgraphs.io/learning)
3. **Ejemplos de Visualizaciones**: [https://rawgraphs.io/gallery/](https://rawgraphs.io/gallery/)