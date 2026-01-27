import requests

# The data for our first student
new_student = {
    "name": "Pristine Dev",
    "course": "Backend Engineering",
    "email": "your-test-email@example.com" # Put a real email here to see the magic
}

response = requests.post("http://127.0.0.1:5000/students", json=new_student)

if response.status_code == 201:
    print("🔥 SWAG! Student added and automation triggered.")
else:
    print(f"💀 L, something went wrong: {response.text}")