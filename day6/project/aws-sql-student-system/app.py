from flask import Flask, request, jsonify
from db import get_connection
from notifier import mail, send_enrollment_email
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# =====================
# Mail Configuration
# =====================
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail.init_app(app)

# =====================
# Routes
# =====================

@app.route("/")
def home():
    return "AWS Student SQL System is LIVE 🚀"

@app.route("/students", methods=["GET"])
def get_students():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, name, course, email FROM students")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows), 200

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data:
        return {"error": "Invalid JSON body"}, 400

    name = data.get("name")
    course = data.get("course")
    email = data.get("email")

    if not name or not email:
        return {"error": "Name and email are required"}, 400

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO students (name, course, email) VALUES (%s, %s, %s)",
            (name, course, email)
        )
        conn.commit()
    finally:
        cur.close()
        conn.close()

    send_enrollment_email(app, email, name)

    return {"message": "Student added and notification sent!"}, 201

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM students WHERE id = %s", (id,))
        conn.commit()
    finally:
        cur.close()
        conn.close()

    return {"message": "Student deleted"}, 200

# =====================
# App Runner
# =====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
