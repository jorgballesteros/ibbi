# Ejercicio 2. Personalización de Gráficos

`matplotlib` permite una amplia personalización de gráficos para adaptarlos a distintos contextos y audiencias. A continuación, se describen los principales aspectos de personalización y buenas prácticas asociadas.

---

## Buenas Prácticas Generales

1. **Conoce tu audiencia**:
   - Asegúrate de que los gráficos sean claros para el público objetivo (e.g., técnicos, directivos).
2. **Simplifica**:
   - Elimina elementos innecesarios que puedan distraer.
3. **Consistencia**:
   - Usa la misma paleta de colores, estilos y tamaños en gráficos relacionados.
4. **Accesibilidad**:
   - Asegúrate de que los gráficos sean interpretables para personas con discapacidades visuales.
5. **Prueba antes de presentar**:
   - Verifica que los elementos sean legibles en diferentes dispositivos o formatos (e.g., pantallas pequeñas, impresiones).

## Personalización de Elementos

### **1. Añadir Títulos y Etiquetas a un Gráfico**
#### Títulos y etiquetas
- **Títulos**: Un título claro y descriptivo ayuda a comprender rápidamente el propósito del gráfico.
  - Coloca un título informativo en la parte superior del gráfico.
- **Etiquetas de Ejes**: Los ejes deben estar etiquetados con unidades o descripciones relevantes.
  - Ejemplo: En un gráfico de tiempo, el eje X puede ser "Meses", y el eje Y "Consumo Energético (kWh)".
#### Líneas de Cuadrícula
- Las cuadrículas mejoran la legibilidad al permitir al lector localizar valores.
- **Recomendaciones**:
  - Usa cuadrículas ligeras y no intrusivas (e.g., grises claros o discontinuas).
  - Activa las cuadrículas para gráficos con valores continuos.
```python
import matplotlib.pyplot as plt

# Datos simples
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico
plt.plot(x, y)

# Personalización
plt.title("Gráfico de Números Primos")  # Título
plt.xlabel("Índice")                   # Etiqueta del eje X
plt.ylabel("Valor")                    # Etiqueta del eje Y
plt.grid(True)                         # Agregar cuadrícula
plt.show()
```

---

### **2. Cambiar Colores y Estilos de Línea**
#### Colores
- Los colores ayudan a distinguir categorías o elementos.
- **Buenas prácticas**:
  - Usa colores consistentes con el tema o marca de la visualización.
  - Evita usar demasiados colores brillantes o similares, ya que dificultan la lectura.
  - Utiliza paletas accesibles para personas con daltonismo (e.g., paleta `viridis`).

#### Estilos de Líneas y Marcadores
- Los estilos de líneas (e.g., sólidas, punteadas) y los marcadores (e.g., círculos, cuadrados) son útiles para diferenciar series.
- **Recomendaciones**:
  - Usa líneas sólidas para la mayoría de los gráficos de tendencia.
  - Combina estilos de líneas con colores si tienes muchas series.
  - Asegúrate de que los marcadores sean visibles y no se solapen demasiado.
```python
plt.plot(x, y, color="red", linestyle="--", linewidth=2, marker="o", markersize=8)

# Personalización
plt.title("Gráfico Personalizado con Estilo")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid(True)
plt.show()
```

---

### **3. Agregar Leyendas a Múltiples Líneas**
- Las leyendas identifican las distintas categorías, series o elementos en un gráfico.
- **Buenas prácticas**:
  - Usa nombres descriptivos en las leyendas (no abreviaturas ambiguas).
  - Ubica la leyenda fuera del área de trazado si el gráfico tiene varias líneas o elementos que se solapan.
  - Asegúrate de que los colores o estilos de las líneas coincidan con los elementos representados.


```python
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Crear múltiples líneas
plt.plot(x, y1, label="Línea 1", color="blue")
plt.plot(x, y2, label="Línea 2", color="green")

# Personalización
plt.title("Gráfico con Leyendas")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend(loc="upper left")  # Posición de la leyenda
plt.grid(True)
plt.show()
```

---

### **4. Cambiar Tamaño y Fuentes de los Textos**
#### Tamaño de la Figura
- Ajustar el tamaño del gráfico garantiza que todos los elementos sean visibles.
- **Recomendaciones**:
  - Para gráficos complejos, utiliza tamaños más grandes para evitar saturación.
  - Mantén una proporción adecuada entre el gráfico y los textos o leyendas.

#### Fuentes y Tamaños de Texto
- Elige fuentes legibles y tamaños apropiados para el contexto.
- **Buenas prácticas**:
  - Usa fuentes más grandes para presentaciones.
  - Evita fuentes decorativas; prioriza la claridad.
  - Asegúrate de que los textos no se superpongan con otros elementos.
```python
plt.plot(x, y)

# Personalización de texto
plt.title("Gráfico con Fuentes Personalizadas", fontsize=16, fontweight="bold")
plt.xlabel("Eje X", fontsize=12)
plt.ylabel("Eje Y", fontsize=12)
plt.grid(True)
plt.show()
```

---

### **5. Usar Colores Personalizados (RGB o Hexadecimal)**
Es posible seleccionar colores personalizdos para los elementos de la gráfica. En este caso, seleccionamos un color mediante su código en hexadecimal.

```python
plt.plot(x, y, color="#FF5733", marker="o")  # Hexadecimal para naranja
plt.title("Gráfico con Colores Personalizados")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.show()
```

---

### **6. Cambiar el Estilo Global del Gráfico**
- `matplotlib` incluye estilos predefinidos (e.g., `ggplot`, `seaborn`, `fivethirtyeight`) que mejoran la apariencia del gráfico.
- **Recomendaciones**:
  - Usa estilos consistentes en todas las visualizaciones de un proyecto.
  - Elige estilos que se alineen con el propósito: algunos son más adecuados para publicaciones científicas, otros para presentaciones.

```python
import matplotlib.pyplot as plt

# Cambiar estilo
plt.style.use("ggplot")  # Estilos: 'seaborn', 'ggplot', 'fivethirtyeight', etc.

# Crear gráfico
plt.plot(x, y)
plt.title("Gráfico con Estilo ggplot")
plt.show()
```

---

### **7. Personalizar un Gráfico de Barras**
```python
categorias = ["A", "B", "C", "D"]
valores = [3, 7, 5, 9]

plt.bar(categorias, valores, color="skyblue", edgecolor="black", linewidth=1.5)

# Personalización
plt.title("Gráfico de Barras Personalizado")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.show()
```

---

### **8. Gráfico con Anotaciones**
- Las anotaciones destacan puntos clave o explican patrones en los datos.
- **Buenas prácticas**:
  - Úsalas para resaltar máximos, mínimos o puntos de interés.
  - Mantén las anotaciones breves y claras.
```python
plt.plot(x, y)

# Anotar un punto específico
plt.annotate("Punto máximo", xy=(5, 11), xytext=(4, 9),
             arrowprops=dict(facecolor="black", arrowstyle="->"))

# Personalización
plt.title("Gráfico con Anotaciones")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.show()
```

---

### **9. Gráfico de Dispersión con Personalización**
```python
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color="purple", alpha=0.7, edgecolor="black")
plt.title("Gráfico de Dispersión Personalizado")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
```

---

### **10. Gráfico con Subgráficos (Subplots)**
#### Subgráficos
- Representación de varias gráficas en una misma figura. 
- **Buenas prácticas**:
  - Recomendable cuando repesentamos datos que no tiene una correlación temporal alta y/o tienen diferentes unidades de medida.

#### Espaciado y Márgenes
- Deja espacio suficiente para que los títulos, etiquetas y leyendas no se recorten.
- **Buenas prácticas**:
  - Usa opciones como `tight_layout` para ajustar automáticamente los márgenes.
  - Si hay muchos elementos externos al gráfico (e.g., títulos largos), aumenta manualmente los márgenes.
```python
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# Subgráfico 1
ax[0, 0].plot(x, y, color="blue")
ax[0, 0].set_title("Subgráfico 1")

# Subgráfico 2
ax[0, 1].bar(categorias, valores, color="green")
ax[0, 1].set_title("Subgráfico 2")

# Subgráfico 3
ax[1, 0].scatter(x, y, color="red")
ax[1, 0].set_title("Subgráfico 3")

# Subgráfico 4
ax[1, 1].hist(valores, bins=5, color="orange")
ax[1, 1].set_title("Subgráfico 4")

plt.tight_layout()
plt.show()
```

---
## Conclusión
En este ejercicio, hemos explorado cómo **personalizar gráficos** en Python utilizando `matplotlib` y `seaborn` para crear visualizaciones **claras, efectivas y visualmente atractivas**. Aprendimos a seleccionar tipos de gráficos adecuados según el tipo de dato y el mensaje que deseamos comunicar, aplicando personalizaciones como **títulos, etiquetas, leyendas, colores y estilos**. Estas herramientas nos permiten destacar **patrones, relaciones y tendencias** en los datos, garantizando que nuestras visualizaciones no solo sean informativas, sino también comprensibles para diferentes audiencias. La clave está en mantener **consistencia, simplicidad y claridad** en nuestras visualizaciones para maximizar su impacto.