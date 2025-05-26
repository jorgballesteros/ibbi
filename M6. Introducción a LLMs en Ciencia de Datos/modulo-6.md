# Módulo 6: Introducción a Modelos de Lenguaje en Ciencia de Datos

**Duración total:** 6 horas lectivas + 3 horas de trabajo autónomo  
**Objetivo general:** Aprender a utilizar modelos de lenguaje (LLMs) para consultar, analizar e interpretar datos mediante lenguaje natural, integrándolos con herramientas de ciencia de datos como Pandas y visualización automática.

---

## 📅 Sesión 1 (3h): Introducción al uso de LLMs para análisis de datos

### Parte teórica (30 min)

- ¿Qué es un LLM y cómo se relaciona con la ciencia de datos?
- Introducción a la arquitectura **Transformer** (explicación + gráfico).
- Casos de uso de LLMs para análisis de datos.
- ¿Qué es un *prompt* y cómo influye en los resultados?
- Buenas prácticas para redactar instrucciones claras a un modelo.

📎 Recursos:
- [ChatGPT (OpenAI)](https://chat.openai.com/)
- [Gemini (Google)](https://gemini.google.com/)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/gpt-best-practices)

---

### Ejercicios prácticos

1. **Ejercicio 1 – Buenas prácticas con prompts**  
   Comparativa entre prompts vagos y precisos. Exploración de un dataset con consumo energético (`consumo_diario.csv`).

2. **Ejercicio 2 – Análisis exploratorio automático con un modelo de lenguaje**  
   Usar lenguaje natural para describir y graficar datos directamente con un LLM.

3. **Ejercicio 3 - Generación de código con un LLM**
   Aprender a utilizar un modelo de lenguaje para generar código Python que permita analizar datos

4. **Ejercicio 4 – Detección de anomalías en series temporales**  
   Uso de LLM para detectar consumos anómalos (outliers) en una serie temporal y generar visualizaciones marcando esos valores.

### Agenda de la sesión 1

| Tiempo estimado | Actividad | Contenido | Herramientas |
|-----------------|-----------|-----------|--------------|
| **0:00 - 0:30** | 🧠 **Introducción teórica** | - ¿Qué es un LLM? <br> - ¿Cómo funciona un Transformer? <br> - Aplicaciones en análisis de datos <br> - Qué es un *prompt* y cómo diseñarlo correctamente | Presentación con visuales + ejemplos en vivo |
| **0:30 - 1:00** | 🧪 **Ejercicio 1 – Buenas prácticas con prompts** | - Subida de `consumo_diario.csv` <br> - Comparativa entre prompts vagos vs estructurados <br> - Extraer estructura del dataset y detectar valores nulos | ChatGPT o Gemini |
| **1:00 - 1:30** | 🧪 **Ejercicio 2 – Análisis exploratorio automático** | - Pedir resúmenes y estadísticas básicas al modelo <br> - Generar un gráfico simple desde lenguaje natural <br> - Interpretar y corregir salidas del modelo | ChatGPT o Gemini |
| **1:30 - 2:15** | 🧪 **Ejercicio 3 – Generación de código con un LLM** | - Solicitar código Python (Pandas + Matplotlib) desde un prompt <br> - Ejecutar el código en VSCode <br> - Verificar funcionamiento y modificar visualización | ChatGPT + VSCode |
| **2:15 - 2:45** | 🧪 **Ejercicio 4 – Detección de anomalías en series temporales** | - Pedir al LLM que detecte outliers <br> - Visualizar puntos anómalos en rojo <br> - Generar y analizar el código subyacente | ChatGPT + VSCode |
| **2:45 - 3:00** | 💬 **Cierre y reflexión + explicación de la tarea** | - Discusión sobre fortalezas y limitaciones de los LLMs <br> - Consejos para seguir explorando en casa <br> - Entrega de la tarea autónoma: analizar un dataset propio | Debate abierto + instrucciones escritas |

---

### 🏠 Tarea para casa (1.5h)

> **Título:** Explorando tu propio dataset con un modelo de lenguaje

**Descripción:**  
El alumnado seleccionará o reutilizará un dataset sencillo (agua, energía, temperatura, etc.) y realizará:
- Un análisis descriptivo con prompts en ChatGPT o Gemini.
- Un intento de detección de valores anómalos.
- Una visualización generada con ayuda del modelo.

**Entrega:** Captura de pantalla de los resultados + breve reflexión (máx. 300 palabras)

---

## 📅 Sesión 2 (3h): Consulta y análisis de datos con herramientas LLM

**Duración:** 3h lectivas + 1.5h de trabajo autónomo  
**Objetivo:** Explorar y comparar herramientas que permiten interactuar con datasets mediante lenguaje natural, sin necesidad de conocimientos avanzados de programación.

### Parte teórica (30 minutos)

- ¿Qué son los LLM agents aplicados a datos?
- ¿Qué ventajas ofrecen frente a código tradicional?
- Diferencias entre asistentes conversacionales (Claude, ChatGPT) y agentes integrados en herramientas (Copilot, LangChain).
- Presentación de herramientas seleccionadas:
  - Claude Artifacts
  - Julius AI
  - GitHub Copilot en Notebooks
  - LangChain Tabular Agent
- Comparativa de sus capacidades: tipo de interacción, trazabilidad, requisitos técnicos, contexto ideal.

---

### Ejercicio 1 – *Claude Artifacts para análisis sin código*
- Cargar CSV y realizar preguntas sobre consumo y temperatura.
- Generar artefactos visuales reutilizables.
- Explorar patrones y generar informes automáticos.

### Ejercicio 2 – *Exploración de datos con Julius AI*
- Análisis de un CSV multivariable sin código ni instalación.
- Preguntas creativas sobre consumo, condiciones ambientales y relaciones.
- Comparación con Claude.

### Ejercicio 3 – *Análisis asistido con GitHub Copilot en VSCode*
- Escribir comentarios en celdas que Copilot convierte en código Python.
- Gráficos, estadísticas y explicación automática del código.
- Uso de `m6_consumo_agua.csv`.

### Ejercicio 4 – *Agente inteligente para análisis multivariable con LangChain Tabular Agent*
- Crear un agente con GPT-4 y conectar un DataFrame multivariable.
- Consultas como “días con mayor ratio agua/energía” o “detección de valores faltantes”.
- Comparativa entre herramientas.

---

### Desglose esquemático – Módulo 6, Sesión 2

| Tiempo        | Actividad                                       | Herramienta               |
|---------------|--------------------------------------------------|----------------------------|
| 0:00 – 0:30   | Introducción y repaso teórico                   | Presentación + demostración |
| 0:30 – 1:05   | Claude Artifacts: exploración sin código        | Claude.ai                  |
| 1:05 – 1:40   | Julius AI: visualización y resúmenes            | Julius.ai                  |
| 1:40 – 2:15   | GitHub Copilot en Jupyter                       | VSCode + Copilot           |
| 2:15 – 2:50   | LangChain Tabular Agent (avanzado)              | LangChain + GPT-4          |
| 2:50 – 3:00   | Cierre y explicación de la tarea                | Debate abierto             |

---

### 🏠 Tarea para casa (1.5h)

#### **Título:** Compara dos herramientas conversacionales para análisis de datos

**Descripción:**  
El alumnado debe elegir dos de las herramientas vistas en clase (Claude, Julius AI, Copilot o LangChain) y realizar las siguientes tareas:

- Cargar un nuevo dataset (puede ser una versión reducida del que trabajamos en clase).
- Hacer al menos **3 preguntas analíticas** en lenguaje natural.
- **Comparar los resultados, explicaciones y facilidad de uso.**
- Incluir al menos una visualización generada por cada herramienta.

**Formato de entrega:**  
- PDF o `.ipynb` con capturas, resultados y reflexión breve (máx. 400 palabras).

---

### Resultados esperados

Al finalizar esta sesión, el profesorado será capaz de:

- Comprender los distintos enfoques para consultar datos con LLMs.
- Utilizar asistentes como Copilot o Claude para analizar datos sin conocimientos profundos de código.
- Evaluar el potencial de herramientas como LangChain para proyectos educativos más avanzados.
- Comparar herramientas según facilidad, transparencia y aplicabilidad.
- Reflexionar sobre el uso de IA conversacional en el aula y proyectos docentes.
