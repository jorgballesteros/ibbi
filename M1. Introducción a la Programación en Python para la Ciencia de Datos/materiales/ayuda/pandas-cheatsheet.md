## Cheatsheet de Pandas
Pandas es una de las bibliotecas más populares para el análisis y manipulación de datos en Python. Es ideal para trabajar con datos tabulares, similares a los de una hoja de cálculo.

---

### 🔧 Importar la biblioteca
```python
import pandas as pd
import numpy as np
```

---

### 📋 Creación de Series y DataFrames
```python
# Crear una Serie desde una lista
serie = pd.Series([10, 20, 30, 40, 50])

# Crear un DataFrame desde un diccionario
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 35, 31],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(data)

# Crear un DataFrame vacío
df_vacio = pd.DataFrame()
```

---

### 🔍 Inspección de datos
```python
# Cargar un archivo CSV
df = pd.read_csv('archivo.csv')

# Mostrar las primeras y últimas filas
print(df.head())      # Primeras 5 filas
print(df.tail(3))     # Últimas 3 filas

# Obtener información general
print(df.info())      # Resumen del DataFrame
print(df.describe())  # Estadísticas descriptivas
print(df.shape)       # Dimensiones (filas, columnas)
print(df.columns)     # Nombres de las columnas
print(df.dtypes)      # Tipos de datos
```

---

### 🗂️ Selección y filtrado de datos
```python
# Seleccionar una columna
print(df['Nombre'])

# Seleccionar varias columnas
print(df[['Nombre', 'Edad']])

# Seleccionar filas por índice
print(df.iloc[0])     # Primera fila
print(df.iloc[1:4])   # Filas de la 2 a la 4

# Seleccionar filas por condición
print(df[df['Edad'] > 30])
print(df[(df['Ciudad'] == 'Madrid') & (df['Edad'] > 25)])
```

---

### 🔄 Manipulación de datos
```python
# Crear una nueva columna
df['Altura'] = [1.75, 1.80, 1.65]

# Eliminar columnas
df.drop('Altura', axis=1, inplace=True)

# Renombrar columnas
df.rename(columns={'Nombre': 'Nombre_Completo'}, inplace=True)

# Reemplazar valores
df['Ciudad'] = df['Ciudad'].replace('Madrid', 'MAD')

# Eliminar filas duplicadas
df.drop_duplicates(inplace=True)
```

---

### 🧹 Manejo de valores faltantes
```python
# Identificar valores nulos
print(df.isnull().sum())

# Eliminar filas o columnas con valores nulos
df.dropna(axis=0, inplace=True)  # Filas
df.dropna(axis=1, inplace=True)  # Columnas

# Rellenar valores nulos
df['Edad'].fillna(df['Edad'].mean(), inplace=True)
```

---

### 🧮 Operaciones con datos
```python
# Sumar, restar, multiplicar y dividir columnas
df['Doble_Edad'] = df['Edad'] * 2

# Ordenar por columna
df.sort_values(by='Edad', ascending=False, inplace=True)

# Agrupar datos y calcular estadísticas
grupo = df.groupby('Ciudad').mean()
print(grupo)

# Pivot tables
pivot = df.pivot_table(values='Edad', index='Ciudad', aggfunc='mean')
print(pivot)
```

---

### 🔄 Funciones útiles para DataFrames
```python
# Aplicar una función a cada fila o columna
df['Edad_Cuadrado'] = df['Edad'].apply(lambda x: x**2)

# Borrar filas según condición
df.drop(df[df['Edad'] < 25].index, inplace=True)

# Obtener filas con los valores únicos
print(df['Ciudad'].unique())
print(df['Ciudad'].value_counts())
```

---

### 🔍 Merge, Join y Concatenación
```python
# Concatenar DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_concat = pd.concat([df1, df2], ignore_index=True)

# Merge (similar a un JOIN en SQL)
df_izq = pd.DataFrame({'key': ['A', 'B', 'C'], 'val1': [1, 2, 3]})
df_der = pd.DataFrame({'key': ['A', 'B', 'D'], 'val2': [4, 5, 6]})
df_merged = pd.merge(df_izq, df_der, on='key', how='inner')
```

---

### 🗂️ Exportar datos
```python
# Exportar a CSV
df.to_csv('nuevo_archivo.csv', index=False)

# Exportar a Excel
df.to_excel('archivo.xlsx', index=False)

# Exportar a JSON
df.to_json('datos.json')
```

---

### 📊 Visualización rápida
```python
import matplotlib.pyplot as plt

# Gráfica de barras
df['Edad'].plot(kind='bar')
plt.show()

# Histograma
df['Edad'].plot(kind='hist')
plt.show()

# Gráfico de dispersión
df.plot(kind='scatter', x='Edad', y='Altura')
plt.show()
```

---

### 🔍 Ejemplo práctico: Análisis y limpieza de datos
```python
# Cargar datos
df = pd.read_csv('data.csv')

# Filtrar datos y limpiar
df = df[df['Salario'] > 50000]
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Crear una nueva columna basada en condición
df['Alto_Salario'] = np.where(df['Salario'] > 80000, 'Sí', 'No')

# Agrupar y resumir datos
resumen = df.groupby('Departamento')['Salario'].mean()
print(resumen)
```
