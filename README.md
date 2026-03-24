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


# 📊 API Promedio de Calificaciones - ITIC

API REST desarrollada con Python y Flask que calcula el promedio 
de calificaciones de un estudiante.

## 📋 Descripción

Este proyecto forma parte de la materia **Aplicaciones Web Orientadas 
a Servicios (ITIC 2025-2026)**. El objetivo es practicar el uso de 
rutas en Flask, lectura de datos en formato JSON y generación de 
respuestas JSON.

## 🎯 Propósito

Recibir el nombre de un estudiante y una lista de calificaciones, 
calcular automáticamente el promedio y devolver el resultado 
en formato JSON.

## 🚀 Endpoint

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/promedio` | Calcula el promedio de calificaciones |

## 📥 Ejemplo de petición
```json
POST /promedio
{
    "nombre": "Juan",
    "calificaciones": [80, 90, 85, 70]
}
```

## 📤 Ejemplo de respuesta
```json
{
    "nombre": "Juan",
    "calificaciones": [80, 90, 85, 70],
    "total_materias": 4,
    "promedio": 81.25,
    "aprobado": true
}
```

## 🛠 Tecnologías

- Python 3.14
- Flask 3.x

## ⚙️ Instalación
```bash
git clone https://github.com/tu-usuario/api_promedio.git
cd api_promedio
python -m venv venv
venv\Scripts\activate
pip install flask
```

## ▶️ Ejecutar
```bash
python app.py
```

Probar en Postman:
- Método: POST
- URL: `http://127.0.0.1:5000/promedio`
- Body: raw → JSON

## 📁 Estructura

| Archivo | Descripción |
|---|---|
| `app.py` | Aplicación principal con el endpoint |



## app.py
```bash
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
```
![pruebas](https://github.com/natalyvictoria-jpg/3.9.-Ejercicios-de-API/raw/main/j.jpeg)

![pruebas](https://github.com/natalyvictoria-jpg/3.9.-Ejercicios-de-API/raw/main/u.jpeg)

![pruebas](https://github.com/natalyvictoria-jpg/3.9.-Ejercicios-de-API/raw/main/n.jpeg)


# 🌡️ API Convertidor de Temperaturas - ITIC

API REST desarrollada con Python y Flask que convierte temperaturas 
entre Celsius y Fahrenheit.

## 📋 Descripción

Este proyecto forma parte de la materia **Aplicaciones Web Orientadas 
a Servicios (ITIC 2025-2026)**. El objetivo es practicar el manejo 
de solicitudes HTTP, estructuras condicionales y procesamiento 
simple de datos dentro de una API.

## 🎯 Propósito

Recibir un valor de temperatura y su escala de origen, aplicar 
la fórmula de conversión correspondiente y devolver el resultado 
en formato JSON.

## 🚀 Endpoint

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/convertir-temperatura` | Convierte entre Celsius y Fahrenheit |

## 📌 Escalas válidas

| Escala | Descripción |
|---|---|
| `C` | Celsius → convierte a Fahrenheit |
| `F` | Fahrenheit → convierte a Celsius |

## 📥 Ejemplo de petición — Celsius a Fahrenheit
```json
POST /convertir-temperatura
{
    "valor": 100,
    "escala": "C"
}
```

## 📤 Ejemplo de respuesta
```json
{
    "valor_original": "100°C",
    "escala_origen": "Celsius",
    "resultado": 212.0,
    "valor_convertido": "212.0°F",
    "escala_destino": "Fahrenheit"
}
```

## 📥 Ejemplo de petición — Fahrenheit a Celsius
```json
POST /convertir-temperatura
{
    "valor": 32,
    "escala": "F"
}
```

## 📤 Ejemplo de respuesta
```json
{
    "valor_original": "32°F",
    "escala_origen": "Fahrenheit",
    "resultado": 0.0,
    "valor_convertido": "0.0°C",
    "escala_destino": "Celsius"
}
```

## 🛠 Tecnologías

- Python 3.14
- Flask 3.x

## ⚙️ Instalación
```bash
git clone https://github.com/tu-usuario/api_convertidor.git
cd api_convertidor
python -m venv venv
venv\Scripts\activate
pip install flask
```

## ▶️ Ejecutar
```bash
python app.py
```

Probar en Postman:
- Método: POST
- URL: `http://127.0.0.1:5000/convertir-temperatura`
- Body: raw → JSON

## 📁 Estructura

| Archivo | Descripción |
|---|---|
| `app.py` | Aplicación principal con el endpoint |

## app.py
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



