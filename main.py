from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

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

all_books = db.session.query(Book).all()
for book in all_books:
    print(book.title)
print(all_books)

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', libros = all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        data = request.form
        new_book = Book(title=data["title"], author=data["author"], rating=data["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<int:index>", methods=["POST", "GET"])
def edit(index):
    book = Book.query.get(index)
    if request.method == "POST":
        data = request.form
        rating_to_change = Book.query.get(index)
        rating_to_change.rating = data["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book_to_change = book)

@app.route("/change/<int:index>", methods=["POST", "GET"])   
def change_rating(index):
    if request.method == "POST":
        data = request.form
        rating_to_change = Book.query.get(index)
        rating_to_change.rating = data["rating"]
        db.session.commit()
        return redirect(url_for('home'))

@app.route("/delete/<int:index>", methods=["POST", "GET"])  
def delete(index):
    book_to_delete = Book.query.get(index)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

