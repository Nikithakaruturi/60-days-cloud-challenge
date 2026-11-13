
import os
import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app, resources={
    r"/api/*": {"origins": "http://localhost:5173"}
})


# MySQL database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3307)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


# Health check API
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "message": "Backend API is running"
    })


# Get all employees from MySQL
@app.route("/api/employees", methods=["GET"])
def get_employees():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT id, name, email, department FROM employees ORDER BY id"
        )
        employees = cursor.fetchall()
        return jsonify(employees)

    finally:
        cursor.close()
        connection.close()


# Add employee to MySQL
@app.route("/api/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    if not data or not all(
        data.get(field) for field in ["name", "email", "department"]
    ):
        return jsonify({"error": "All fields are required"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        query = """
            INSERT INTO employees (name, email, department)
            VALUES (%s, %s, %s)
        """

        values = (
            data["name"],
            data["email"],
            data["department"]
        )

        cursor.execute(query, values)
        connection.commit()

        employee_id = cursor.lastrowid

        return jsonify({
            "id": employee_id,
            "name": data["name"],
            "email": data["email"],
            "department": data["department"]
        }), 201

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
