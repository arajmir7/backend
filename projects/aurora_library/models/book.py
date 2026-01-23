# models/book.py
"""Book model for Aurora Library."""

from dataclasses import dataclass, asdict


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    copies: int = 1
    tags: list = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data: dict):
        return Book(
            isbn=data["isbn"],
            title=data["title"],
            author=data["author"],
            copies=data.get("copies", 1),
            tags=data.get("tags", []),
        )
