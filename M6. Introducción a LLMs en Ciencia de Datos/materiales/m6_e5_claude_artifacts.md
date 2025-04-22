# 🧪 Ejercicio 1 – Claude Artifacts para análisis sin código

## 🎯 Objetivo

Aprender a utilizar **Claude Artifacts**, una funcionalidad integrada en [Claude.ai](https://claude.ai/) que permite analizar archivos cargados (CSV, Excel, etc.) directamente desde el navegador, mediante lenguaje natural. El alumnado explorará, visualizará y extraerá conclusiones de un dataset sin necesidad de programar.

## 🧠 ¿Qué son los Artifacts de Claude?

Los **Artifacts** son elementos interactivos creados por el modelo Claude (de Anthropic) al trabajar con archivos, especialmente datos. Cuando subes un archivo, Claude puede crear vistas dinámicas (gráficas, tablas, resúmenes) que se muestran en pantalla y se pueden reutilizar o modificar mediante nuevas instrucciones.

## 📁 Dataset para el ejercicio

Usaremos el archivo `m6_consumo_energia_a.csv` con columnas como:

```
Fecha,Energia Consumida,Temperatura,Humedad
2024-07-01,191.15,21.71,76.765
2024-07-02,185.83,21.969,73.388
2024-07-03,200.53,22.129,73.098
2024-07-04,197.76,22.161,75.965
2024-07-05,196.79,21.929,76.122
```

## 🧪 Paso a paso del ejercicio

### 🔹 Paso 1 – Acceder a Claude

1. Ir a [https://claude.ai/](https://claude.ai/) (requiere cuenta gratuita).
2. Seleccionar el modelo **Claude 3.7 Sonnet** o similar (según disponibilidad).
3. Crear un nuevo chat.

---

### 🔹 Paso 2 – Subir el archivo

1. Arrastra el archivo `m6_consumo_energia_a.csv` al chat.
2. Espera a que Claude reconozca los datos y proponga una tabla interactiva.

---

### 🔹 Paso 3 – Realizar preguntas al modelo

**Prompts sugeridos:**

```plaintext
He subido un archivo CSV con datos de consumo de energía por hora. Haz un resumen estadístico, un gráfico de consumo diario y dime si hay anomalías en el dataset.
```

Claude generará **Artifacts** como tablas, gráficos o explicaciones textuales, que se visualizarán en el lateral del chat.

---

## 📊 Resultados esperados

- Resumen estadístico del dataset (media, máximo, mínimo, etc).
- Gráficos interactivos creados automáticamente.
- Anomalías y detalles sobre valores extremos.

---

## 🧠 Discusión y análisis

**Preguntas para el grupo:**

- ¿Qué ventajas ofrece Claude frente a otras herramientas?
- ¿Cuándo es útil usar un LLM como asistente de análisis?
- ¿Qué información adicional te gustaría obtener?

---

## 🧩 Prompts adicionales

Perfecto, aquí tienes un **cuadro de referencia en formato Markdown** con ideas de prompts útiles y pedagógicos para usar con **Claude Artifacts**. Este recurso puede incluirse como anexo en el módulo o entregarse al profesorado como plantilla de uso en el aula.

---

```markdown
# 💬 Guía de Prompts para Claude Artifacts  
*Análisis exploratorio de datos en lenguaje natural*

Claude Artifacts permite interactuar con datos sin escribir código. A continuación se presentan ejemplos de preguntas útiles y didácticas para explorar todo su potencial.

---

## 📊 Estadística descriptiva

| Tipo de análisis | Prompt sugerido |
|------------------|-----------------|
| Media por variable | ¿Puedes mostrarme los valores promedio de cada columna? |
| Mediana y desviación | ¿Cuál es la mediana y la desviación estándar de cada variable? |
| Valores por encima del promedio | ¿Qué filas tienen valores por encima de la media en consumo energético? |

---

## 📉 Series temporales

| Tipo de análisis | Prompt sugerido |
|------------------|-----------------|
| Tendencia de consumo | ¿Puedes crear un gráfico de líneas del consumo energético a lo largo del tiempo? |
| Evolución parcial | ¿Qué tendencia se observa en el consumo de agua durante los primeros 10 días? |
| Comportamiento diario | ¿Cuál fue el consumo total por día y su variación? |

---

## 🚨 Detección de anomalías

| Tipo de análisis | Prompt sugerido |
|------------------|-----------------|
| Identificación de outliers | ¿Qué día tiene un consumo eléctrico anormalmente alto? |
| Filtrado por valores extremos | ¿Puedes eliminar los outliers del dataset y recalcular la media? |
| Visualización de anomalías | Crea un gráfico con los días anómalos resaltados en rojo. |

---

## 🔗 Relaciones entre variables

| Tipo de análisis | Prompt sugerido |
|------------------|-----------------|
| Correlaciones | ¿Existe correlación entre la temperatura y el consumo energético? |
| Gráficos cruzados | Crea un gráfico de dispersión entre consumo de agua y consumo de energía. |
| Comparativa multivariable | ¿Qué variable parece influir más en el consumo de agua? |

---

## 🧮 Agrupación y resumen

| Tipo de análisis | Prompt sugerido |
|------------------|-----------------|
| Resumen semanal | Agrupa los datos por semana y muestra el consumo promedio. |
| Clasificación por tramos | ¿Puedes mostrar un resumen por tramos de temperatura (baja/media/alta)? |
| Ranking de consumo | Tabla con los 5 días con mayor consumo total (agua + energía). |

---

## 📝 Informes automáticos

| Tipo de informe | Prompt sugerido |
|------------------|-----------------|
| Informe ejecutivo | Redacta un resumen ejecutivo del comportamiento del consumo durante el periodo. |
| Propuesta para dirección | Crea un informe para directiva explicando los patrones observados y posibles medidas de eficiencia. |
| Resumen Markdown | Resume los puntos clave del dataset en formato Markdown. |

---

## 🔁 Reutilización de Artifacts

| Tipo de interacción | Prompt sugerido |
|----------------------|-----------------|
| Modificar gráfico anterior | Utiliza el gráfico anterior y añade una línea de referencia con el promedio. |
| Generar nueva vista | Crea un nuevo gráfico basado en la tabla que acabas de mostrar. |

---

## ✅ Conclusiones

- Claude facilita el análisis exploratorio sin conocimientos técnicos.
- Los Artifacts permiten mantener la trazabilidad y editar los resultados.
- Es una herramienta ideal para prototipado rápido o entornos educativos.

---

## 🔗 Recursos útiles

- 🌐 [Accede a Claude](https://claude.ai/)
- 📄 [Documentación sobre Claude 3](https://www.anthropic.com/index/claude-3)
- 📊 [Ejemplo de Artifact compartido](https://claude.ai/share) *(reemplazar con enlace generado si se desea)*

---
```

¿Quieres que prepare ahora el siguiente ejercicio (por ejemplo, el de **Nixtral** o el nuevo de **Copilot en VSCode**)?