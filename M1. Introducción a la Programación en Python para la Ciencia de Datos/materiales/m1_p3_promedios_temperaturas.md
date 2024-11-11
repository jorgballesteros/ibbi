### Caso Práctico 3: Análisis de Temperaturas con NumPy
**Objetivo**: Practicar la creación y manipulación de arrays de NumPy, así como el uso de operaciones básicas y funciones de este paquete.

---

#### **Descripción del ejercicio**:
Se te proporcionan los datos de temperatura (en grados Celsius) registrados durante los últimos 7 días en tres ciudades diferentes. Utiliza **NumPy** para realizar cálculos y análisis de estas temperaturas.

Los datos son los siguientes:

```
Ciudad A: [22, 21, 23, 24, 20, 19, 21]
Ciudad B: [18, 17, 19, 20, 21, 20, 22]
Ciudad C: [25, 24, 26, 27, 23, 22, 24]
```

La tarea es:

1. Crear un array de **NumPy** para cada ciudad.
2. Calcular la **temperatura promedio** de cada ciudad.
3. Determinar la **temperatura máxima y mínima** registrada en cada ciudad.
4. Calcular la **temperatura promedio de todas las ciudades** para cada día.
5. Determinar qué ciudad tuvo la **mayor temperatura promedio** durante la semana.
6. Crear un nuevo array que contenga la **diferencia** entre las temperaturas de la Ciudad A y Ciudad B para cada día.

---

#### **Instrucciones**:
1. Importa el módulo `numpy`.
2. Crea arrays de NumPy para almacenar los datos de temperatura.
3. Realiza los cálculos solicitados utilizando las funciones y métodos de NumPy.
4. Imprime los resultados de cada cálculo.

---

#### **Código de inicio**:

```python
import numpy as np

# 1. Crear arrays de NumPy para cada ciudad
ciudad_a = np.array([22, 21, 23, 24, 20, 19, 21])
ciudad_b = np.array([18, 17, 19, 20, 21, 20, 22])
ciudad_c = np.array([25, 24, 26, 27, 23, 22, 24])
```