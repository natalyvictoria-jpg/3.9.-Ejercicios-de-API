# 3.9.-Ejercicios-de-API

<p align="center">
  <img width="100%" src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake.svg" alt="" />
</p>

<h1 align="center">
  🌐💻 APLICACIONES WEB ORIENTADA A SERVICIOS
</h1>

## GTID153

📘 **Materia:** Aplicaciones Web Orientada a Servicios  
👩‍💻❤️ **Nombre:** Nataly Victoria Gonzalez Aviles  
🏫 **Proyecto o Actividad:** 3.9.-Ejercicios-de-API
📅 **Unidad:** 3  
⚙️ **Lenguaje:** Python  
🧠 **Propósito:** Desarrollar aplicaciones web utilizando APIs diferentes, aplicando los conocimientos adquiridos en la unidad 3 y comprendiendo su funcionamiento mediante su implementación en Python.  
👨‍🏫 **Docente:** Anastacio Rodriguez Garcia


# Api Promedio

![pruebas](https://github.com/natalyvictoria-jpg/3.9.-Ejercicios-de-API/raw/main/j.jpeg)

![pruebas](https://github.com/natalyvictoria-jpg/3.9.-Ejercicios-de-API/raw/main/u.jpeg)

![pruebas](https://github.com/natalyvictoria-jpg/3.9.-Ejercicios-de-API/raw/main/n.jpeg)

# Api Convertidor

# app.py
```bash
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
```

![pruebas](https://github.com/natalyvictoria-jpg/3.9.-Ejercicios-de-API/raw/main/cvn.jpeg)

# Conversión inversa de Fahrenheit a Celsius:
![pruebas](https://github.com/natalyvictoria-jpg/3.9.-Ejercicios-de-API/raw/main/bts.jpeg)



