# 📘 Day 5 – OOP + File Handling (Python)

## What Today Was About
Day 5 was a turning point. Until now, most programs ran once and forgot everything.  
Today was about building **real programs** — programs that:

- Have structure  
- Use classes properly  
- Save data  
- Don’t break when restarted  

This felt like actual backend development, not just practice.

---

## 🧠 Object-Oriented Programming (OOP)

### What is OOP?
OOP is a way to organize code so it behaves like real-world things.

Instead of writing long scripts with random variables, we use:
- Classes
- Objects
- Methods

This makes code cleaner, reusable, and scalable.

---

### Classes and Objects
A class is a blueprint.  
An object is the real thing created from that blueprint.

```python
class Student:
    def __init__(self, id, name, course):
        self.id = id
        self.name = name
        self.course = course
