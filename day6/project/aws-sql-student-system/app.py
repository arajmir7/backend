from flask import Flask, request, jsonify
from db import get_connection

from flask import Flask, request, jsonify
from notifier import mail, send_enrollment_email
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Automation Config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME') # Add this to your .env!
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD') # Your App Password

mail.init_app(app)

@app.route("/")
def home():
    return "AWS Student SQL System is LIVE 🚀"

@app.route("/students", methods=["GET"])
def get_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, course, email FROM students;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    students = [
        {"id": r[0], "name": r[1], "course": r[2], "email": r[3]}
        for r in rows
    ]
    return jsonify(students)

@app.route("/students", methods=["POST"])
@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, course, email) VALUES (%s, %s, %s)",
        (data["name"], data["course"], data["email"])
    )
    conn.commit()
    cur.close()
    conn.close()

    send_enrollment_email(app, data["email"], data["name"])

    return {"message": "Student added and notification sent!"}, 201

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Student deleted"}, 200

if __name__ == "__main__":
    app.run(debug=True)
