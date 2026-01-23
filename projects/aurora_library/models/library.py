# models/library.py
"""Library core logic: CRUD, searching, issuing, persistence."""

import json
from typing import Dict, Optional
from projects.aurora_library.models.book import Book
import os


class Library:
    def __init__(self):
        # isbn -> Book
        self.books: Dict[str, Book] = {}

    # ----- Persistence -----
    def load(self, path: str):
        if not os.path.exists(path):
            return
        with open(path, "r", encoding="utf-8") as fh:
            obj = json.load(fh)
            for isbn, data in obj.items():
                self.books[isbn] = Book.from_dict(data)

    def save(self, path: str):
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({isbn: b.to_dict() for isbn, b in self.books.items()}, fh, indent=2)

    # ----- CRUD -----
    def add_book(self, book: Book):
        if book.isbn in self.books:
            self.books[book.isbn].copies += book.copies
        else:
            self.books[book.isbn] = book

    def remove_book(self, isbn: str):
        if isbn in self.books:
            del self.books[isbn]
            return True
        return False

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        return self.books.get(isbn)

    def search(self, q: str):
        q = q.lower().strip()
        results = []
        for b in self.books.values():
            if q in b.title.lower() or q in b.author.lower() or q in b.isbn.lower() or q in " ".join(b.tags).lower():
                results.append(b)
        return results

    # ----- Issue / Return -----
    def issue_book(self, isbn: str) -> bool:
        b = self.books.get(isbn)
        if not b or b.copies < 1:
            return False
        b.copies -= 1
        return True

    def return_book(self, isbn: str) -> bool:
        b = self.books.get(isbn)
        if not b:
            return False
        b.copies += 1
        return True

    # ----- Utilities -----
    def list_books(self):
        return list(self.books.values())

    def stats(self):
        total_titles = len(self.books)
        total_copies = sum(b.copies for b in self.books.values())
        popular = sorted(self.books.values(), key=lambda x: x.copies, reverse=True)[:5]
        return {"titles": total_titles, "copies": total_copies, "popular": popular}
