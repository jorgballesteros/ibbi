### Caso Práctico 2: Juego de Adivinanza de Números
**Objetivo:** Practicar el uso de bucles, condicionales, variables y funciones.

1. **Descripción del ejercicio**:
   - Escribe un programa en el que el usuario intente adivinar un número entre 1 y 100.
   - El número será generado aleatoriamente por el programa.
   - Utiliza una función llamada `jugar_adivinanza` que se encargue de la lógica del juego.
   - El programa debe indicar si el número introducido por el usuario es mayor o menor que el número objetivo y continuar hasta que el usuario lo adivine.
   - Al final, muestra cuántos intentos tomó adivinar el número.

2. **Instrucciones**:
   - Importa el módulo `random` para generar un número aleatorio.
   - Usa condicionales para verificar si el número ingresado es mayor, menor o igual al número a adivinar.
   - Cuenta el número de intentos realizados por el usuario.
   - La cuenta de intentos y el número aleatorio deben generarse en una celda independiente a la de ejecución de la función.

3. **Código de inicio**:

```python
import random
incognita = random.random() * 100
# Redondear a número entero

```