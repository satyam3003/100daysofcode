from flask import Flask, render_template, request
import requests
import smtplib

my_email = ''
password = ''
app = Flask(__name__)


@app.route("/")
def home_page():
    all_blogs = requests.get("https://api.npoint.io/e42b353ee387383898c7").json()
    print(all_blogs)
    return render_template("index.html", all_blogs=all_blogs)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone_no = data["phoneno"]
        message = data["message"]

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='baldawasatyam30@gmail.com',
                                msg=f'Subject: New message from BLOG! \n\nNAME: {name}\nEMAIL ID: {email}\nPHONE NO: {phone_no}\nMESSAGE :{message}')  # Subject:--- to add subject ---- \n\n to indicate subject is over and further add content
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<num>")
def post(num):
    blog = requests.get("https://api.npoint.io/e42b353ee387383898c7").json()[int(num) - 1]
    return render_template("post.html", blog=blog, img=blog['image'])


# @app.route("/login", methods=["POST","GET"])
# def login_info():
#     print(request.method)
#     name = request.form['name']
#     email = request.form['email']
#     phone_no = request.form['phoneno']
#     message = request.form['message']
#     return f"<h1>Message send successfully!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
