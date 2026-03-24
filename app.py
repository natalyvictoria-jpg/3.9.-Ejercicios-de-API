from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400

    if "valor" not in datos:
        return jsonify({"error": "El campo 'valor' es requerido"}), 400

    if "escala" not in datos:
        return jsonify({"error": "El campo 'escala' es requerido"}), 400

    valor  = datos["valor"]
    escala = datos["escala"].upper()

    if escala == "C":
        resultado     = (valor * 9/5) + 32
        escala_origen = "Celsius"
        escala_destino = "Fahrenheit"
        simbolo_origen  = "°C"
        simbolo_destino = "°F"

    elif escala == "F":
        resultado      = (valor - 32) * 5/9
        escala_origen  = "Fahrenheit"
        escala_destino = "Celsius"
        simbolo_origen  = "°F"
        simbolo_destino = "°C"

    else:
        return jsonify({
            "error": "Escala invalida. Use 'C' para Celsius o 'F' para Fahrenheit"
        }), 400

    return jsonify({
        "valor_original": f"{valor}{simbolo_origen}",
        "escala_origen":  escala_origen,
        "resultado":      round(resultado, 2),
        "valor_convertido": f"{round(resultado, 2)}{simbolo_destino}",
        "escala_destino": escala_destino
    }), 200


if __name__ == '__main__':
    app.run(debug=True)