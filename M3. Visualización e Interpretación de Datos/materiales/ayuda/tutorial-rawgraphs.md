# **Tutorial de Instalación y Uso de RAWGraphs**

RAWGraphs es una herramienta de visualización de datos autoalojada (**self-hosted**) que permite crear gráficos personalizados a partir de tus datos. Aquí te explico cómo instalarlo en tu máquina local paso a paso.


---
## Instalación de RAWGraphs

### **1. Requisitos Previos**
Antes de instalar RAWGraphs, asegúrate de tener:
- **Node.js** (v16 o superior): Puedes descargarlo desde [nodejs.org](https://nodejs.org/).
- **npm** (v8 o superior): Viene incluido con Node.js.

Para verificar si ya tienes Node.js y npm instalados, ejecuta en tu terminal:
```bash
node -v
npm -v
```

---

### **2. Clonar el Repositorio de RAWGraphs**
1. Abre tu terminal o línea de comandos.
2. Clona el repositorio de RAWGraphs desde GitHub:
   ```bash
   git clone https://github.com/rawgraphs/rawgraphs-app.git
   ```
3. Navega al directorio clonado:
   ```bash
   cd rawgraphs-app
   ```

---

### **3. Instalar Dependencias**
Ejecuta el siguiente comando para instalar todas las dependencias necesarias:
```bash
npm install
```

---

### **4. Iniciar RAWGraphs en Modo Local**
Para ejecutar RAWGraphs en tu máquina, utiliza:
```bash
npm start
```

Esto iniciará un servidor local, y podrás acceder a RAWGraphs en tu navegador web en:
```
http://localhost:8080
```

---

### **5. Compilar para Producción (Opcional)**
Si deseas construir una versión lista para producción:
1. Ejecuta:
   ```bash
   npm run build
   ```
2. La aplicación compilada estará en el directorio `dist/`. Puedes desplegar este directorio en un servidor web.

---

### **6. Resolución de Problemas Comunes**
#### **Error de Dependencias (ERESOLVE)**
Si encuentras errores relacionados con dependencias, prueba los siguientes comandos:
- Instalar ignorando dependencias no resueltas:
  ```bash
  npm install --legacy-peer-deps
  ```
- Forzar la instalación (menos recomendado):
  ```bash
  npm install --force
  ```

#### **Error con la Versión de Node.js**
RAWGraphs requiere una versión específica de Node.js (v16 o superior). Si tienes problemas:
1. Actualiza Node.js descargándolo desde [nodejs.org](https://nodejs.org/).
2. Usa una herramienta de gestión de versiones como `nvm`:
   ```bash
   nvm install 16
   nvm use 16
   ```

---

### **7. Desinstalación (Opcional)**
Si deseas eliminar RAWGraphs de tu máquina:
1. Borra el directorio clonado:
   ```bash
   rm -rf rawgraphs-app
   ```

2. Elimina las dependencias instaladas:
   ```bash
   rm -rf node_modules
   ```

---

## Visualización de Datos
Para visualizar gráficos interactivos en **RAWGraphs**, sigue estos pasos:

---

### **1. Accede a RAWGraphs**
1. Si lo estás ejecutando localmente:
   - Abre tu navegador y ve a `http://localhost:8080`.
2. Si usas la versión en línea:
   - Accede al sitio web oficial: [RAWGraphs.io](https://app.rawgraphs.io).

---

### **2. Carga tus Datos**
1. Haz clic en **"Load your data"**.
2. Elige una de las opciones:
   - **Copiar y pegar**: Pega datos tabulares (como CSV) directamente en el campo de texto.
   - **Cargar un archivo**: Sube un archivo en formato `.csv` o `.tsv`.
   - **Google Spreadsheet**: Usa un enlace público de Google Sheets.

---

### **3. Configura los Datos**
1. RAWGraphs detectará automáticamente las columnas y el tipo de datos (numérico, categórico, etc.).
2. Ajusta las propiedades de las columnas si es necesario:
   - **Categorías**: Para valores como nombres, regiones o productos.
   - **Valores numéricos**: Para valores como ventas, ingresos o cantidades.
   - **Fechas**: RAWGraphs reconoce automáticamente las fechas en formato ISO (`YYYY-MM-DD`).

---

### **4. Selecciona un Gráfico**
1. RAWGraphs ofrece una variedad de gráficos interactivos y personalizados, como:
   - **Bar Chart** (Gráfico de Barras).
   - **Scatter Plot** (Gráfico de Dispersión).
   - **Alluvial Diagram** (Diagrama de Flujo).
   - **Bubble Chart** (Gráfico de Burbujas).
   - **Sunburst** (Diagrama de Sol Radial).

2. Selecciona el gráfico que mejor se adapte a tus datos.

---

### **5. Asigna Variables al Gráfico**
1. RAWGraphs mostrará un panel donde puedes arrastrar las columnas de tus datos a los roles del gráfico:
   - **Ejes**: Para gráficos como barras o dispersión.
   - **Tamaño**: Para gráficos de burbujas o mapas.
   - **Color**: Para diferenciar categorías.
   - **Flujos**: En diagramas como el Alluvial.

2. RAWGraphs genera el gráfico automáticamente mientras asignas las variables.

---

### **6. Personaliza la Visualización**
1. RAWGraphs permite personalizar:
   - **Colores**: Cambia la paleta de colores o selecciona colores específicos para cada categoría.
   - **Tamaños de texto**: Ajusta la escala de etiquetas o leyendas.
   - **Filtros**: Filtra valores directamente en el gráfico.

2. Explora las opciones avanzadas para adaptar el diseño a tus necesidades.

---

### **7. Exporta tu Gráfico**
1. Una vez satisfecho con el gráfico, haz clic en **"Export"**.
2. RAWGraphs ofrece varios formatos de exportación:
   - **SVG**: Para editar en software de diseño como Illustrator o Inkscape.
   - **PNG**: Para una imagen estática.
   - **JSON**: Para reutilizar la configuración en RAWGraphs.
   - **D3.js Code**: Para desarrolladores que quieran integrar el gráfico en sitios web.

---

### **Ejemplo Rápido: Scatter Plot**
- **Datos**: Lista de productos, sus precios y cantidades vendidas.
- **Proceso**:
  1. Sube tu archivo CSV.
  2. Elige **Scatter Plot**.
  3. Arrastra:
     - **Eje X**: Columna de precios.
     - **Eje Y**: Columna de cantidades vendidas.
     - **Color**: Columna de categorías de productos.
  4. Personaliza el tamaño de los puntos y los colores.
  5. Exporta el gráfico.

---

### **Tips para Gráficos Interactivos**
- RAWGraphs es principalmente para gráficos estáticos, pero puedes exportar los datos a herramientas como **Plotly** o **D3.js** para añadir interactividad avanzada.
- Puedes probar a usra los conjntos de datos de prueba y seguir los tutoriales de uso del sitio web.
- Si necesitas ver cambios dinámicos, considera configurar diferentes versiones de los datos en RAWGraphs y comparar visualmente.

## 5. Referencias y Ayuda

1. **RawGraphs**: [https://rawgraphs.io/](https://rawgraphs.io/)
2. **Tutoriales de RawGraphs**: [https://www.rawgraphs.io/learning](https://www.rawgraphs.io/learning)
3. **Ejemplos de Visualizaciones**: [https://rawgraphs.io/gallery/](https://rawgraphs.io/gallery/)