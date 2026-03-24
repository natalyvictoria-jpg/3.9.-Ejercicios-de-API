from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400

    if "nombre" not in datos:
        return jsonify({"error": "El campo 'nombre' es requerido"}), 400

    if "calificaciones" not in datos:
        return jsonify({"error": "El campo 'calificaciones' es requerido"}), 400

    if len(datos["calificaciones"]) == 0:
        return jsonify({"error": "La lista de calificaciones no puede estar vacia"}), 400

    nombre        = datos["nombre"]
    calificaciones = datos["calificaciones"]
    promedio      = sum(calificaciones) / len(calificaciones)

    respuesta = {
        "nombre":          nombre,
        "calificaciones":  calificaciones,
        "total_materias":  len(calificaciones),
        "promedio":        round(promedio, 2),
        "aprobado":        promedio >= 60
    }

    return jsonify(respuesta), 200


if __name__ == '__main__':
    app.run(debug=True)