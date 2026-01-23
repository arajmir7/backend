# cli/cli.py
"""Simple but pretty CLI for Aurora Library."""

from aurora_library.models.library import Library
from projects.aurora_library.models.book import Book
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "library.json"

def prompt_int(msg, default=None):
    try:
        return int(input(msg))
    except Exception:
        return default

def main():
    lib = Library()
    lib.load(str(DATA_PATH))

    print("✨ Welcome to Aurora Library (CLI demo)\n")
    while True:
        print("="*40)
        print("1) Add book  2) Remove book  3) Issue  4) Return")
        print("5) Search  6) Show all  7) Stats  8) Exit")
        choice = input("> ").strip()

        if choice == "1":
            isbn = input("ISBN: ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            copies = prompt_int("Copies (1): ", 1) or 1
            tags = input("Tags (comma separated, optional): ").split(",")
            tags = [t.strip() for t in tags if t.strip()]
            lib.add_book(Book(isbn, title, author, copies=copies, tags=tags))
            lib.save(str(DATA_PATH))
            print("✅ Book added/synced.")

        elif choice == "2":
            isbn = input("ISBN to remove: ").strip()
            ok = lib.remove_book(isbn)
            lib.save(str(DATA_PATH))
            print("✅ Removed." if ok else "⚠️ Not found.")

        elif choice == "3":
            isbn = input("ISBN to issue: ").strip()
            ok = lib.issue_book(isbn)
            lib.save(str(DATA_PATH))
            print("✅ Issued." if ok else "❌ Not available.")

        elif choice == "4":
            isbn = input("ISBN to return: ").strip()
            ok = lib.return_book(isbn)
            lib.save(str(DATA_PATH))
            print("✅ Returned." if ok else "⚠️ Unknown book.")

        elif choice == "5":
            q = input("Search by title/author/isbn/tag: ")
            found = lib.search(q)
            if not found:
                print("No matches.")
            else:
                for b in found:
                    print(f"- {b.title} by {b.author} | ISBN:{b.isbn} | copies:{b.copies}")

        elif choice == "6":
            for b in lib.list_books():
                print(f"- {b.title} by {b.author} | ISBN:{b.isbn} | copies:{b.copies}")

        elif choice == "7":
            s = lib.stats()
            print(f"Titles: {s['titles']}, Copies: {s['copies']}")
            print("Top by copies:")
            for b in s["popular"]:
                print(f"  {b.title} ({b.copies})")

        elif choice == "8":
            lib.save(str(DATA_PATH))
            print("Bye! Saved state.")
            break
        else:
            print("Try again — choose 1-8.")

if __name__ == "__main__":
    main()
