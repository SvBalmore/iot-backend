from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# ----------- CONEXION A MONGODB ----------
MONGO_URI = "mongodb+srv://balmorechavez123_db_user:tognDnbWokhtQmHY@iot-proyecto.61kstlx.mongodb.net/?appName=iot-proyecto"

client = MongoClient(MONGO_URI)

db = client["iot_data"]  # base de datos
collection = db["sensores"]  # colección

# ----------- RUTA BASE ----------
@app.route("/", methods=["GET"])
def home():
    return "Servidor IoT activo ✅", 200


# ----------- RECEPCION DE DATOS ----------
@app.route("/datos", methods=["POST"])
def recibir_datos():
    data = request.get_json()

    print("\n📥 NUEVO PAQUETE RECIBIDO")
    print(data)

    try:
        # 💾 GUARDAR EN MONGODB
        collection.insert_one(data)

        print("✅ Datos guardados en MongoDB")

        return jsonify({
            "status": "ok",
            "mensaje": "Datos guardados correctamente"
        }), 200

    except Exception as e:
        print("❌ Error al guardar:", str(e))

        return jsonify({
            "status": "error",
            "mensaje": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
