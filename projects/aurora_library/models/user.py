# models/user.py
"""User and Librarian models."""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    user_id: str


@dataclass
class User(Person):
    pass


@dataclass
class Librarian(Person):
    employee_id: str

    def __repr__(self):
        return f"Librarian(name={self.name}, id={self.user_id}, emp={self.employee_id})"
