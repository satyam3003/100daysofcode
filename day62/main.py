from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators
from flask_wtf.html5 import URLField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('location', validators=[DataRequired(), validators.url(message="Not a valid url")])
    open_time = StringField('open time ', validators=[DataRequired()])
    close_time = StringField('close time', validators=[DataRequired()])
    coffee_rate = SelectField('coffee rating',
                              choices=[('✘', '✘'), ('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'),
                                       ('☕☕☕☕☕', '☕☕☕☕☕')])
    wifi_rate = SelectField('wifi rating (1-5)',
                            choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'),
                                     ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')])
    power_rate = SelectField('power rating (1-5)',
                             choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),
                                      ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit() and request.method == "POST":
        print("True")
        with open('day62/cafe-data.csv', encoding='utf8', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            cafe = form.cafe.data
            location = form.location.data
            open_time = form.open_time.data
            close_time = form.close_time.data
            coffee_rating = form.coffee_rate.data
            wifi_rating = form.wifi_rate.data
            power = form.power_rate.data
            row = [cafe, location, open_time, close_time, coffee_rating, wifi_rating, power]
            writer.writerow(row)
        return redirect('/cafes')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('day62/cafe-data.csv', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file)
        list_of_rows = []
        for row in csv_data:
            if len(row) != 0:
                list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, len=len(list_of_rows))


if __name__ == '__main__':
    app.run(debug=True)
