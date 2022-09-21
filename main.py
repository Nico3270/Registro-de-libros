from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
all_books = []


#Creando una base de datos con SQLALchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(250), nullable=False)

db.create_all()
new_book = Book(id=2, title="El Sindrome de Ulises", author="J. K. Rowling", rating=9.5)
db.session.add(new_book)
db.session.commit()

@app.route('/')
def home():
    return render_template('index.html', libros = all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_data = {}
        data = request.form
        book_data["title"] = data["title"]
        book_data["author"] = data["author"]
        book_data["rating"] = data["rating"]
        all_books.append(book_data)
        print(all_books)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

