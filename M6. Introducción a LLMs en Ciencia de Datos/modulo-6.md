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
