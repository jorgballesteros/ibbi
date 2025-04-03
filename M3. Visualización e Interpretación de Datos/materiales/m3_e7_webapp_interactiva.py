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
folder_path = os.path.join(current_dir, "data")

# Carga de datos
df = pd.read_csv(os.path.join(folder_path, 'm3_e6_datos_meteo_combinados.csv'))
df["fecha"] = pd.to_datetime(df['fecha'])

# Eliminar duplicados
df = df.loc[~df[['fecha', 'location']].duplicated(keep='first')]

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    # Encabezado
    html.H1("Visualización de Datos Meteorológicos", 
            style={"color": "white", "text-align": "center", "background-color": "#FF8080", "padding": "20px"}),

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
        ], style={"margin-right": "20px"}),

        html.Div([
            # Dropdown para seleccionar la localización
            html.Label("Localización:", style={"font-weight": "bold"}),
            dcc.Dropdown(
                id="location-dropdown",
                options=[{"label": loc, "value": loc} for loc in df["location"].unique()],
                value=df["location"].unique()[0],  # Primera localización por defecto
                placeholder="Seleccione una localización",
                style={"width": "150px", "margin": "10px"}
            )
        ])
    ], style={"display": "flex", "align-items": "center", "margin": "20px"}),

    # Gráficos
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
    [Output("line-graph", "figure"), Output("area-graph", "figure")],
    [Input("date-picker", "start_date"),
     Input("date-picker", "end_date"),
     Input("location-dropdown", "value")]
)
def update_graph(start_date, end_date, location):
    if not start_date or not end_date or not location:
        return dash.no_update

    # Filtrar los datos según las fechas y localización seleccionadas
    filtered_df = df[
        (df["fecha"] >= start_date) & 
        (df["fecha"] <= end_date) & 
        (df["location"] == location)
    ]

    if filtered_df.empty:
        return dash.no_update

    # Gráfico de líneas
    line_fig = px.line(
        filtered_df, 
        x="fecha", 
        y=["temperature", "humidity", "precipitation", "wind_speed"],
        labels={"value": "Valor", "fecha": "Fecha", "variable": "Variable"},
        title=f"Datos Meteorológicos para {location}"
    )
    line_fig.update_traces(mode="lines")

    # Gráfico de área
    area_fig = px.area(
        filtered_df, 
        x="fecha", 
        y="temperature", 
        title=f"Evolución de la Temperatura en {location}"
    )

    return line_fig, area_fig

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)