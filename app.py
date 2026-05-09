from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta básica para verificar que funciona
@app.route("/", methods=["GET"])
def home():
    return "Servidor IoT activo ✅", 200


# Endpoint que recibirá datos del ESP32
@app.route("/datos", methods=["POST"])
def recibir_datos():
    data = request.get_json()

    print("\n📥 Dato recibido:")
    print(data)

    respuesta = {
        "status": "ok",
        "mensaje": "Datos recibidos correctamente"
    }

    return jsonify(respuesta), 200


if __name__ == "__main__":
    app.run(debug=True)