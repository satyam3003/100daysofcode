from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    posts = db.session.query(BlogPost).get(index)
    return render_template("post.html", post=posts)


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit_blog(id):
    edit_post = BlogPost.query.get(id)
    form = CreatePostForm(title=edit_post.title,
                          subtitle=edit_post.subtitle,
                          img_url=edit_post.img_url,
                          author=edit_post.author,
                          body=edit_post.body)

    if form.validate_on_submit():
        edit_post.title = form.title.data
        edit_post.subtitle = form.subtitle.data
        edit_post.date = datetime.now().strftime("%d %B, %Y")
        edit_post.body = form.body.data
        edit_post.author = form.author.data
        edit_post.img_url = form.img_url.data

        db.session.commit()
        return redirect(f"/post", id = edit_post.id)

    return render_template("make-post.html", form=form, is_edit=True)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
def newpost():
    form = CreatePostForm()
    if form.validate_on_submit() and request.method == "POST":
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=datetime.now().strftime("%d %B, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")

    return render_template("make-post.html", form=form)


@app.route("/deletepost/<int:post_id>", methods=["GET","POST"])
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
