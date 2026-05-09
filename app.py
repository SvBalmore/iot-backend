from flask import Flask, request, jsonify

app = Flask(__name__)

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

    # ----------- DATOS GENERALES ----------
    dia = data.get("dia")
    hora = data.get("hora")

    print(f"📅 Dia: {dia}")
    print(f"⏰ Hora: {hora}")

    print("\n🌍 Zonas:")

    # ----------- RECORRER ZONAS ----------
    zonas = data.get("zonas", [])

    for zona in zonas:
        nombre = zona.get("zona")
        temp = zona.get("temperatura")
        hum = zona.get("humedad")
        pres = zona.get("presion")

        print("\n-----------------------------")
        print(f"Zona: {nombre}")
        print(f"🌡️ Temp: {temp} °C")
        print(f"💧 Humedad: {hum}%")
        print(f"🧭 Presion: {pres} hPa")

    print("\n✅ Datos procesados correctamente")

    return jsonify({
        "status": "ok",
        "mensaje": "Datos recibidos correctamente"
    }), 200


# ----------- RUN LOCAL ----------
if __name__ == "__main__":
    app.run(debug=True)