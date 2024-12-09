### **Tutorial de Instalación y Uso de Metabase**

**Metabase** es una herramienta de **Business Intelligence** (BI) de código abierto que permite crear dashboards, realizar consultas y visualizar datos de forma sencilla e intuitiva. Aquí tienes un tutorial paso a paso para instalarlo y empezar a usarlo.

---

### **1. Requisitos Previos**
Antes de instalar Metabase, asegúrate de tener:
- **Java Runtime Environment (JRE)**: Metabase requiere Java 8 o superior. Para verificar si está instalado, usa:
  ```bash
  java -version
  ```
  Si no está instalado, descárgalo desde [OpenJDK](https://openjdk.org/) o usa tu gestor de paquetes (por ejemplo, `sudo apt install openjdk-11-jre` en Ubuntu).

---

Aquí tienes un tutorial actualizado con la posibilidad de usar un fichero **CSV** como fuente de datos en **Metabase** y referencias adicionales para profundizar en su uso.

---

### **2. Instalación de Metabase**
Sigue estos pasos para instalar Metabase:

#### **A) Requisitos Previos**
- **Java Runtime Environment (JRE)**:
  - Verifica si está instalado:
    ```bash
    java -version
    ```
  - Si no está instalado, descárgalo desde [OpenJDK](https://openjdk.org/) o instala con:
    ```bash
    sudo apt install openjdk-11-jre  # Ubuntu
    brew install openjdk            # macOS
    ```

#### **B) Descarga de Metabase**
1. Visita la página oficial de descargas: [Metabase Downloads](https://www.metabase.com/start).
2. Descarga el archivo JAR (`metabase.jar`).

#### **C) Ejecutar Metabase**
1. Abre una terminal y navega al directorio donde descargaste `metabase.jar`:
   ```bash
   cd /ruta/donde/descargaste/metabase
   ```
2. Inicia Metabase con:
   ```bash
   java -jar metabase.jar
   ```
3. Abre tu navegador y ve a:
   ```
   http://localhost:3000
   ```

---

### **3. Configuración Inicial**
1. **Crear un Usuario Administrador**:
   - Introduce tu nombre, correo y contraseña.
2. **Conectar Datos**:
   - Si estás usando un archivo CSV, sigue los pasos en la sección **"Usar un Archivo CSV"**.
   - Si tienes una base de datos (MySQL, PostgreSQL, etc.), ingresa las credenciales y conecta.

---

### **4. Usar un Archivo CSV en Metabase**
#### **A) Preparar el Adaptador para CSV**
Metabase no admite archivos CSV directamente, pero puedes usar un adaptador como [csv2sqlite](https://github.com/dbohdan/csv2sqlite) para convertir tu archivo CSV en una base de datos SQLite.

1. **Instalar `csv2sqlite`**:
   - Descárgalo desde su repositorio oficial:
     ```bash
     git clone https://github.com/dbohdan/csv2sqlite.git
     ```
   - Entra al directorio:
     ```bash
     cd csv2sqlite
     ```
   - Asegúrate de tener Python instalado, luego convierte tu archivo CSV:
     ```bash
     python csv2sqlite.py archivo.csv archivo.sqlite
     ```

2. **Conectar el SQLite a Metabase**:
   - Durante la configuración inicial de Metabase, selecciona **SQLite** como tipo de base de datos.
   - En el campo "Archivo", selecciona el archivo `archivo.sqlite` generado.

#### **B) Alternativa: Usar una Herramienta SQLite**
- Puedes usar herramientas como `DB Browser for SQLite` para importar manualmente un archivo CSV a SQLite.

---

### **5. Crear Consultas y Visualizaciones**
1. **Haz clic en "Ask a Question"**:
   - Selecciona una tabla de datos (de tu archivo CSV convertido o de cualquier otra base de datos conectada).
   - Usa **Filtros** y **Agrupaciones** para analizar tus datos.

2. **Selecciona una Visualización**:
   - Gráficos disponibles incluyen barras, líneas, mapas, tablas, entre otros.

3. **Guarda tus Consultas**:
   - Haz clic en **Save this Question** para reutilizar consultas en dashboards.

---

### **6. Crear un Dashboard**
1. Haz clic en **"New Dashboard"** desde el menú principal.
2. Arrastra tus preguntas guardadas al espacio del dashboard.
3. Personaliza las gráficas y guarda el dashboard.

---

### **7. Desinstalación (Opcional)**
1. Si ejecutaste Metabase desde el archivo JAR, simplemente elimina el archivo:
   ```bash
   rm metabase.jar
   ```
2. Para bases de datos locales (si configuraste una en SQLite), elimina también los archivos relacionados.

---

### **Resolución de Problemas Comunes**
#### **Error: "Java not found"**
- Asegúrate de que Java está instalado correctamente. Verifica con:
  ```bash
  java -version
  ```

#### **Metabase no se inicia**
- Revisa el archivo de log para ver detalles del error:
  ```bash
  tail -f metabase.log
  ```

---

### **Ejemplo Completo**
#### Supongamos que tienes un archivo CSV llamado `ventas.csv`:
Contenido:
```csv
Fecha,Producto,Unidades,Ingresos
2023-01-01,Producto A,10,200
2023-01-02,Producto B,5,100
2023-01-03,Producto C,20,400
```

1. Usa `csv2sqlite` para convertirlo:
   ```bash
   python csv2sqlite.py ventas.csv ventas.sqlite
   ```
2. Conecta `ventas.sqlite` a Metabase durante la configuración inicial.
3. Crea un gráfico de barras agrupando los ingresos por producto.

---

### **Recursos Adicionales**
- **Documentación Oficial de Metabase**: [https://www.metabase.com/docs/](https://www.metabase.com/docs/)
- **Guía de Adaptadores CSV**:
  - [`csv2sqlite`](https://github.com/dbohdan/csv2sqlite)
  - [`csv-to-sqlite`](https://pypi.org/project/csv-to-sqlite/)
