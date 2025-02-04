from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    number = request.args.get("number", type=int)
    if number is None:
        return jsonify({"error": "Invalid number"}), 400
    
    properties = []
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Check if Armstrong number (example logic)
    sum_of_cubes = sum(int(digit) ** 3 for digit in str(number))
    if sum_of_cubes == number:
        properties.append("armstrong")

    return jsonify({
        "number": number,
        "properties": properties
    })

if __name__ == "__main__":
    app.run(debug=True)
