# 🧪 Ejercicio 2 – Exploración de datos con Julius AI

## 🎯 Objetivo

Explorar un conjunto de datos subido por el usuario usando **Julius AI**, realizando preguntas en lenguaje natural para obtener estadísticas, gráficos e insights sin escribir código.


## 🧠 ¿Qué es Julius AI?

[Julius AI](https://www.julius.ai/) es una herramienta de análisis de datos basada en inteligencia artificial que permite subir archivos y analizarlos mediante lenguaje natural, sin necesidad de programar. El modelo interpreta las preguntas y responde con textos, tablas o visualizaciones directamente en el navegador. Permite realizar acciones como:
 - Explorar datos.
 - Visualizar información.
 - Obtener insights.
 - Generar resúmenes y explicaciones.
 - Crear informes.

Está enfocado a usuarios sin conocimientos técnicos y se puede utilizar directamente desde el navegador, sin instalar nada.

## 📁 Dataset para el ejercicio

Usaremos el mismo archivo de ejercicios anteriores: `m6_consumo_eneergia.csv`, con las siguientes columnas:

```
Fecha,Energia Consumida,Temperatura,Humedad
2024-07-01,191.15,21.71,76.765
2024-07-02,185.83,21.969,73.388
2024-07-03,200.53,22.129,73.098
2024-07-04,197.76,22.161,75.965
2024-07-05,196.79,21.929,76.122
```

---

## 🧪 Paso a paso del ejercicio

### 🔹 Paso 1 – Accede a Julius

1. Ve a [https://www.julius.ai/](https://www.julius.ai/)
2. Inicia sesión con tu cuenta de Google o regístrate (gratuito).
3. Crea un nuevo proyecto haciendo clic en **“New Analysis”**.

---

### 🔹 Paso 2 – Sube el archivo CSV

1. En la interfaz, selecciona “Upload file”.
2. Sube el archivo `m6_consumo_eneergia.csv`.
3. Julius mostrará una vista previa de los datos y habilitará el campo de texto para hacer preguntas.

---

### 🔹 Paso 3 – Realiza preguntas al modelo

Puedes escribir tus preguntas directamente. Algunos ejemplos útiles:

```plaintext
1. ¿Cuál es el promedio del consumo energético?
2. ¿Qué día tuvo el mayor consumo de agua?
3. ¿Puedes crear un gráfico de líneas del consumo energético diario?
4. ¿Hay algún valor atípico en el consumo eléctrico?
5. ¿Existe correlación entre la temperatura y el consumo energético?
```

> Julius generará visualizaciones interactivas, gráficos, estadísticas y explicaciones automáticas.

---

## 📊 Resultados esperados

- Una tabla con estadísticas resumen.
- Gráficos simples y automáticos (líneas, barras, etc.).
- Resúmenes de insights en lenguaje natural.
- Explicaciones sobre valores extremos si se detectan.

---

## 🧠 Preguntas para discusión

- ¿Qué tipo de preguntas devuelve mejores resultados?
- ¿Es fácil interpretar las respuestas del modelo?
- ¿Cómo se compara la experiencia de uso con Claude o ChatGPT?

---

## 💡 Variante opcional (para ampliar)

Pide a Julius que **genere un resumen ejecutivo del análisis**:

```plaintext
Resume en un informe los patrones de consumo energético y de agua observados en el archivo.
```

> También puedes exportar visualizaciones desde Julius para usarlas en una presentación.

---

## ✅ Conclusiones

Es una herramienta bastante interesante que se posiciona como una solución de **“análisis de datos asistido por IA sin necesidad de programar”**, muy útil para contextos educativos.

---

### 🔍 Diferencias entre Julius AI, Claude Artifacts y ChatGPT

| Característica              | Julius AI                                | Claude Artifacts                          | ChatGPT + Code Interpreter               |
|----------------------------|-------------------------------------------|--------------------------------------------|-------------------------------------------|
| **Plataforma**             | Web (https://www.julius.ai/)             | Web (https://claude.ai/)                  | Web (https://chat.openai.com/)           |
| **Requiere código**        | ❌ No                                     | ❌ No                                      | ✅ Sí (aunque lo escribe por ti)          |
| **Tipo de respuesta**      | Texto + gráficos integrados              | Artifacts (gráficos, tablas, texto)       | Código ejecutable, resultados dinámicos   |
| **Carga de datos**         | Archivos o conexión a base de datos      | Archivos (CSV, Excel, etc.)               | Archivos (CSV, Excel), edita y ejecuta    |
| **Análisis exploratorio**  | ✅ Muy bueno y accesible                  | ✅ Muy bueno con visuales reutilizables    | ✅ Avanzado y altamente personalizable     |
| **Control del usuario**    | Medio (menos técnico, más guiado)        | Alto (puedes ajustar prompts)             | Alto (puedes editar código y repetirlo)   |
| **Visualización**          | Gráficos automáticos integrados          | Artifacts reutilizables e interactivos     | Genera gráficos con `matplotlib`, etc.    |
| **Uso ideal**              | Presentaciones, informes rápidos, docencia básica | Docencia interactiva, prototipos rápidos | Análisis técnico, desarrollo y validación |

---

### ✅ ¿Cuándo usar Julius AI?

Es ideal para:
- Profesorado sin experiencia en programación.
- Sesiones demostrativas rápidas.
- Casos en los que se quiera **analizar datos sin tocar código**.
- Crear informes automáticos en lenguaje natural desde un Excel.

---

### 💬 ¿En qué destaca frente a Claude o ChatGPT?

- Tiene una interfaz **más sencilla y visual**.
- Muestra los resultados como **dashboards dinámicos**.
- Permite **exportar insights** en forma de reporte sin esfuerzo.
- No requiere cuentas de pago ni API keys.

---

## 🔗 Recursos complementarios

- 🌐 [Julius AI – Página oficial](https://www.julius.ai/)
- 📄 [Guía de introducción](https://www.julius.ai/blog/product-update-natural-language-data-analysis)
- 🎓 [Tutorial en vídeo (YouTube)](https://www.youtube.com/results?search_query=julius+ai+data+analysis)

---