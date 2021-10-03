from flask import Flask, render_template
import datetime
import requests

now = datetime.datetime.now().year
print(now)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", year=now)


@app.route("/guess/<name>")
def guess(name):
    parameters = {
        "name": name
    }
    gender_api = requests.get(url="https://api.genderize.io", params=parameters)
    age_api = requests.get(url="https://api.agify.io", params=parameters)
    gender = gender_api.json()["gender"]
    age = age_api.json()["age"]
    count = age_api.json()["count"]
    return render_template("guess.html", name=name, gender=gender, age=age, count=count)


@app.route("/blog")
def blog_main():
    all_blogs = requests.get("https://api.npoint.io/ed99320662742443cc5b").json()
    print(all_blogs)
    return render_template("blog.html", all_blogs=all_blogs)


@app.route("/blog/<num>")
def blog_post(num):
    all_blogs = requests.get("https://api.npoint.io/ed99320662742443cc5b").json()
    blog = all_blogs[int(num) - 1]
    return render_template("ind_blog.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
