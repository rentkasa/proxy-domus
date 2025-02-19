from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuración de la API de Domus
DOMUS_API_URL = "https://apiv3get.domus.la/inmuebles/lista"
DOMUS_API_TOKEN = "APP_USR_2f0f2de35385c25ab964cc6fc00fe806"

@app.route("/get_inmuebles", methods=["GET"])
def get_inmuebles():
    """Proxy para obtener la lista de inmuebles desde Domus."""
    headers = {"Authorization": f"Bearer {DOMUS_API_TOKEN}"}
    response = requests.get(DOMUS_API_URL, headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "No se pudo obtener la información de Domus"}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

