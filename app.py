from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# ----------- CONEXION A MONGODB ----------
# 🔴 REEMPLAZA CON TU URI REAL
MONGO_URI = "mongodb+srv://balmorechavez123_db_user:tognDnbWokhtQmHY@iot-proyecto.61kstlx.mongodb.net/?appName=iot-proyecto"

client = None
collection = None

try:
    client = MongoClient(
        MONGO_URI,
        tls=True,
        tlsAllowInvalidCertificates=True,  # evita fallo SSL en Render
        serverSelectionTimeoutMS=5000
    )

    # Intentar conexión (esto valida la conexión)
    client.server_info()

    print("✅ Conectado a MongoDB correctamente")

    # Base de datos y colección
    db = client["iot_data"]
    collection = db["sensores"]

except Exception as e:
    print("⚠️ No se pudo conectar a MongoDB:", e)
    print("⚠️ El servidor seguirá funcionando sin base de datos")

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

    # ----------- GUARDAR EN MONGO (SI ESTA DISPONIBLE) ----------
    if collection is not None:
        try:
            collection.insert_one(data)
            print("✅ Datos guardados en MongoDB")

        except Exception as e:
            print("❌ Error al guardar en MongoDB:", str(e))
    else:
        print("⚠️ MongoDB no disponible, no se guardaron los datos")

    return jsonify({
        "status": "ok"
    }), 200


# ----------- RUN LOCAL ----------
if __name__ == "__main__":
    app.run(debug=True)
