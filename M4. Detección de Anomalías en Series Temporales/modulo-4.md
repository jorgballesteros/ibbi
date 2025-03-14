# **Módulo 4: Detección de Anomalías en Series Temporales con IA**

**Duración total:** 6 horas lectivas (2 sesiones de 3 horas cada una) + 3 horas de tarea en casa.

## **Objetivo General**

- Capacitar a los participantes para identificar anomalías en el consumo de recursos (energéticos y/o de agua) combinando técnicas estadísticas y modelos de IA.
- Destacar el potencial de la inteligencia artificial para automatizar y mejorar la detección en entornos reales, promoviendo el uso de herramientas low-code y soluciones accesibles para todos.

---

## **Sesión 1**

- **Duración:**  (3h lectivas + 1,5h trabajo en casa)

### **Contenidos y Actividades**

1. **Series Temporales y Preprocesamiento de Datos con IA**  
   - **Teoría (30 min):**
     - Conceptos básicos de series temporales: estacionalidad, tendencia, ruido y su importancia en la analítica.
     - Importancia del preprocesamiento de datos para alimentar modelos de IA: limpieza, imputación, normalización y transformaciones.
     - Presentación de herramientas de IA de nivel usuario para explorar datos:
       - [YData Profiling](https://docs.profiling.ydata.ai/latest/)
       - [PyGWalker](https://github.com/Kanaries/pygwalker)
       - [Metabase](https://www.metabase.com/)
   - **Práctica en clase (45 min):**
     - Carga y visualización de un dataset de consumo energético usando Python (pandas, matplotlib/Seaborn).
     - Demostración de técnicas de limpieza y transformación aplicadas en un entorno colaborativo.
     - Exploración rápida con una herramienta low-code para visualizar patrones en los datos.
   - **Trabajo en casa (1,5h):**
     - Ejercicio práctico: explorar y preprocesar un dataset alternativo (por ejemplo, datos de consumo de agua), utilizando tanto código en Python como una herramienta de IA low-code para identificar patrones.
     - Reflexión sobre las diferencias y ventajas de cada enfoque en el preprocesamiento.

2. **Detección de Anomalías: Métodos Estadísticos y Primeros Pasos con IA**  
   - **Teoría (30 min):**
     - Revisión de métodos estadísticos (medias móviles, z-scores, percentiles) y su aplicación en la detección de anomalías.
     - Introducción al uso de modelos de IA: presentación de técnicas como Isolation Forest, destacando su implementación y uso en entornos de bajo código.
   - **Práctica en clase (15 min):**
     - Implementación de un método estadístico sencillo en Python para detectar anomalías en el dataset preprocesado.
     - Discusión sobre cómo un enfoque híbrido (estadístico + IA) puede mejorar la detección.
   - **Comentario y debate:**
     - Conversación sobre casos de uso reales donde la integración de IA ha permitido optimizar la detección de anomalías en tiempo real.

---

## **Sesión 2**

- **Duración:**  (3h lectivas + 1,5h trabajo en casa)

### **Contenidos y Actividades**

1. **Modelos de IA para la Detección de Anomalías**  
   - **Teoría (30 min):**
     - Profundización en modelos de IA:  
       - **Isolation Forest:** Cómo funciona y su aplicación en series temporales.
       - **Autoencoders:** Conceptos básicos, su uso para detectar patrones y anomalías y cómo optimizarlos.
       - Breve introducción a técnicas basadas en redes neuronales recurrentes (por ejemplo, LSTM) para datos secuenciales.
     - Discusión sobre la integración de modelos de IA en herramientas de bajo código para facilitar su uso en entornos no expertos.
   - **Práctica en clase (1h):**
     - Implementación de un modelo de IA (Isolation Forest) utilizando scikit-learn en Python sobre el mismo dataset.
     - Visualización y análisis comparativo de los resultados obtenidos con el método estadístico implementado en la sesión 1.
     - Demostración de cómo replicar el análisis con una plataforma de IA low-code, permitiendo a los usuarios explorar ajustes y resultados sin programar en exceso.

2. **Evaluación y Validación de Modelos con Enfoque en IA**  
   - **Teoría y práctica (45 min):**
     - Introducción a métricas de evaluación: precisión, recall, F1-score y nociones básicas de la curva ROC, enfocando cómo interpretarlas en modelos de IA.
     - Ejercicio práctico: cálculo de las métricas para evaluar ambos métodos (estadístico y basado en IA) y discusión sobre cuál se adapta mejor a diferentes escenarios.
     - Enfatizar la importancia de la validación cruzada en series temporales para garantizar resultados robustos.

3. **Caso Práctico Integrado: Consumo Energético con Soluciones IA**  
   - **Actividad final en clase (15 min):**
     - Desarrollo de un mini proyecto integrador: los participantes, de forma individual o en grupos, planifican una estrategia para la detección de anomalías en consumo energético, combinando métodos estadísticos e IA.
     - Elaboración de un esquema que detalle cómo se implementaría la solución utilizando tanto código en Python como herramientas de IA low-code.
   - **Trabajo en casa (1,5h):**
     - Elaborar un informe (2-3 páginas) en el que se describa el proceso de preprocesamiento, la implementación de los métodos (estadístico e IA) y un análisis comparativo de los resultados.
     - Incluir código en un notebook comentado y capturas de pantalla o resultados de la herramienta low-code, resaltando cómo la IA mejora la detección de anomalías.

---

### **Recursos y Herramientas Recomendadas**

- **Materiales:**
  - Presentación M4 iBBi [PDF](https://drive.google.com/file/d/1WaNfSmLGS5muRVlWIraAa_wmMXz6qJqj/view?usp=drive_link)
  - Repositorio de materiales en [Github](https://github.com/jorgballesteros):
    - Dataset de ejemplo (archivo CSV).
    - Ejercicios prácticos en notebooks.
    - Tutoriales y ayuda.
- **Python y Librerías:**
  - *pandas*, *matplotlib* y *Seaborn* para manejo y visualización de datos.
  - *scikit-learn* para la implementación de modelos de IA (Isolation Forest, etc.).
  - *Keras/TensorFlow* para explorar autoencoders (opcional según el nivel).
- **Plataformas de IA Low-Code/No-Code:**
  - Ydata Profiling, PyGWalker y otras herramientas similares para complementar la experiencia y facilitar la exploración de modelos.
  - Ydata Profiling, PyGWalker y otras herramientas similares para complementar la experiencia y facilitar la exploración de modelos.
- **Entornos de Desarrollo:**
  - [Google Colab](https://colab.research.google.com/) y [Jupyter Notebooks](https://jupyter.org/) para el desarrollo de código reproducible.
