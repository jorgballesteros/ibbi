import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import random
import time
import os
from collections import deque
from datetime import datetime, timedelta
from openai import OpenAI

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

load_from_csv = False

# --- CONFIGURACION INICIAL ---
st.set_page_config(layout="wide")
st.title("iBBi - Comparativa de Consumo Energético")

# --- VARIABLE A VISUALIZAR ---
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

# --- CONFIGURACIÓN THINGSBOARD ---
tb_url = st.secrets["TB_API_URL"]
tb_url = tb_url if tb_url.endswith("/") else tb_url + "/"

# Obtener token de ThingsBoard
tmp_folder = os.path.join(DIR_PATH, "tmp")
if not os.path.exists(tmp_folder):
    os.makedirs(tmp_folder)

token_file = os.path.join(DIR_PATH, "tmp", "token.txt")
if os.path.exists(token_file):
    with open(token_file, "r") as f:
        token = f.read().strip()
        if token.startswith("Bearer "):
            token = token[7:]
else:
    print("❌ No se encontró el token. Asegúrate de haberlo generado previamente.")
    exit()

# --- SELECCIÓN DE FECHA ---
now = datetime.now()
today = datetime.now().date()
yesterday = today - timedelta(days=1)

cola, colb, colc = st.columns([1, 1, 1])
with cola:
    selected_date = st.date_input("Selecciona una fecha", value=yesterday, max_value=today)
with colb:
    key = st.selectbox("Variable a visualizar", list(key_map.values()), index=0)
    # Mapeo inverso de clave
    src_key = next((k for k, v in key_map.items() if v == key), None)
with colc:
    st.write("")
    # load_from_csv = st.checkbox(label="Cargar desde CSV", value=True, help="Si no está marcado, se cargarán los datos desde ThingsBoard. Si está marcado, se cargarán los datos desde archivos CSV locales.")

# --- ZONAS DISPONIBLES ---
# Mapeo de zonas a nombres
device_map = {
    "zonaalta": "Zona Alta",
    "zonamedia": "Zona Media",
    "zonabaja": "Zona Baja"
}
device_names = device_map.keys()
# Mapeo de zonas a ids
device_id_map = {
    "zonaalta": "3d76ce90-24cc-11f0-93b2-b714401cbb0f",
    "zonamedia": "73d802b0-24cc-11f0-874c-af5d629c6095",
    "zonabaja": "1d6c4040-24cb-11f0-93b2-b714401cbb0f"
}

# --- CARGA DE DATOS ---
def prepare_dataframe(df, key, name, date):
    if "timestamp" not in df.columns:
        df = df.rename({"ts":"timestamp"}, axis=1)
    df["fecha"] = pd.to_datetime(df["timestamp"]).dt.date
    df = df[df["fecha"] == date]
    df = df[["timestamp", "fecha", key]]
    df = df.rename({key:key_map[key]}, axis=1)
    df['zona'] = name
    return df

def load_data_from_csv(date):
    print(f"🔄 Cargando datos desde CSV para la fecha {date}...")
    df = pd.DataFrame()
    try:
        for name in device_names:
            df_zone = pd.read_csv("data/ibbi_energia_"+name+"_1h.csv")
            df_zone = prepare_dataframe(df_zone, src_key, name, date)
            df = pd.concat([df, df_zone], ignore_index=True)

        df = df.sort_values(by=["timestamp", "zona"]).reset_index(drop=True)
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame()

def get_latest_data_from_tb(device_id, key):
    url = f"{tb_url}/api/plugins/telemetry/DEVICE/{device_id}/values/timeseries?limit=1&keys={key}"
    headers = {
        "X-Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    if key not in data:
        return None
    latest_value = data[key][0]
    return {
        "ts": datetime.fromtimestamp(int(latest_value["ts"]) / 1000),
        "value": float(latest_value["value"])
    }

def get_data_from_tb(device_id, key, start_ts, end_ts):
    url = f"{tb_url}/api/plugins/telemetry/DEVICE/{device_id}/values/timeseries"
    params = {
        "keys": src_key,
        "startTs": start_ts,
        "endTs": end_ts,
        "interval": 3600000,  # 1 hora
        "limit": 24,
        "agg": "AVG"
    }
    headers = {
        "X-Authorization": f"Bearer {token}"
    }
    # Realizar la solicitud a ThingsBoard
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    # Procesar resultados
    if src_key not in data:
        return pd.DataFrame()
    
    valores = [
        {
            "ts": datetime.fromtimestamp(int(item["ts"]) / 1000),
            src_key: float(item["value"])
        }
        for item in data[src_key]
    ]
    return pd.DataFrame(valores)

def load_data_from_tb(date):
    df = pd.DataFrame()
    
    # Rango horario del día
    start_ts = int(datetime.combine(date, datetime.min.time()).timestamp() * 1000)
    end_ts = int(datetime.combine(date + timedelta(days=1), datetime.min.time()).timestamp() * 1000)
    try:
        print(f"🔄 Cargando datos desde ThingsBoard para la fecha {date}...")
        for name, device_id in device_id_map.items():
            latest_data = get_latest_data_from_tb(device_id, src_key)
            last_dt = latest_data["ts"] if latest_data else None
            print(f"Último dato de {name} [{device_id}]: {last_dt}")
            df_zone = get_data_from_tb(device_id, src_key, start_ts, end_ts)
            df_zone["zona"] = name
            if not df_zone.empty:
                df_zone = prepare_dataframe(df_zone, src_key, name, date)
                df = pd.concat([df, df_zone], ignore_index=True)

        if not df.empty:
            df = df.sort_values(by=["timestamp", "zona"]).reset_index(drop=True)
        
        return df

    except:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame()
    
# Cargar datos desde CSV o ThingsBoard
if load_from_csv:
    df_day = load_data_from_csv(selected_date)
    df_vs = load_data_from_csv(selected_date - timedelta(days=1))
else:
    df_day = load_data_from_tb(selected_date)
    df_vs = load_data_from_tb(selected_date - timedelta(days=1))

if df_day.empty:
    st.warning("No hay datos disponibles para la fecha seleccionada.")
else:
    # Generamos las gráficas y métricas
    col1, col2, col3 = st.columns([2, 3, 1])
    with col2:
        fig = px.area(
            df_day,
            x="timestamp",
            y=key,
            color="zona",
            markers=True,
            labels={"timestamp": "Hora", key: key.upper()},
            title=f"{key} horaria",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig, use_container_width=True)
    with col1:
        df_sum_pie = df_day.groupby("zona")[key].sum().reset_index()
        df_sum_pie = df_sum_pie.sort_values(by="zona")
        fig_pie = px.pie(
            df_sum_pie, 
            values=key, 
            names="zona",
            category_orders={'zona': df_sum_pie['zona'].tolist()},
            title="Distribución por zona",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    with col3:
        st.subheader("Métricas")
        # Agregar métricas por hora
        df_group = df_day.groupby("timestamp").agg({key: "sum"}).reset_index()
        total_value = df_group[key].sum().round()
        avg_value = df_group[key].mean()
        max_value = df_group[key].max()
        hora_max = df_group[df_group[key] == max_value]["timestamp"].values[0]

        if not df_vs.empty:
            df_vs_group = df_vs.groupby("timestamp").agg({key: "sum"}).reset_index()
            total_value_vs = df_vs_group[key].sum().round()
            delta_total_value = total_value - total_value_vs
            avg_value_vs = df_vs_group[key].mean()
            delta_avg_value = avg_value - avg_value_vs
            max_value = df_vs_group[key].max()
            st.metric("Total", f"{total_value:.2f} {key_unit_map[key]}", f"{delta_total_value:.2f} {key_unit_map[key]}")
            st.metric("Promedio", f"{avg_value:.2f} {key_unit_map[key]}", f"{delta_avg_value:.2f} {key_unit_map[key]}")
        else:
            st.metric("Total", f"{total_value:.2f} {key_unit_map[key]}")
            st.metric("Promedio", f"{avg_value:.2f} {key_unit_map[key]}")
        
        st.metric("Máximo", f"{max_value:.2f} {key_unit_map[key]}", f"a las {hora_max}")

    col4, col5 = st.columns([1, 2])
    with col4:
        df_bar = pd.DataFrame({
            "fecha": [selected_date - timedelta(days=1), selected_date],
            "total": [total_value_vs, total_value]
        })
        fig_bar = px.bar(
            df_bar, 
            x="fecha", 
            y="total",
            color="fecha",
            text_auto=True,
            labels={"total": f"{key} {key_unit_map[key]}"},
            title="Comparativa diaria",
            color_discrete_sequence=px.colors.qualitative.Set2)

        st.plotly_chart(fig_bar, use_container_width=True)
    with col5:
        st.subheader("Mensaje al alumno")
        openai = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        # Set a default model
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-4o-mini"
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = deque(maxlen=7)  # Limit history to last 7 messages

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        if not df_vs.empty:
            # Generate user input
            prompt = f"Analiza el consumo de {key} del día {selected_date.strftime('%d/%m/%Y')} y compara con el día anterior. " \
                    f"El consumo total del día anterior fue de {total_value_vs} kWh y el día seleccionado {total_value} kWh." \
                    f"El consumo promedio del día anterior fue de {avg_value_vs} kWh y el día seleccionado {avg_value} kWh." \
                    f"El consumo máximo del día anterior fue de {avg_value_vs} kWh y el día seleccionado {avg_value} kWh." \
                    f"Solo debes emitir un mensaje de concienciación al alumnado. Si la difrencia es menor de +/-5% emite un mensaje neutro, si es un incremento superior a 5% emite un mensaje negaivo y si se reduce más de 5% uno positivo"
        else:
            prompt = f"No dispones de datos del dia entorior. Solo analiza el consumo de {key} del día {selected_date.strftime('%d/%m/%Y')}. " \
                     f"El consumo total del día seleccionado es {total_value} kWh. El promedio es {avg_value} kWh y el máximo es {max_value} kWh a las {hora_max.strftime('%H:%M')}." \
                     f"Se conciso y claro."

        if st.button("Generar mensaje"):
            with st.chat_message("assistant"):
                st.markdown("Generando mensaje...")
            try:
                response = openai.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": "system", "content": "Eres un asistente experto en análisis de consumo energético."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=500
                )
                message = response.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": message})
                with st.chat_message("assistant"):
                    st.markdown(message)
            except Exception as e:
                st.error(f"Error al generar el mensaje: {e}")

# --- REFRESCO AUTOMÁTICO (en producción) ---
time.sleep(3600)
st.rerun()
