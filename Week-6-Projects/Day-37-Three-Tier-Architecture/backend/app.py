from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

employees = []


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "message": "Backend API is running"
    })


@app.route("/api/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)


@app.route("/api/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    if not data or not all(data.get(field) for field in ["name", "email", "department"]):
        return jsonify({"error": "All fields are required"}), 400

    employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "email": data["email"],
        "department": data["department"]
    }

    employees.append(employee)

    return jsonify(employee), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
