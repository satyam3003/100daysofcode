from flask import Flask
import random

app = Flask(__name__)
print(__name__)


class RandomNumberPicker:
    def __init__(self):
        self.number = random.randint(1, 9)


number_random = RandomNumberPicker()
print(number_random.number)

@app.route("/")
def start_screen():
    return '<h1>Choose a number between 1 to 9</h1>' \
           '<img src="https://media.giphy.com/media/QvBoMEcQ7DQXK/giphy.gif?cid=ecf05e47kbja3lbltyirxlhtgfr651auwz987yfprm6pdmbe&rid=giphy.gif&ct=g" alt="" width="400">'


@app.route("/<int:numb>")
def choice_screen(numb):
    if numb == number_random.number:
        return '<h1>Correct Choice</h1>' \
               '<img src=" https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="" width="400">'

    elif numb > number_random.number:
        return '<h1>Too High</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="" width="400">'

    else:
        return '<h1>Too Low</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="" width="400">'


if __name__ == "__main__":
    app.run(debug=True)
