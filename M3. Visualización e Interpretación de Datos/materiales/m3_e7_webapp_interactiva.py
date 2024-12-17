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
                style={"color":"white","text-align": "center", "background-color": "#FF8080", "padding": "20px"}),
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
    dcc.Graph(id="area-graph", style={"margin": "20px"}),
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
    Output("area-graph", "figure"),
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
    fig.update_traces(mode="lines")
    return fig

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
