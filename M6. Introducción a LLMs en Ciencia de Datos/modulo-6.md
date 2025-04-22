# Módulo 6: Introducción a Modelos de Lenguaje en Ciencia de Datos

**Duración total:** 6 horas lectivas + 3 horas de trabajo autónomo  
**Objetivo general:** Aprender a utilizar modelos de lenguaje (LLMs) para consultar, analizar e interpretar datos mediante lenguaje natural, integrándolos con herramientas de ciencia de datos como Pandas y visualización automática.

---

## Sesión 1 (3h): Introducción al uso de LLMs para análisis de datos

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

### Tarea para casa (1.5h)

> **Título:** Explorando tu propio dataset con un modelo de lenguaje

**Descripción:**  
El alumnado seleccionará o reutilizará un dataset sencillo (agua, energía, temperatura, etc.) y realizará:
- Un análisis descriptivo con prompts en ChatGPT o Gemini.
- Un intento de detección de valores anómalos.
- Una visualización generada con ayuda del modelo.

**Entrega:** Captura de pantalla de los resultados + breve reflexión (máx. 300 palabras)

---

## Sesión 2 (3h): Consultas en lenguaje natural con PandasAI, Nixtral y LangChain

### Parte teórica (30 min)

- ¿Qué es una interfaz de lenguaje natural para análisis de datos?
- Introducción a **PandasAI**, **Nixtral** y **LangChain Tabular Agents**
- Ventajas de usar estas herramientas frente a prompts manuales.
- Comparativa de sus enfoques, dependencias y usos recomendados.

📎 Recursos:
- [PandasAI en GitHub](https://github.com/gventuri/pandas-ai)
- [Nixtral](https://github.com/nixtral/nixtral)
- [LangChain para datos tabulares](https://python.langchain.com/docs/use_cases/tabular/)

---

### Ejercicios prácticos

1. **Ejercicio 1 – Análisis de datos con PandasAI**  
   - Cargar un DataFrame en Python y hacer preguntas en lenguaje natural.
   - Consultas como: "¿Cuál es el día de mayor consumo?" o "¿Puedes mostrar un gráfico de consumo mensual?"

2. **Ejercicio 2 – Uso de Nixtral para análisis y procesado de datos**  
   - Consultas sobre el mismo dataset.
   - Comparación de respuestas con PandasAI: precisión, trazabilidad, visualización.

3. **Ejercicio 3 – LangChain Tabular Agent (opcional según nivel)**  
   - Ejecutar un análisis más completo en lenguaje natural sobre datos multivariables (agua + energía + temperatura).
   - Discusión: ¿qué herramienta funcionó mejor?

---

### Agenda de la sesión 2

Perfecto, con esta incorporación el esquema de la **Sesión 2** quedaría actualizado con un nuevo ejercicio demostrativo enfocado en el uso de **GitHub Copilot en VSCode**. Aquí tienes la versión revisada:

---

### 🧩 **Desglose esquemático – Módulo 6, Sesión 2 (3h lectivas)**  
**Tema:** Librerías para análisis de datos en lenguaje natural con LLMs

| Tiempo estimado | Actividad | Contenido | Herramientas |
|-----------------|-----------|-----------|--------------|
| **0:00 - 0:30** | 🧠 **Introducción teórica** | - ¿Qué es una interfaz de lenguaje natural para análisis de datos? <br> - Comparativa: PandasAI, Nixtral, LangChain y Copilot <br> - Revisión de ventajas y limitaciones | Presentación con demos breves |
| **0:30 - 1:05** | 🧪 **Ejercicio 1 – Primeros pasos con PandasAI** | - Cargar un DataFrame <br> - Consultas simples y visualizaciones automáticas | VSCode + PandasAI |
| **1:05 - 1:40** | 🧪 **Ejercicio 2 – Análisis con Nixtral** | - Consultas avanzadas <br> - Comparación con PandasAI (precisión, explicaciones) | VSCode + Nixtral |
| **1:40 - 2:10** | 🧪 **Ejercicio 3 – LangChain Tabular Agent (opcional/avanzado)** | - Crear agente con capacidad para responder consultas en lenguaje natural <br> - Análisis multivariable | LangChain + OpenAI API |
| **2:10 - 2:40** | 🧪 **Ejercicio 4 – Demostración con GitHub Copilot en VSCode** | - Cómo funciona Copilot como asistente de código <br> - Generación de funciones de análisis y gráficos a partir de comentarios <br> - Evaluación crítica del resultado | VSCode con Copilot |
| **2:40 - 3:00** | 💬 **Cierre y reflexión + explicación de la tarea** | - ¿Qué herramienta fue más útil y por qué? <br> - Casos de uso reales <br> - Instrucciones para la tarea autónoma | Discusión + instrucciones |

---

### Tarea para casa (1.5h)

> **Título:** Consulta guiada sobre datos reales

**Descripción:**  
- Usar PandasAI o Nixtral para analizar un nuevo dataset (proporcionado o propio).
- Formular 3 preguntas relevantes en lenguaje natural.
- Generar al menos una visualización automática a partir de las respuestas.
- Comparar la experiencia con el uso directo de ChatGPT o Gemini en la primera sesión.

**Entrega:** Notebook con resultados + breve autoevaluación del proceso (máx. 400 palabras)

---

## Resultados esperados del módulo

- Comprensión básica del funcionamiento de los LLMs en el análisis de datos.
- Capacidad para formular prompts efectivos.
- Dominio inicial de herramientas como PandasAI, Nixtral y LangChain para consultar y visualizar datos.
- Habilidad para evaluar críticamente las respuestas generadas por modelos de lenguaje.
