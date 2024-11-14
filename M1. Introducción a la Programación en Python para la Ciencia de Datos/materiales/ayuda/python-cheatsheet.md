## Cheatsheet de Python
Funciones y conceptos más comunes que te serán útiles para cualquier proyecto! Esta guía está enfocada en funciones básicas, manipulación de listas, diccionarios, cadenas, archivos y más.

---

### 📌 Estructura básica
```python
# Comentario de una sola línea
"""
Comentario
multilínea
"""

# Imprimir en consola
print("Hola, mundo")

# Variables
x = 10
nombre = "Python"
es_activo = True
```

---

### 📊 Tipos de datos
```python
# Números
entero = 10
flotante = 3.14
complejo = 1 + 2j

# Booleanos
verdadero = True
falso = False

# Cadenas (Strings)
texto = "Hola"
texto_mayus = texto.upper()  # "HOLA"
texto_minus = texto.lower()  # "hola"
```

---

### 🔁 Estructuras de control
```python
# Condicionales
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")

# Bucle for
for i in range(5):
    print(i)  # Imprime 0, 1, 2, 3, 4

# Bucle while
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

---

### 📋 Listas
```python
# Crear lista
numeros = [1, 2, 3, 4, 5]

# Acceso e indexación
print(numeros[0])   # Primer elemento
print(numeros[-1])  # Último elemento

# Operaciones comunes
numeros.append(6)       # Agregar un elemento
numeros.remove(3)       # Eliminar elemento
numeros.pop()           # Elimina y devuelve el último
numeros.sort()          # Ordenar
print(len(numeros))     # Longitud de la lista
```

---

### 📌 Diccionarios
```python
# Crear diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso
print(persona["nombre"])

# Modificar
persona["edad"] = 31

# Métodos comunes
persona.keys()     # Obtener llaves
persona.values()   # Obtener valores
persona.items()    # Obtener pares clave-valor
persona.get("pais", "No encontrado")  # Evitar error si no existe la clave
```

---

### 🧵 Funciones
```python
# Definir una función
def saludo(nombre):
    return f"Hola, {nombre}!"

print(saludo("Ana"))  # Llama a la función

# Función con parámetros por defecto
def sumar(a, b=5):
    return a + b

print(sumar(3))       # Resultado: 8
print(sumar(3, 7))    # Resultado: 10
```

---

### 🗂️ Manejo de archivos
```python
# Leer archivo
with open("archivo.txt", "r") as file:
    contenido = file.read()
    print(contenido)

# Escribir en archivo
with open("nuevo_archivo.txt", "w") as file:
    file.write("Este es un nuevo archivo")

# Agregar contenido a un archivo existente
with open("archivo.txt", "a") as file:
    file.write("\nNueva línea")
```

---

### 📦 Manejo de paquetes y módulos
```python
import math

# Funciones matemáticas
print(math.sqrt(16))    # Raíz cuadrada
print(math.pi)          # Constante Pi

import random
print(random.randint(1, 10))  # Número aleatorio entre 1 y 10
```

---

### 📌 Comprensión de listas
```python
# Crear una nueva lista a partir de otra
numeros = [1, 2, 3, 4, 5]
cuadrados = [n**2 for n in numeros if n % 2 == 0]
print(cuadrados)  # Resultado: [4, 16]
```

---

### 🐼 Uso básico de Pandas (para trabajar con datos)
```python
import pandas as pd

# Crear un DataFrame
data = {'Nombre': ['Ana', 'Juan', 'Carlos'], 'Edad': [23, 30, 35]}
df = pd.DataFrame(data)

# Mostrar información
print(df.head())        # Primeras filas
print(df.describe())    # Estadísticas descriptivas

# Acceso a columnas
print(df['Nombre'])

# Filtrar filas
print(df[df['Edad'] > 25])
```

---

### 🧪 Manejo de errores
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
finally:
    print("Operación finalizada")
```

---

### 📌 Utilidades adicionales
```python
# Enumerar elementos de una lista
nombres = ["Ana", "Juan", "Carlos"]
for indice, nombre in enumerate(nombres):
    print(indice, nombre)

# Zipear dos listas
a = [1, 2, 3]
b = ['a', 'b', 'c']
for x, y in zip(a, b):
    print(x, y)
```