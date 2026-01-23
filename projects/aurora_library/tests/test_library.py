# tests/test_library.py
import unittest
from projects.aurora_library.models.library import Library
from projects.aurora_library.models.book import Book
from pathlib import Path
import tempfile
import json


class TestLibrary(unittest.TestCase):

    def test_add_issue_return(self):
        lib = Library()
        b = Book(isbn="x1", title="T", author="A", copies=2)
        lib.add_book(b)

        self.assertTrue(lib.issue_book("x1"))
        self.assertEqual(lib.find_by_isbn("x1").copies, 1)

        self.assertTrue(lib.return_book("x1"))
        self.assertEqual(lib.find_by_isbn("x1").copies, 2)

    def test_persistence(self):
        lib = Library()
        b = Book(isbn="x2", title="T2", author="B", copies=1)
        lib.add_book(b)

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            lib.save(tmp.name)
            path = tmp.name  # safe reference

        lib2 = Library()
        lib2.load(path)

        self.assertIsNotNone(lib2.find_by_isbn("x2"))

if __name__ == "__main__":
    unittest.main()
