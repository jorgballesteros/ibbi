
# Introducción a Modelos de Lenguaje

## ¿Qué es un Modelo de Lenguaje?

Un **Modelo de Lenguaje de gran tamaño** (LLM, por sus siglas en inglés) es una inteligencia artificial entrenada con enormes cantidades de texto para **entender y generar lenguaje humano**.  Estos modelos cuentan con una gran cantidad de parámetros y se entrenan mediante aprendizaje autosupervisado en vastos volúmenes de texto.

Un LLM se basa en una arquitectura llamada **Transformer**, introducida por Google en 2017. Esta arquitectura revolucionó el campo de la inteligencia artificial al permitir que los modelos procesen texto de forma paralela y contextual, entendiendo el significado de una palabra según su posición y relación con las demás. En lugar de leer palabra por palabra como lo haría un lector, los Transformers utilizan un **mecanismo llamado atención** (attention mechanism), que permite al modelo enfocarse en las partes más relevantes del texto para cada tarea.

![Componentes de una arquitectura de LLM](https://upload.wikimedia.org/wikipedia/commons/8/8f/The-Transformer-model-architecture.png)

Los LLMs han demostrado ser eficaces en una variedad de tareas lingüísticas, incluyendo la traducción, el resumen y la respuesta a preguntas. Su capacidad para manejar múltiples tareas sin necesidad de ajustes específicos los hace especialmente versátiles en el ámbito del procesamiento del lenguaje natural. 

Sin embargo, su entrenamiento y funcionamiento requieren considerables recursos computacionales y energéticos, lo que plantea desafíos en términos de sostenibilidad y accesibilidad. Además, es fundamental abordar cuestiones éticas relacionadas con posibles sesgos y la generación de información inexacta o engañosa.

Algunos ejemplos conocidos son **ChatGPT, Gemini, Claude** o **Copilot**.

- [ChatGPT (OpenAI)](https://chat.openai.com/)
- [Gemini (Google)](https://gemini.google.com/)
- [Claude (Anthropic)](https://claude.ai/)
- [Microsoft Copilot](https://copilot.microsoft.com/)

Estos modelos funcionan prediciendo la siguiente palabra o frase basándose en lo que se les ha dicho previamente. Ests modelos son capaces de **responder preguntas, redactar informes, generar código, resumir información e incluso analizar datos**.

> Un LLM es como un asistente que ha leído millones de libros, artículos, manuales y código. No sabe todo, pero tiene muy buena intuición sobre lo que probablemente tenga sentido decir o hacer.

### Enlaces de ineterés
 - [What are Large Language Models (LLMs)? (Google)](https://www.youtube.com/watch?v=iR2O2GPbB0E)
 - [Intro to Large Language Models (Andrej Karpathy)](https://www.youtube.com/watch?v=zjkBMFhNj_g&pp=ygUKcXVlIGVzIGxsbdIHCQl-CQGHKiGM7w%3D%3D)
 - [¿Qué son los Grandes Modelos de Lenguaje? 🤖 Explicación Sencilla de la IA Generativa](https://www.youtube.com/watch?v=0K5Knnq2ZRk)
 - [Transformers (how LLMs work) explained visually](https://www.youtube.com/watch?v=wjZofJX0v4M)
 - [AI, Machine Learning, Deep Learning and Generative AI Explained](https://www.youtube.com/watch?v=qYNweeDHiyU)
---

## ¿Cómo se usan los LLMs en ciencia de datos?

Los LLMs pueden ayudarnos en muchas tareas dentro del análisis de datos. Aquí tienes algunos ejemplos:

| Tarea | ¿Cómo puede ayudar un LLM? |
|------|-----------------------------|
| **Comprensión de datos** | Resumir el contenido de un dataset (columnas, tipos de datos, valores más frecuentes). |
| **Limpieza de datos** | Sugerir cómo tratar valores nulos, errores tipográficos o datos atípicos. |
| **Visualización** | Proponer y generar gráficos adecuados según el tipo de datos. |
| **Análisis exploratorio** | Detectar patrones, correlaciones y tendencias. |
| **Generación de código** | Escribir scripts en Python para analizar, visualizar o transformar datos. |
| **Generación de informes** | Redactar conclusiones o explicaciones en lenguaje natural a partir de los datos. |

---

## Modelos abiertos vs. cerrados

Existen dos tipos principales de LLMs:

- **Modelos cerrados**: como ChatGPT (OpenAI), Gemini (Google), Copilot (Microsoft). Están disponibles como servicios en línea, pero no podemos ver ni modificar su funcionamiento interno.
- **Modelos abiertos**: como Mistral, LLaMA o Falcon. Suelen ser más complejos de usar, pero permiten instalarse en servidores propios y personalizarse.

Para este curso, trabajaremos con modelos accesibles desde el navegador, como **ChatGPT** o **Gemini**, que no requieren instalación.

---

## ¿Qué es un prompt y por qué es tan importante?

Un **prompt** es simplemente el mensaje o pregunta que escribimos al modelo para que haga algo.

> *Ejemplo de prompt:*  
> “Crea un gráfico de barras que muestre la energía consumida por día a partir de este archivo CSV.”

Los resultados que obtengamos dependerán en gran medida de **cómo escribamos ese prompt**. Por eso, una parte clave de trabajar con LLMs es **aprender a comunicarse con ellos de forma clara y precisa**.

> **Guía recomendada:**  
> - [OpenAI - Prompt Engineering Guide](https://platform.openai.com/docs/guides/gpt-best-practices)  
> - [FlowGPT - Prompt Library](https://flowgpt.com/) (ejemplos listos para usar)

---

## Buenas prácticas para escribir prompts

1. ✅ Sé claro y directo: indica qué quieres hacer y con qué datos.
2. ✅ Da contexto: si estás usando un archivo CSV, describe su contenido o súbelo si la herramienta lo permite.
3. ✅ Pide paso a paso: los LLMs funcionan mejor si se les pide que resuelvan problemas por partes.
4. ✅ Revísalo todo: los modelos pueden equivocarse o asumir cosas erróneas. Revisa siempre los resultados.

> Consejo útil:  
> Si algo no funciona bien, intenta reformular tu pregunta o ser más específico. ¡Los LLMs aprenden de tus instrucciones!

---

## ¿Qué vamos a aprender?

En esta primera sesión veremos cómo:

- Usar un LLM para explorar un archivo CSV sin escribir una sola línea de código.
- Pedirle que genere visualizaciones o estadísticas básicas.
- Obtener código en Python para reproducir esos análisis.
- Evaluar si lo que ha generado tiene sentido o si necesita ajustes.

> **Herramientas que se usarán en la sesión:**
> - [ChatGPT con Code Interpreter (GPT-4)](https://chat.openai.com/)
> - [Gemini (Google) con análisis de archivos](https://gemini.google.com/)
> - [Google Colab](https://colab.research.google.com/) o [Jupyter Notebooks](https://jupyter.org/) para probar el código generado
