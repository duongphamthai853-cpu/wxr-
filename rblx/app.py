from flask import Flask, request, jsonify

app = Flask(__name__)

# Danh sách whitelist
WHITELIST = {
    123456789,
    987654321,
    2622002334
}

@app.route("/")
def home():
    return "Whitelist API is running!"

@app.route("/api/check", methods=["POST"])
def check():
    data = request.get_json()

    creator = data.get("creator")

    if creator in WHITELIST:
        return jsonify({
            "success": True
        })

    return jsonify({
        "success": False,
        "message": "Not licensed"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)