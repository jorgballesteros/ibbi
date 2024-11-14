### Caso Práctico 4: Análisis de Calificaciones de Estudiantes
**Objetivo**: Practicar la creación y manipulación de DataFrames en Pandas, junto con el uso de operaciones básicas y filtrado de datos.

---

#### **Descripción del ejercicio**:
Tienes un conjunto de datos con las calificaciones de varios estudiantes en tres materias: Matemáticas, Física y Química. Utiliza **Pandas** para analizar estos datos y responder a algunas preguntas.

Los datos son los siguientes:

| Nombre     | Matemáticas | Física | Química |
|------------|-------------|--------|---------|
| Ana        | 85         | 78     | 92      |
| Benjamín   | 76         | 85     | 88      |
| Carla      | 90         | 95     | 85      |
| Daniel     | 65         | 70     | 75      |
| Elena      | 80         | 88     | 82      |

Tu tarea es:

1. Crear un **DataFrame** con los datos anteriores.
2. Calcular el **promedio** de calificaciones de cada estudiante.
3. Determinar qué estudiante tiene la **calificación más alta** en Matemáticas.
4. Filtrar el DataFrame para mostrar solo a los estudiantes que tienen un promedio superior a **80**.
5. Agregar una nueva columna llamada `Promedio` que contenga el promedio de las tres materias.

---

#### **Instrucciones**:
1. Importa el módulo `pandas`.
2. Crea un DataFrame a partir de los datos proporcionados.
3. Realiza los cálculos y filtrados utilizando las funciones de Pandas.
4. Imprime los resultados de cada análisis.

---

### **Código de inicio**:

```python
import pandas as pd

# 1. Crear el DataFrame con los datos proporcionados
datos = {
    "Nombre": ["Ana", "Benjamín", "Carla", "Daniel", "Elena"],
    "Matemáticas": [85, 76, 90, 65, 80],
    "Física": [78, 85, 95, 70, 88],
    "Química": [92, 88, 85, 75, 82]
}

df = pd.DataFrame(datos)
```