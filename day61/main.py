from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "abcdEFG"


class MyForm(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired(), validators.length(min=5, message="Too short")])
    email = StringField('email', validators=[validators.DataRequired(), validators.email(message="Invalid email")])
    password = PasswordField('password', validators=[])
    submit = SubmitField(label='Log In')


@app.route("/login", methods=['GET', 'POST'])
def log_in():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if form.name.data == "admin" and form.email.data == 'admin@gmail.com' and form.password.data == "12345":
                print(form.name.data, form.email.data, form.password.data)
                return redirect('/success')
            else:
                return redirect('/denied')
    return render_template('login.html', form=form)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/denied")
def failure():
    return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True)
