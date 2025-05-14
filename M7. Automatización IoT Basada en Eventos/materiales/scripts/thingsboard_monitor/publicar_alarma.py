import sys
import time
import requests
import os
from dotenv import load_dotenv

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# Cargar variables de entorno
load_dotenv()
tb_url = os.getenv("TB_API_URL")
device_id = os.getenv("TB_DEVICE_ID")

# Obtener token de ThingsBoard
token_file = os.path.join(DIR_PATH, "tmp", "token.txt")
if os.path.exists(token_file):
    with open(token_file, "r") as f:
        token = f.read().strip()
else:
    print("❌ No se encontró el token. Asegúrate de haberlo generado previamente.")
    exit()

value = sys.argv[1]  # valor anómalo detectado

url = f"{tb_url}/api/alarm"

headers = {
    "X-Authorization": f"Bearer {token}"
}
payload = {
  "type": "Fuera de Rango",
  "originator": {
    "id": device_id,
    "entityType": "DEVICE"
  },
  "severity": "CRITICAL",
  "acknowledged": False,
  "cleared": False,
  "startTs": round(time.time() * 1000),
  "details": {"valor": value},
  "propagate": True,
  "propagateToOwner": True,
  "propagateToTenant": True,
}

r = requests.post(url, json=payload, headers=headers)
print(f"🚨 Alarma enviada a ThingsBoard: {r.status_code}")
