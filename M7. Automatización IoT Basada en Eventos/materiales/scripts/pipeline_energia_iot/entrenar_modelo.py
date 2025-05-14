import pandas as pd
import os
from sklearn.ensemble import IsolationForest
import joblib

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

df_clean = pd.read_csv(DIR_PATH+"/data/consumo_potencia_min_limpio.csv",  parse_dates=["dt"])
df_clean.set_index("dt", inplace=True)

# Usamos sólo la columna normalizada
X = df_clean[["potencia_norm"]]

# Entrenamos el modelo
model = IsolationForest(contamination=0.025, random_state=42)
model.fit(X)

df_clean["anomaly"] = model.predict(X)

joblib.dump(model, DIR_PATH+"/models/isolationforest.pkl")