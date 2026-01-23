# web/app.py
from flask import Flask, render_template, request, redirect, url_for
from aurora_library.models.library import Library
from aurora_library.models.book import Book
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "library.json"
lib = Library()
lib.load(str(DATA))

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q", "")
    results = lib.search(q) if q else lib.list_books()
    return render_template("index.html", books=results, q=q)

@app.route("/add", methods=["POST"])
def add():
    data = request.form
    from models.book import Book
    book = Book(isbn=data["isbn"], title=data["title"], author=data["author"], copies=int(data.get("copies",1)))
    lib.add_book(book)
    lib.save(str(DATA))
    return redirect(url_for("index"))

@app.route("/issue/<isbn>")
def issue(isbn):
    lib.issue_book(isbn)
    lib.save(str(DATA))
    return redirect(url_for("index"))

@app.route("/return/<isbn>")
def ret(isbn):
    lib.return_book(isbn)
    lib.save(str(DATA))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
