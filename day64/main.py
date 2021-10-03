from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, number_range
import requests

# https://api.themoviedb.org/3/movie/550?api_key=e92e5bd98f3a9abe3d1f02035de8653c
API_KEY = "e92e5bd98f3a9abe3d1f02035de8653c"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False, default=2021)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String, nullable=False,
                        default="https://www.shortlist.com/media/images/2019/05/the-30-coolest-alternative-movie-posters-ever-2-1556670563-K61a-column-width-inline.jpg")

    def __repr__(self):
        return f'<Movie {self.title} {self.rating}>'


db.create_all()


class UpdateForm(FlaskForm):
    rating = FloatField(label="Your Rating outoff 10. e.g: 7.3",
                        validators=[DataRequired(), number_range(max=10, min=0, message="Rating out of range")])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class MovieNameForm(FlaskForm):
    name = StringField(label="Movie name", validators=[DataRequired()])
    submit = SubmitField(label="Search")


def add_new_movie(title, year, description, rating, ranking, review, img_url):
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=rating,
        ranking=ranking,
        review=review,
        img_url=img_url
    )

    db.session.add(new_movie)
    db.session.commit()


# add_new_movie()


@app.route("/")
def home():
    results = Movie.query.order_by(Movie.rating).all()
    a = results.reverse()
    return render_template("index.html", movies=results, total_movies=len(results))


@app.route("/edit/<id>", methods=["POST", "GET"])
def edit(id):
    edit_rating = Movie.query.get(id)
    form = UpdateForm()
    if request.method == "POST" and form.validate_on_submit():
        edit_rating.rating = form.rating.data
        edit_rating.review = form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=form, movie=edit_rating)


@app.route("/delete/<id>", methods=["POST", "GET"])
def delete(id):
    delete_movie = Movie.query.get(id)
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect("/")


@app.route("/add_moviename", methods=["POST", "GET"])
def add():
    form = MovieNameForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        print(name)
        parameter = {
            "api_key": API_KEY,
            "query": name,
            "language": "en-US",
            "page": "1"
        }

        require = requests.get(url='https://api.themoviedb.org/3/search/movie', params=parameter)
        movies = require.json()['results']
        print(movies)
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)


@app.route("/add_moviename/<id>", methods=["POST", "GET"])
def add_movie(id):
    URL_add = f"https://api.themoviedb.org/3/movie/{id}"
    # https: // api.themoviedb.org / 3 / movie / 593158?api_key = e92e5bd98f3a9abe3d1f02035de8653c & language = en - US
    parameters = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    require = requests.get(url=URL_add, params=parameters)
    movie_info = require.json()
    form = UpdateForm()
    if request.method == "POST" and form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data
        print(movie_info['poster_path'])
        if movie_info['poster_path'] == None:
            img_url = "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YmFubmVyJTIwYmFja2dyb3VuZHxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80"

        else:
            img_url = f"https://image.tmdb.org/t/p/w500/{movie_info['poster_path']}"
        title = movie_info['original_title']
        year = movie_info['release_date'].split("-")[0]
        description = movie_info['overview']
        ranking = 12

        add_new_movie(title, year, description, rating, ranking, review, img_url)
        print(title, year, description, rating, ranking, review, img_url)

        return redirect("/")
    return render_template("add_review_rating.html", movie=movie_info, form=form)


if __name__ == '__main__':
    app.run(debug=True)
