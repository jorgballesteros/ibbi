# Módulo 5 – Modelos Predictivos en Series Temporales

**Duración total:** 6 horas lectivas (2 sesiones de 3 horas cada una) + 3 horas de tarea en casa.
**Objetivo del módulo:**  
Capacitar al profesorado en la construcción de modelos predictivos aplicados a series temporales, con el fin de identificar tendencias en el uso de recursos (energía y agua) y anticipar patrones futuros que permitan una gestión más eficiente.

---

## Sesión 1 – Fundamentos del modelado temporal y modelos clásicos

**Duración:** 3 horas  
**Objetivo:** Introducir los conceptos básicos de las series temporales y aplicar modelos clásicos como ARIMA y Prophet para realizar predicciones de consumo.

### Parte teórica (45 min)

- ¿Qué son las series temporales? Componentes: tendencia, estacionalidad, ruido.
- Conceptos clave: estacionariedad, autocorrelación, descomposición.
- Introducción a los modelos ARIMA.
- Introducción a Prophet.

### Parte práctica (2h 15 min)

**Actividad 1:** Exploración y análisis de una serie temporal real.  
**Actividad 2:** Predicción de series temporales con ARIMA
**Actividad 3:** Prophet para la predicción de series temporales

### Tarea 1 - Modelado predicitvo de series temporales
**Duración estimada:** 1,5 horas  
**Título:** Ajuste y comparación de modelos clásicos para series temporales

**Objetivo:** Reforzar los fundamentos del modelado clásico de series temporales aplicando ARIMA y Prophet a un nuevo subconjunto de datos y reflexionando sobre los resultados.

**Instrucciones:**

1. Utiliza el archivo `consumo_energia.csv` incluido en la carpeta `data/`. Selecciona una de las columnas (por ejemplo, consumo diario de un edificio concreto).
2. Visualiza la serie y descompón sus componentes (tendencia, estacionalidad).
3. Ajusta un modelo **ARIMA** con `statsmodels` y un modelo **Prophet**, siguiendo la estructura de los notebooks trabajados en clase.
4. Realiza una predicción para los siguientes 15 días.
5. Compara ambos modelos visualmente y, si es posible, calcula métricas como MAE o RMSE.
6. Redacta una breve reflexión (5-10 líneas) sobre:
   - ¿Cuál de los dos modelos se ajustó mejor a tus datos?
   - ¿Cuál te pareció más sencillo de aplicar?
   - ¿Qué limitaciones observaste?

Puedes entregar un notebook `.ipynb` o un documento `.pdf` generado desde Colab.

---

## Sesión 2 – Predicción avanzada con redes neuronales, GluonTS y AutoML

**Duración:** 3 horas  
**Objetivo:** Explorar técnicas modernas de predicción temporal con redes neuronales y librerías como GluonTS, y facilitar el uso de AutoML para docentes que deseen aplicar modelos sin programación avanzada.

### Parte teórica (45 min)

- Introducción a RNN/LSTM.
- Librería GluonTS.
- ¿Qué es AutoML? Uso de H2O AutoML.

### Parte práctica (2h 15 min)

**Actividad 1:** LSTM en Keras.  
**Actividad 2:** Predicción rápida con GluonTS.  
**Actividad 3:** AutoML con H2O AutoML.

### Tarea 2 - Modelos predicitivos avanzados y AutoML
**Duración estimada:** 1,5 horas  
**Título:** Comparación práctica entre GluonTS y H2O.ai AutoML para la predicción de consumo de agua

**Objetivo:** Consolidar el uso de librerías modernas y herramientas AutoML para la predicción de series temporales, evaluando su rendimiento y facilidad de uso.

**Instrucciones:**

1. Usa el dataset `consumo_agua.csv` de la carpeta `data/`.  
2. Realiza una predicción de al menos 15 días futuros con:
   - **GluonTS**: empleando `ProphetModel` o `ThetaModel`, según tu preferencia.
   - **H2O.ai AutoML**: desde Google Colab, usando un `H2OFrame` e indicando la columna temporal correctamente.
3. Compara los resultados:
   - Visualización de ambas predicciones.
   - Métricas de error (si es posible): MAE, RMSE.
   - Tiempo de ejecución, facilidad de configuración, necesidad de intervención.
4. Redacta una reflexión breve (5-10 líneas):
   - ¿Qué herramienta fue más accesible?
   - ¿Cuál consideras más útil en contextos educativos?
   - ¿Te imaginaste aplicando alguna en tu centro?

Formato de entrega: notebook `.ipynb` o `.pdf`.

---

## Recursos adicionales

- Notebooks de ejemplo en `materiales/`.
- Datasets disponibles en `data/m5_consumo_agua.csv` y `data/m5_consumo_energia.csv`.
- Librerías de modelado predicitvo:
- Series temporales y modelos predicitivo:
  - **Statsmodels** (modelos estadísticos, ARIMA): https://www.statsmodels.org/stable/index.html
  - **Prophet** (modelado de series temporales): https://facebook.github.io/prophet/docs/quick_start.html
  - **GluonTS (Meta)** – Kit de análisis de series temporales: https://facebookresearch.github.io/GluonTS/
- Redes neuronales y aprendizaje profundo:
  - **TensorFlow** (librería de ML de Google): https://www.tensorflow.org/api_docs
  - **Keras** (API de alto nivel para redes neuronales): https://keras.io/guides/
- Plataformas de AutoML
  - **H2O.ai AutoML**: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html

