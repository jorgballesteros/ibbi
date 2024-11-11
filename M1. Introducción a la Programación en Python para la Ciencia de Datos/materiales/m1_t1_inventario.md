### Tarea 1: Inventario de Productos
**Objetivo**: Practicar el uso de diccionarios, bucles y la definición de funciones para manipular datos.

---

#### **Descripción del ejercicio**:
Escribe un programa que gestione un inventario de productos en una tienda utilizando un diccionario. El programa permitirá al usuario buscar el precio de un producto, añadir un nuevo producto al inventario y actualizar el precio de un producto existente.

- Utiliza un diccionario donde las **claves** son los nombres de los productos y los **valores** son sus precios.
- Define las siguientes funciones:
  1. `buscar_precio(producto)`: Busca el precio de un producto dado.
  2. `añadir_producto(producto, precio)`: Añade un nuevo producto al inventario.
  3. `actualizar_precio(producto, nuevo_precio)`: Actualiza el precio de un producto existente.

---

#### **Instrucciones**:
1. Crea un diccionario con al menos 5 productos y sus precios.
2. Define las funciones `buscar_precio`, `añadir_producto` y `actualizar_precio`.
3. Permite al usuario realizar las siguientes acciones mediante un menú:
   - Buscar el precio de un producto.
   - Añadir un nuevo producto.
   - Actualizar el precio de un producto existente.
   - Salir del programa.

---

#### **Datos de ejemplo**:

```python
# Diccionario de inventario inicial
inventario = {
    "Manzana": 1.2,
    "Plátano": 0.9,
    "Leche (1L)": 1.3,
    "Pan": 1.5,
    "Huevos (12 unidades)": 3.2,
    "Café (250g)": 4.8,
    "Arroz (1kg)": 2.1,
    "Pasta (500g)": 1.7,
    "Aceite de oliva (1L)": 6.5,
    "Jabón de manos": 2.3,
    "Papel higiénico (6 rollos)": 4.0,
    "Detergente (1L)": 5.6,
    "Agua embotellada (1.5L)": 0.7,
    "Yogurt (pack de 4)": 2.4,
    "Chocolate (100g)": 2.5
}

```

### **Posible salida del programa**:
```
Opciones:
1. Buscar precio de un producto
2. Añadir un nuevo producto
3. Actualizar precio de un producto
4. Salir
Elige una opción (1-4): 1
Introduce el nombre del producto: manzana
0.5 €

Elige una opción (1-4): 2
Introduce el nombre del nuevo producto: yogurt
Introduce el precio del producto: 0.8
Producto 'yogurt' añadido con precio 0.8 €.

Elige una opción (1-4): 3
Introduce el nombre del producto a actualizar: leche
Introduce el nuevo precio: 1.5
El precio de 'leche' ha sido actualizado a 1.5 €.

Elige una opción (1-4): 4
¡Gracias por usar el programa!
```