# Ejercicio 7: Aplicación Web Interactiva

---

## 1. Contexto

**Dash** es un framework en Python que permite construir aplicaciones web interactivas para análisis y visualización de datos. Se basa en **Plotly** para gráficos y **Flask** para la interfaz web, ofreciendo una solución poderosa para dashboards y herramientas analíticas. En este ejercicio, usaremos **Dash** para construir una aplicación sencilla que permita seleccionar un rango de fechas y visualizar variables meteorológicas de un dataset con datos horarios.

El dataset contiene las siguientes columnas:
- **fecha**: Marca temporal.
- **temperature**: Temperatura en grados Celsius.
- **humidity**: Humedad relativa en porcentaje.
- **precipitation**: Precipitación en milímetros.
- **wind_speed**: Velocidad del viento en m/s.
- **location**: Localización de la medición.

---

## 2. Objetivo

Crear una aplicación sencilla en **Dash** que:
1. Permita seleccionar un rango de fechas utilizando un selector interactivo.
2. Visualice las variables meteorológicas seleccionadas para el rango de fechas especificado.
3. Ofrezca gráficos de líneas interactivos para las variables seleccionadas.

---

## 3. Desarrollo del Ejercicio

### Paso 1: Preparar el Dataset
En caso de no disponer de un consjunto de datos, podemos cnostruir uno que nos permita aprender estos conceptos. Si así fuera generaremos un dataset simulado para el ejercicio.

```python
import pandas as pd
import numpy as np

# Generar un dataset simulado
np.random.seed(42)
fechas = pd.date_range(start="2023-01-01", end="2023-12-31", freq="H")
locations = ["Location 1", "Location 2", "Location 3", "Location 4"]

data = {
    "fecha": np.tile(fechas, len(locations)),
    "location": np.repeat(locations, len(fechas)),
    "temperature": np.random.normal(20, 5, len(fechas) * len(locations)),
    "humidity": np.random.uniform(30, 90, len(fechas) * len(locations)),
    "precipitation": np.random.uniform(0, 5, len(fechas) * len(locations)),
    "wind_speed": np.random.uniform(0, 15, len(fechas) * len(locations)),
}

df = pd.DataFrame(data)
df.to_csv('archivo.csv')
```

---

### Paso 2: Crear la Aplicación Dash

1. Instala Dash si no lo tienes ya instalado:
   ```bash
   pip install dash
   ```

2. Escribe el código para la aplicación:

```python
import os
import pandas as pd
from datetime import timedelta

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Obtener solo la carpeta del archivo
current_dir = os.path.dirname(__file__)

# Ruta a la carpeta con los archivos CSV
folder_path = current_dir+"/data/"

# Carga de datos
df = pd.read_csv(folder_path+'m3_e6_datos_meteo_combinados.csv')
print(df.info())
df["fecha"] = pd.to_datetime(df['fecha'])
df = df.loc[~df[['fecha','location']].duplicated(keep='first')]
df.info()

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    # Encabezado
    html.Div(
        html.H1("Visualización de Datos Meteorológicos", 
                style={"color":"white","text-align": "center", "background-color": "#008080", "padding": "20px"}),
    ),

    # Controles en una fila
    html.Div([
        html.Div([
            # Selector de rango de fechas
            html.Label("Rango de Fechas:", style={"font-weight": "bold"}),
            dcc.DatePickerRange(
                id="date-picker",
                min_date_allowed=df["fecha"].min().date(),
                max_date_allowed=df["fecha"].max().date(),
                start_date=df["fecha"].max().date() - timedelta(days=7),
                end_date=df["fecha"].max().date(),
                display_format="YYYY-MM-DD",
                style={"margin": "10px"}
            )
        ], style={"display": "flex", "align-items": "center", "margin-right": "20px"}),

        html.Div([
            # Dropdown para seleccionar la localización
            html.Label("Localización:", style={"font-weight": "bold"}),
            dcc.Dropdown(
                id="location-dropdown",
                options=[{"label": loc, "value": loc} for loc in df["location"].unique()],
                value="icod",
                placeholder="Seleccione una localización",
                style={"width":"120px", "margin": "10px"}
            )
        ], style={"display": "flex", "align-items": "center"})
    ], style={"display": "flex", "align-items": "center", "margin": "20px", "text-align": "center"}),

    # Gráfico de líneas
    dcc.Graph(id="line-graph", style={"margin": "20px"}),
    # Footer
    html.Div(
        html.P([
            html.A("iBBi", href="https://github.com/jorgballesteros/ibbi", target="_blank", style={"color": "#008080"}),
            " @ 2024."
        ], style={"text-align": "center", "color": "gray", "font-size": "14px"}),
        style={"border-top": "1px solid #D5D8DC", "padding": "10px", "margin-top": "20px"}
    )
])

# Callbacks para interactividad
@app.callback(
    Output("line-graph", "figure"),
    Input("date-picker", "start_date"),
    Input("date-picker", "end_date"),
    Input("location-dropdown", "value")
)
def update_graph(start_date, end_date, location):
    # Filtrar los datos según las fechas y localización seleccionadas
    filtered_df = df[
        (df["fecha"] >= start_date) &
        (df["fecha"] <= end_date) &
        (df["location"] == location)
    ]

    # Crear gráfico interactivo
    fig = px.line(
        filtered_df,
        x="fecha",
        y=["temperature", "humidity", "precipitation", "wind_speed"],
        labels={"value": "Valor", "fecha": "Fecha", "variable": "Variable"},
        title=f"Datos Meteorológicos para {location}"
    )
    fig.update_traces(mode="lines+markers")
    return fig

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)

```

---

## 4. Conclusión

Esta aplicación demuestra cómo **Dash** puede facilitar la creación de herramientas analíticas interactivas:
- **Selector de fechas**: Permite enfocar el análisis en un rango específico.
- **Dropdown para localización**: Simplifica la selección de datos específicos.
- **Gráficos dinámicos**: Muestran las variables seleccionadas de manera clara y visualmente atractiva.

---

## 5. Referencias y Ayuda

1. **Dash Documentation**: [https://dash.plotly.com/](https://dash.plotly.com/)
2. **Plotly Express**: [https://plotly.com/python/plotly-express/](https://plotly.com/python/plotly-express/)
3. **Dash Callbacks**: [https://dash.plotly.com/basic-callbacks](https://dash.plotly.com/basic-callbacks)
