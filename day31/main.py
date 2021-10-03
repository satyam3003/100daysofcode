from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
new_french_word = None

# --------------------------- reading csv -------------------------
try:
    data = pd.read_csv('day31/data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('day31/data/french_words.csv')

french_list = data.French.to_list()
eng_fr_dict = {row.French: row.English for (index, row) in data.iterrows()}
print(len(french_list), len(eng_fr_dict))


# ---------------------------- commands -----------------------
def right_command():
    global new_french_word, flip_timer
    window.after_cancel(flip_timer)
    french_list.remove(new_french_word)
    eng_fr_dict.pop(new_french_word)
    new_french_word = random.choice(french_list)
    canvas.itemconfig(word_text, text=new_french_word, fill='#000')
    canvas.itemconfig(title_text, text='French', fill='#000')
    canvas.itemconfig(canvas_img, image=card_front)
    flip_timer = window.after(3000, flip_card)


def wrong_command():
    global new_french_word, flip_timer
    new_french_word = random.choice(french_list)
    canvas.itemconfig(word_text, text=new_french_word, fill='#000')
    canvas.itemconfig(title_text, text='French', fill='#000')
    canvas.itemconfig(canvas_img, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global new_french_word
    canvas.itemconfig(title_text, text='English', fill='#FFFFFF')
    canvas.itemconfig(word_text, text=eng_fr_dict[new_french_word], fill='#FFFFFF')
    canvas.itemconfig(canvas_img, image=card_back)


# --------------------------- UI ----------------------------------
window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=540, bg=BACKGROUND_COLOR,
                highlightthickness=0)
card_front = PhotoImage(file='day31/images/card_front.png')
card_back = PhotoImage(file='day31/images/card_back.png')
canvas_img = canvas.create_image(400, 269, image=card_front)
title_text = canvas.create_text(400, 150, text='Title', font=('arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='Word', font=('arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_mark = PhotoImage(file='day31/images/wrong.png')
wrong_button = Button(image=wrong_mark, bg=BACKGROUND_COLOR, highlightthickness=0, padx=50, pady=10,
                      command=wrong_command)
wrong_button.grid(row=1, column=0)

tick_mark = PhotoImage(file='day31/images/right.png')
tick_button = Button(image=tick_mark, bg=BACKGROUND_COLOR, highlightthickness=0, padx=50, pady=10,
                     command=right_command)
tick_button.grid(row=1, column=1)

wrong_command()
window.mainloop()

print(len(french_list), len(eng_fr_dict))
english_list = [eng_fr_dict[item] for item in french_list]
print(french_list, english_list)

unanswered_dict = {
    'French': french_list,
    'English': english_list
}
df = pd.DataFrame(unanswered_dict)
print(df)

df.to_csv('day31/data/words_to_learn.csv')
