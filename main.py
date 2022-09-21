from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


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

