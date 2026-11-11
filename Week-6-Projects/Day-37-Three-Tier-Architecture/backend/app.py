from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "message": "Backend API is running"})

@app.route("/api/employees", methods=["GET"])
def get_employees():
    return jsonify([])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
