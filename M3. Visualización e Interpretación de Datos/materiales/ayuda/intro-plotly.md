# **¿Qué es Plotly?**

**Plotly** es una biblioteca de visualización de datos interactiva y de código abierto para **Python**, **R**, **JavaScript**, y otros lenguajes. Es ampliamente utilizada en análisis de datos, ciencia de datos, y creación de dashboards debido a su capacidad para generar gráficos visualmente atractivos, interactivos y altamente personalizables.

---

## **Características Principales**

1. **Visualizaciones Interactivas**:
   - Los gráficos creados con Plotly permiten interacciones como:
     - Zoom.
     - Pan.
     - Hover (información contextual al pasar el cursor).
     - Selección de subconjuntos de datos.

2. **Variedad de Gráficos**:
   - Gráficos básicos: Barras, líneas, dispersión, histogramas.
   - Gráficos avanzados: Mapas coropléticos, diagramas de Sankey, gráficos 3D.
   - Gráficos estadísticos: Box plots, violín, densidad de kernel.

3. **Compatibilidad Multiplataforma**:
   - Funciona tanto en notebooks Jupyter como en scripts y aplicaciones web.

4. **Integración con Dash**:
   - Plotly se integra perfectamente con **Dash**, una biblioteca que permite crear aplicaciones web interactivas para visualización de datos.

5. **Opciones de Exportación**:
   - Gráficos interactivos (`HTML`) para compartir fácilmente.
   - Exportación de gráficos estáticos (`PNG`, `SVG`, `PDF`).

---

## **¿Para Qué Sirve Plotly?**

- **Exploración de Datos**:
  - Analizar tendencias y patrones en datos complejos con gráficos interactivos.
  
- **Presentaciones y Dashboards**:
  - Crear visualizaciones profesionales para informes y presentaciones.
  
- **Análisis en Tiempo Real**:
  - Monitoreo de sistemas o procesos con gráficos que se actualizan dinámicamente.
  
- **Ciencia de Datos y Machine Learning**:
  - Visualizar resultados de modelos y métricas con claridad.

---

## **Conceptos Clave**

1. **Zoom y Pan**:
   - Permite acercar y desplazar gráficos dinámicamente.
   - Control interactivo directamente desde el gráfico.

2. **Hover (Información Contextual)**:
   - Muestra detalles al pasar el cursor sobre los puntos, líneas o barras.
   - Personalizable para mostrar campos específicos.

3. **Selección de Datos**:
   - Herramientas de selección (rectangular, lazo) para resaltar subconjuntos de datos.
   - Útil para análisis interactivo en gráficos de dispersión o mapas.

4. **Actualizaciones Dinámicas**:
   - Los gráficos se pueden actualizar en tiempo real mediante callbacks (ej. usando Dash).
   - Ideal para datos que cambian continuamente (como monitoreo de sistemas).

5. **Filtros y Animaciones**:
   - Usa `animation_frame` para crear gráficos animados basados en datos temporales.
   - Interactúa con deslizadores o botones para filtrar y explorar datos.

6. **Gráficos Enlazados (Linked Charts)**:
   - Acciones como zoom o selección en un gráfico afectan otros gráficos relacionados.
   - Ejemplo: seleccionar un subconjunto en un gráfico de dispersión y ver cómo se reflejan en un gráfico de barras.

7. **Exportación Interactiva**:
   - Guarda gráficos como archivos `HTML` que conservan toda la interactividad para compartirlos fácilmente.

---

## Funcionalidad

### **1. Estructura Básica: Figuras y Trazas**
- **Figura** (`Figure`): Es el contenedor principal donde se incluyen todos los elementos de un gráfico (ejes, leyendas, títulos, etc.).
- **Trazas** (`Trace`): Cada conjunto de datos que se representa en la figura. Por ejemplo, una línea en un gráfico de líneas o una barra en un gráfico de barras.
  - Ejemplo: En un gráfico con dos líneas, cada línea es una traza separada.
  
```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[10, 15, 13], mode='lines', name='Línea 1'))
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[20, 25, 23], mode='lines', name='Línea 2'))
fig.show()
```

---

### **2. Módulos Principales**
- **`plotly.express`**:
  - Módulo fácil de usar para crear gráficos rápidamente con menos código.
  - Ejemplo: Gráficos de líneas, barras, dispersión, histogramas.
  - Ideal para análisis exploratorio.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Iris Data")
fig.show()
```

- **`plotly.graph_objects`**:
  - Módulo avanzado para personalizar gráficos a nivel detallado.
  - Más control sobre trazas, ejes y estilos.

---

### **3. Interactividad**
Los gráficos de Plotly son interactivos por defecto, lo que permite:
- **Zoom y Pan**: Acercar o mover el gráfico.
- **Hover**: Mostrar información detallada al pasar el cursor sobre un punto.
- **Selección**: Seleccionar subconjuntos de datos.
- **Actualizaciones Dinámicas**: Actualizar gráficos en tiempo real con herramientas como Dash.

---

### **4. Subplots y Ejes Secundarios**
- **Subplots**: Permiten combinar varios gráficos en una cuadrícula.
- **Ejes Secundarios**: Agregar un segundo eje Y a una gráfica.

Ejemplo de subplots con dos filas y dos columnas:
```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, subplot_titles=("Gráfico 1", "Gráfico 2", "Gráfico 3", "Gráfico 4"))
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines'), row=1, col=1)
fig.add_trace(go.Bar(x=[1, 2, 3], y=[6, 5, 4]), row=1, col=2)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[7, 8, 9], mode='markers'), row=2, col=1)
fig.add_trace(go.Bar(x=[1, 2, 3], y=[3, 2, 1]), row=2, col=2)
fig.update_layout(height=600, width=800, title_text="Subplots Ejemplo")
fig.show()
```

---

### **5. Exportación y Compartición**
- **Guardar Gráficos**:
  - Estáticos (`PNG`, `JPEG`, `PDF`, `SVG`) con:
    ```python
    fig.write_image("grafico.png")
    ```
  - Interactivos (`HTML`) para compartir gráficos que conserven interactividad:
    ```python
    fig.write_html("grafico.html")
    ```
- **Integración**:
  - Compatible con Dash para crear dashboards interactivos.
  - Puede incrustarse en sitios web o aplicaciones.

---

### **6. Conceptos Relacionados**
- **Ejes Personalizados**: `update_layout` para personalizar títulos, colores y estilos.
- **Colores y Paletas**: Personalizar paletas con `px` o `go`.
- **Filtros y Animaciones**: Usar `animation_frame` o `animation_group` en `px`.

### **Casos de Uso**
1. **Análisis de Series Temporales** (por ejemplo, ventas mensuales).
2. **Gráficos Estadísticos** (distribuciones, correlaciones).
3. **Visualización Geoespacial** (mapas interactivos).
4. **Dashboards Corporativos** (con gráficos actualizables).
5. **Informes Educativos y Científicos**.
