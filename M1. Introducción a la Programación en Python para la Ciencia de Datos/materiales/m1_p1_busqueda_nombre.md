### Ejercicio 1: Búsqueda de Apellidos por Nombre
**Objetivo**: Practicar el uso de diccionarios y la definición de funciones para la búsqueda de datos.

---

#### **Descripción del ejercicio**:
Escribe un programa que almacene un conjunto de nombres y apellidos en un diccionario y que permita buscar los apellidos de las personas que tienen un nombre específico (en este caso, "Carlos").

- Utiliza un diccionario donde las **claves** son los nombres y los **valores** son los apellidos.
- Define una función llamada `buscar_apellidos(nombre)` que tome un nombre como argumento y devuelva una lista de apellidos asociados con ese nombre.
- Si no se encuentra ninguna persona con el nombre dado, la función debe devolver un mensaje que lo indique.

---

#### **Instrucciones**:
1. Crea un diccionario con al menos 6 pares de nombres y apellidos.
2. Define la función `buscar_apellidos(nombre)` para buscar en el diccionario los apellidos de las personas que tienen el nombre "Carlos".
3. Pide al usuario que ingrese un nombre y muestra los apellidos correspondientes utilizando la función definida.
4. Si no hay coincidencias, muestra un mensaje indicando que no se encontraron resultados.

---

#### Datos de ejemplo:
```python
# Diccionario con nombres como claves y apellidos como valores
personas = {
    "Carlos": "Pérez",
    "Ana": "García",
    "Roberto": "Gómez",
    "Marta": "López",
    "Carlos": "Rodríguez",
    "Luis": "Martínez",
    "Pedro": "Sánchez"
}
```

### Nota importante:
El uso de **diccionarios en Python no permite tener claves duplicadas**, por lo que si en este caso hubiera varios "Carlos", solo se almacenará el último valor asignado.