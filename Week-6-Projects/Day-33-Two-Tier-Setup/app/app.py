from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
	port=int(os.getenv("MYSQL_PORT", "3307")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")

    if not username:
        return "Please enter your name."

    connection = get_db_connection()
    cursor = connection.cursor()

    query = "INSERT INTO users (username) VALUES (%s)"
    cursor.execute(query, (username,))

    connection.commit()

    cursor.close()
    connection.close()

    return render_template("result.html", username=username)


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

