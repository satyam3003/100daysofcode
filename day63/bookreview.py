from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, SubmitField, validators, FloatField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "abcddkladandsakd"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new_book_collection_db.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)


##CREATE TABLE
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


class BookForm(FlaskForm):
    title = StringField(label='title', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    rating = FloatField(label='Rating 1 to 10', validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField(label='Submit Response')


class EditForm(FlaskForm):
    rating = FloatField(label='Rating 1 to 10', validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField(label='Submit Response')


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global count
    form = BookForm()
    if form.validate_on_submit() and request.method == "POST":
        new_review = {
            "title": form.title.data,
            "author": form.author.data,
            "rating": form.rating.data,
        }

        new_book = Books(title=new_review['title'], author=new_review['author'], rating=new_review['rating'])
        db.session.add(new_book)
        db.session.commit()

        return redirect("/")
    return render_template('add.html', form=form)


@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    edit_id = Books.query.get(id)
    form = EditForm()
    if request.method == "POST" and form.validate_on_submit():
        edit_id.rating = form.rating.data
        db.session.commit()
        return redirect("/")

    return render_template('edit.html', form=form, info=edit_id)


@app.route("/delete/<id>")
def delete(id):
    delete_id = Books.query.get(id)
    db.session.delete(delete_id)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
