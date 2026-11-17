from flask import Flask, render_template, request, jsonify
from conversions import CONVERSIONS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json(silent=True) or {}
    category = data.get("category")
    conversion = data.get("conversion")
    raw_value = data.get("value")

    try:
        value = float(raw_value)
    except (TypeError, ValueError):
        return jsonify({"error": "Please enter a valid number."}), 400

    if category not in CONVERSIONS or conversion not in CONVERSIONS[category]:
        return jsonify({"error": "Please select a valid conversion."}), 400

    # Absolute-zero validation for temperature conversions.
    if category == "temperature":
        lower_limits = {
            "Kelvin to Celsius": 0,
            "Celsius to Fahrenheit": -273.15,
            "Celsius to Kelvin": -273.15,
            "Fahrenheit to Celsius": -459.67,
        }
        if conversion in lower_limits and value < lower_limits[conversion]:
            return jsonify({"error": "Temperature cannot be below absolute zero."}), 400

    answer = CONVERSIONS[category][conversion](value)
    return jsonify({
        "input": value,
        "conversion": conversion,
        "result": round(answer, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
