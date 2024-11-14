# Tarea 2: Análisis de Ventas Semanales con Pandas
**Objetivo**: Practicar la creación y manipulación de DataFrames de Pandas, así como el uso de operaciones básicas, filtrado, agregación y análisis de datos.

---

## **Descripción del ejercicio**:
Imagina que trabajas en el departamento de ventas de una tienda y tienes acceso a un conjunto de datos que contiene información sobre las ventas de la última semana. Los datos incluyen:

- **Día de la semana**
- **Categoría del producto**
- **Unidades vendidas**
- **Precio por unidad**

Debes realizar un análisis utilizando **Pandas** para responder a una serie de preguntas sobre el desempeño de las ventas.

Los datos se proporcionan a continuación:

| Día         | Categoría | Unidades Vendidas | Precio Unidad (€) |
|-------------|-----------|--------------------|-------------------|
| Lunes       | Electrónica | 5              | 200               |
| Lunes       | Ropa        | 10             | 30                |
| Martes      | Alimentos   | 8              | 5                 |
| Martes      | Electrónica | 3              | 150               |
| Miércoles   | Ropa        | 7              | 25                |
| Jueves      | Alimentos   | 15             | 7                 |
| Viernes     | Electrónica | 2              | 220               |
| Viernes     | Alimentos   | 20             | 6                 |
| Sábado      | Ropa        | 12             | 40                |
| Domingo     | Electrónica | 1              | 300               |

Tu tarea es:

1. Crear un **DataFrame** con los datos anteriores.
2. Calcular la **venta total por categoría** (Unidades Vendidas * Precio Unidad).
3. Determinar qué **día de la semana** tuvo el **mayor total de ventas**.
4. Calcular la **media de ventas** para cada categoría.
5. Filtrar las ventas para mostrar solo aquellas que superaron los **1000 €**.
6. Agregar una nueva columna llamada `Ingreso Total`, que sea el resultado de multiplicar las **Unidades Vendidas** por el **Precio Unidad**.

---

## **Instrucciones**:
1. Importa el módulo `pandas`.
2. Crea un DataFrame a partir de los datos proporcionados.
3. Realiza los cálculos y filtrados utilizando las funciones de Pandas.
4. Imprime los resultados de cada análisis.

---

## **Posible salida del programa**:

```
Venta total por categoría:
Categoría
Alimentos       216
Electrónica    2150
Ropa            935
Name: Ingreso Total, dtype: int64

El día con mayor total de ventas es: Lunes

Media de ventas por categoría:
Categoría
Alimentos      108.0
Electrónica    537.5
Ropa           311.7
Name: Ingreso Total, dtype: float64

Ventas que superaron los 1000 €:
        Día    Categoría  Unidades Vendidas  Precio Unidad (€)  Ingreso Total
0     Lunes  Electrónica                 5               200           1000
9   Domingo  Electrónica                 1               300           300

DataFrame con columna 'Ingreso Total':
         Día    Categoría  Unidades Vendidas  Precio Unidad (€)  Ingreso Total
```
## Solución del Ejercicio

```python
import pandas as pd

# 1. Crear el DataFrame con los datos proporcionados
datos = {
    "Día": ["Lunes", "Lunes", "Martes", "Martes", "Miércoles", "Jueves", 
            "Viernes", "Viernes", "Sábado", "Domingo"],
    "Categoría": ["Electrónica", "Ropa", "Alimentos", "Electrónica", 
                  "Ropa", "Alimentos", "Electrónica", "Alimentos", "Ropa", "Electrónica"],
    "Unidades Vendidas": [5, 10, 8, 3, 7, 15, 2, 20, 12, 1],
    "Precio Unidad (€)": [200, 30, 5, 150, 25, 7, 220, 6, 40, 300]
}