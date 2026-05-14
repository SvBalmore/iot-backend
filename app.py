from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# ----------- CONEXION A MONGODB ----------
# 🔴 REEMPLAZA TU URI AQUI
MONGO_URI = "mongodb+srv://balmorechavez123_db_user:tognDnbWokhtQmHY@CLUSTER.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(
        MONGO_URI,
        tls=True,
        serverSelectionTimeoutMS=5000
    )

    # Intentar conexión
    client.server_info()
    print("✅ Conectado a MongoDB correctamente")

except Exception as e:
    print("❌ Error de conexión con MongoDB:", e)


# ----------- BASE DE DATOS ----------
db = client["iot_data"]
collection = db["sensores"]


# ----------- RUTA BASE ----------
@app.route("/", methods=["GET"])
def home():
    return "Servidor IoT activo ✅", 200


# ----------- RECEPCION DE DATOS ----------
@app.route("/datos", methods=["POST"])
def recibir_datos():
    data = request.get_json()

    print("\n==============================")
    print("📥 NUEVO PAQUETE RECIBIDO")
    print("==============================")
    print(data)

    try:
        # ✅ GUARDAR EN MONGODB
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


# ----------- RUN LOCAL ----------
if __name__ == "__main__":
    app.run(debug=True)