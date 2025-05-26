# Caso práctico: Comparativa diaria de energía y mensaje de concienciación
## Descripción del caso práctico

El objetivo de este caso práctico es desarrollar un **panel interactivo en Streamlit** que permita al usuario:

* Visualizar el consumo energético diario en distintas zonas.
* Comparar este consumo con el del día anterior.
* Mostrar gráficas interactivas por zonas.
* Generar automáticamente un **mensaje de concienciación energética** con OpenAI en función de la diferencia de consumo.

Enlace a la carpeta: [iBBi Energía Diaria](apps/ibbi_energia_diaria/)

---

## Estructura y explicación paso a paso

### 1. Configuración inicial

Se configuran el diseño de la página, los títulos, las variables a visualizar y sus unidades.

```python
st.set_page_config(layout="wide")
st.title("iBBi - Comparativa de Consumo Energético")

key_map = {
    "p_total": "energía",
    "voltaje_LNAvg": "voltaje",
    "intensidad_Avg_total": "intensidad"
}
key_unit_map = {
    "energía": "kWh",
    "voltaje": "V",
    "intensidad": "A"
}
```

---

### 2. Autenticación con ThingsBoard

Se accede al token previamente generado para poder consultar los datos desde ThingsBoard.

```python
token_file = os.path.join(DIR_PATH, "tmp", "token.txt")
if os.path.exists(token_file):
    with open(token_file, "r") as f:
        token = f.read().strip()
        if token.startswith("Bearer "):
            token = token[7:]
else:
    print("❌ No se encontró el token.")
    exit()
```

---

### 3. Selección de fecha y variable

El usuario selecciona una **fecha**, la **variable a visualizar** y si desea cargar los datos desde CSV o ThingsBoard.

```python
selected_date = st.date_input("Selecciona una fecha", value=yesterday, max_value=today)
key = st.selectbox("Variable a visualizar", list(key_map.values()), index=0)
src_key = next((k for k, v in key_map.items() if v == key), None)
```

---

### 4. Definición de zonas

Cada zona está asociada a un dispositivo en ThingsBoard:

```python
device_map = {
    "zonaalta": "Zona Alta",
    "zonamedia": "Zona Media",
    "zonabaja": "Zona Baja"
}
device_id_map = {
    "zonaalta": "73d802b0-...",
    "zonamedia": "3d76ce90-...",
    "zonabaja": "1d6c4040-..."
}
```

---

### 5. Carga de datos

Dependiendo de la opción, se cargan datos desde **archivos CSV**:

```python
df_zone = pd.read_csv("data/ibbi_energia_"+name+"_1h.csv")
df_zone = prepare_dataframe(df_zone, src_key, name, date)
```

O desde **ThingsBoard API**:

```python
def get_data_from_tb(device_id, key, start_ts, end_ts):
    url = f"{tb_url}/api/plugins/telemetry/DEVICE/{device_id}/values/timeseries"
    ...
    response = requests.get(url, headers=headers, params=params)
    ...
    return pd.DataFrame(valores)
```

Ambas funciones pasan los datos por un proceso de transformación común:

```python
def prepare_dataframe(df, key, name, date):
    df["fecha"] = pd.to_datetime(df["timestamp"]).dt.date
    df = df[df["fecha"] == date]
    df['zona'] = name
    ...
    return df
```

---

### 6. Visualización interactiva

#### Gráfico de área (consumo horario por zona):

```python
fig = px.area(
    df_day,
    x="timestamp",
    y=key,
    color="zona",
    title=f"{key} horaria",
    markers=True
)
```

#### Gráfico de pastel (distribución por zona):

```python
df_sum_pie = df_day.groupby("zona")[key].sum().reset_index()
fig_pie = px.pie(
    df_sum_pie,
    values=key,
    names="zona",
    hole=0.4
)
```

#### Métricas clave:

```python
total_value = df_group[key].sum().round()
avg_value = df_group[key].mean()
max_value = df_group[key].max()
hora_max = df_group[df_group[key] == max_value]["timestamp"].values[0]
st.metric("Total", f"{total_value:.2f} {key_unit_map[key]}")
```

#### Gráfico de barras comparativo:

```python
df_bar = pd.DataFrame({
    "fecha": [selected_date - timedelta(days=1), selected_date],
    "total": [total_value_vs, total_value]
})
fig_bar = px.bar(df_bar, x="fecha", y="total", ...)
```

---

### 7. Generación automática de mensaje con IA

Se genera un prompt dinámico con los valores de consumo y se envía a OpenAI:

```python
prompt = f"Analiza el consumo de {key} del día {selected_date.strftime('%d/%m/%Y')} y compara con el día anterior..."
response = openai.chat.completions.create(
    model=st.session_state["openai_model"],
    messages=[
        {"role": "system", "content": "Eres un asistente experto en análisis de consumo energético."},
        {"role": "user", "content": prompt}
    ]
)
message = response.choices[0].message.content
```

El mensaje se muestra en una interfaz tipo chat:

```python
with st.chat_message("assistant"):
    st.markdown(message)
```

---

## Posibles mejoras

### Inteligencia y UX

* Añadir explicaciones visuales del consumo normal vs. alto o bajo.
* Incluir indicadores de eficiencia energética.
* Visualizar el **estado online/offline de cada zona** con iconos.

### Visualización

* Mostrar **líneas de tendencia semanales**.
* Añadir **desviaciones estándar** o bandas de referencia.

### Backend

* Cachear resultados para acelerar tiempos de respuesta:

  ```python
  @st.cache_data
  def load_data_from_tb_cached(...):
      ...
  ```
* Mejorar la gestión de errores API por zona.

### Exportación y comparación

* Permitir exportar gráficos y datos en CSV.
* Comparar con el mismo día de la semana anterior.