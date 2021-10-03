from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, SubmitField, validators, FloatField
import sqlite3

# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


app = Flask(__name__)

Bootstrap(app)
all_books = []
count = 0
app.secret_key = "abcddkladandsakd"


class BookForm(FlaskForm):
    title = StringField(label='title', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    rating = FloatField(label='Rating 1 to 10', validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField(label='Submit Response')


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global count
    form = BookForm()
    if form.validate_on_submit() and request.method == "POST":
        print(form.rating.data)
        count += 1
        new_review = {
            "count": count,
            "title": form.title.data,
            "author": form.author.data,
            "rating": form.rating.data,
        }

        db = sqlite3.connect("books-collection.db")
        cursor = db.cursor()
        cursor.execute(f"INSERT OR IGNORE INTO  books VALUES(?,?,?,?)",
                       (new_review['count'], new_review['title'], new_review['author'], new_review['rating']))
        db.commit()

        all_books.append(new_review)
        print(all_books)
        return redirect("/")
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
