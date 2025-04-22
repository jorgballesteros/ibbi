# 🧪 Ejercicio 4 – Agente inteligente para análisis multivariable con LangChain Tabular Agent

---

## 🎯 Objetivo

Utilizar un agente conversacional construido con **LangChain** para explorar un conjunto de datos multivariables, identificar relaciones complejas y generar visualizaciones a partir de lenguaje natural. El alumnado aprenderá a usar esta herramienta para analizar correlaciones, detectar anomalías y generar resúmenes automáticos.

---

## 🧠 ¿Qué es LangChain?

[LangChain](https://www.langchain.com/) es un framework en Python diseñado para construir aplicaciones impulsadas por modelos de lenguaje (LLMs), como asistentes conversacionales, analistas de datos o buscadores inteligentes. 

Lo que lo diferencia de otros enfoques es su capacidad de **conectar un LLM con fuentes externas**, como:
- Archivos (CSV, PDFs)
- Bases de datos
- APIs
- Documentos complejos
- Y en este caso, **DataFrames de Pandas**

Con el **Tabular Agent**, LangChain convierte cualquier DataFrame en un sistema conversacional capaz de responder preguntas, generar visualizaciones y ejecutar análisis complejos con trazabilidad y control.

---

## 📁 Dataset utilizado: `m6_consumo_combinado.csv`

Este dataset contiene información diaria de consumo de agua y energía, junto con variables ambientales (temperatura y humedad):

```
Índice,Fecha,Consumo_Agua,Temperatura,Consumo_Energia,Humedad
0,2024-07-01,4794.0,21.71,191.15,76.765
1,2024-07-02,4392.0,21.969,185.83,73.388
2,2024-07-03,4206.0,22.129,200.53,73.098
3,2024-07-04,5038.0,22.161,197.76,75.965
4,2024-07-05,5881.0,21.929,196.79,76.122
5,2024-07-06,541.0,21.888,,79.091
6,2024-07-07,879.0,21.828,144.36,77.684
7,2024-07-08,5484.0,21.505,188.83,75.153
```

---

## 🛠️ Requisitos

```bash
pip install langchain openai pandas matplotlib
```

Además, necesitarás una clave de API de OpenAI con acceso a GPT-4.

---

## 🧪 Paso a paso

### 🔹 Paso 1 – Preparar el entorno

```python
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd

# Cargar datos
df = pd.read_csv("m6_consumo_combinado.csv", index_col="Fecha", parse_dates=True)

# Inicializar el LLM
llm = OpenAI(temperature=0, model_name="gpt-4", openai_api_key="TU_API_KEY")

# Crear el agente
agent = create_pandas_dataframe_agent(llm, df, verbose=True)
```

---

### 🔹 Paso 2 – Consultas en lenguaje natural

A continuación, puedes lanzar preguntas como:

```python
agent.run("¿Qué día se detecta el consumo más bajo de agua y qué condiciones ambientales lo acompañan?")
agent.run("¿Existe relación entre humedad y consumo energético?")
agent.run("Haz un gráfico de líneas con la evolución diaria de consumo de agua y energía en el mismo eje temporal.")
agent.run("¿Cuántos días tienen datos faltantes y cómo podría imputarse la energía faltante?")
agent.run("Calcula el ratio entre consumo de agua y energía por día y ordénalos de mayor a menor.")
agent.run("Redacta un informe breve que resuma los patrones de consumo observados.")
```

---

## 📊 Resultados esperados

- Tablas con rankings y filtrados condicionales.
- Gráficos combinados (`matplotlib`) generados automáticamente.
- Análisis de correlación y métricas personalizadas.
- Códigos ejecutables transparentes generados por el agente.
- Informes automáticos en texto redactado por el LLM.

---

## 🧠 Comparativa: LangChain vs otras herramientas de análisis con LLM

| Herramienta         | Interfaz         | Requiere codificación | Permite personalización | Trazabilidad del análisis | Uso recomendado |
|---------------------|------------------|------------------------|--------------------------|----------------------------|-----------------|
| **LangChain**       | Python (Agentes) | ✅ Sí                  | ✅ Alta                  | ✅ Muestra código y lo ejecuta | Desarrollo de herramientas personalizadas |
| **Claude Artifacts**| Navegador        | ❌ No                  | ⚠️ Limitada              | ✅ Alta visual (reutilizable) | Análisis interactivo sin código |
| **ChatGPT+Code**    | Navegador        | ❌ / ✅ Opcional        | ✅ Media                 | ✅ Código visible           | Exploración rápida de datos |
| **Copilot**         | VSCode           | ✅ Sí (pero asistido)  | ✅ Alta                  | ⚠️ Parcial                 | Escribir código acompañado |
| **Julius AI**       | Navegador        | ❌ No                  | ❌ Baja                  | ❌ No ejecuta código        | Usuario sin experiencia técnica |

---

## ✅ Conclusiones

- LangChain permite crear **agentes inteligentes capaces de analizar datasets reales** de forma autónoma y conversacional.
- Ideal para **proyectos educativos avanzados**, integración en apps, o exploración reproducible.
- Requiere algo más de configuración inicial, pero ofrece una experiencia robusta y transparente.

---

## 🔗 Recursos complementarios

- 📘 [Guía oficial del Tabular Agent](https://python.langchain.com/docs/use_cases/tabular/)
- 🧪 [Documentación LangChain](https://github.com/langchain-ai/langchain)