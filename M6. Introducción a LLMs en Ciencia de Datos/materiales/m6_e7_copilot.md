# 🧪 Ejercicio 3 – Análisis asistido con GitHub Copilot en VSCode

---

## 🎯 Objetivo

Usar **GitHub Copilot** en un **Jupyter Notebook** abierto en Visual Studio Code para generar y ejecutar análisis de datos con ayuda de comentarios en lenguaje natural. El alumnado interactuará con el dataset `m6_consumo_agua.csv`, generando gráficos, estadísticas y observaciones guiadas por la IA.

---

## 🧠 ¿Por qué usar un Notebook con Copilot?

Los notebooks permiten combinar **código, texto y visualizaciones** en el mismo documento. Esto facilita:
- La documentación del análisis paso a paso.
- La comprensión del código generado por Copilot.
- La presentación directa de resultados y reflexiones.

---

## 🛠️ Requisitos

1. Tener instalada la extensión **Jupyter** en VSCode.
2. Tener instalada la extensión **GitHub Copilot**.
3. Tener Python 3.x y `jupyter`, `pandas`, `matplotlib` instalados:

```bash
pip install jupyter pandas matplotlib
```

4. Iniciar sesión en GitHub con Copilot activado.

---

## 📁 Dataset: `m6_consumo_agua.csv`

Columnas:
- `Fecha` (formato fecha)
- `Consumo` (litros)
- `Temperatura` (°C)

---

## 🧪 Paso a paso del ejercicio

### 🔹 Paso 1 – Crear el notebook

1. En VSCode, pulsa `Ctrl + Shift + P` → **Create: New Jupyter Notebook**.
2. Guarda el archivo como `analisis_agua_m6.ipynb`.

---

### 🔹 Paso 2 – Primer bloque de código

Escribe en una celda:

```python
# Cargar el dataset y mostrar las primeras filas
```

👉 Copilot sugerirá automáticamente el código para importar pandas, cargar el CSV y mostrar `df.head()`.

---

### 🔹 Paso 3 – Comentar el análisis paso a paso

A medida que avances, añade nuevas celdas con comentarios como:

```python
# Calcular el promedio de consumo y temperatura

# Crear un gráfico de líneas del consumo de agua por día

# Detectar valores atípicos en el consumo

# Ver la correlación entre consumo y temperatura
```

👉 En cada caso, Copilot completará el código, que puedes aceptar con `Tab`.

---

## 🧠 Comentarios útiles que Copilot entiende

- `# Mostrar el día con el menor consumo de agua`
- `# Explica si hay una relación entre temperatura y consumo`
- `# Crear un gráfico combinado de consumo y temperatura usando dos ejes`
- `# Guardar los resultados en un nuevo CSV`

---

## 📊 Resultados esperados

- Visualizaciones con `matplotlib`.
- Estadísticas básicas (`mean`, `min`, `max`).
- Código bien estructurado con etiquetas y comentarios generados por Copilot.
- Posible explicación de los pasos si lo solicitas.

---

## 💡 Variante adicional (opcional)

Pide a Copilot que actúe como profesor:

```python
# Explica qué hace este código paso a paso
```

Pega debajo el código generado y observa la explicación automática.

---

## ✅ Conclusiones

- El entorno Jupyter + Copilot permite aprender y aplicar Python con apoyo guiado.
- Ideal para documentar un análisis completo con texto + código + gráficos.
- Copilot sirve como asistente en tiempo real para exploración y depuración.

---

## 🔗 Recursos útiles

- 🧪 [Cómo usar Jupyter Notebooks en VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- 💡 [Github Copilot en VSCode](https://code.visualstudio.com/docs/copilot/overview)
- 🤖 [Inicio rápido para GitHub Copilot](https://docs.github.com/en/copilot/quickstart)
- 🎥 [Efforless Python with Github Copilot](https://www.youtube.com/watch?v=DSHfHT5qnGc)
