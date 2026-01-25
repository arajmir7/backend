# Day 5 – OOP + File Handling in Python

## What I Worked On Today
Today was about writing **clean, structured Python code** using classes and saving data so it doesn’t disappear when the program stops.

Basically:
- Stop writing random scripts
- Start writing **real programs**

---

## 🧱 Object-Oriented Programming (OOP)

### Classes & Objects
A class is like a template, and an object is the real thing created from it.

Example:
```python
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
