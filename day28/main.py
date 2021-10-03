from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = '#000080'
WHITE = '#FFFFFF'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_count():
    global reps
    timer_head.config(text='Timer', fg=GREEN)
    tickmarks['text'] = ''
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_head['text'] = 'Long Break'
        timer_head.config(fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_head['text'] = 'Break'
        timer_head.config(fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_head['text'] = 'Work'
        timer_head.config(fg=GREEN)

    if reps > 1 and reps % 2 == 0:
        tickmarks['text'] += '✔'


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    min = count // 60
    sec = count % 60
    if len(str(min)) < 2:
        min = f"0{int(min)}"
    if len(str(sec)) < 2:
        sec = f"0{int(sec)}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomadoro')
window.config(padx=100, pady=50, bg=YELLOW)  # bg is for background color

canvas = Canvas(width=204, height=224, bg=YELLOW,
                highlightthickness=0)  # height and width was decideb by pixel size to tomato img

tomato_img = PhotoImage(file='day28/tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

timer_head = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer_head.grid(row=0, column=1)

start = Button(text='Start', width=5, bg=BLUE, fg=WHITE, command=start_count)

start.grid(row=4, column=0)

reset = Button(text='Reset', width=5, bg=BLUE, fg=WHITE, command=reset_count)
reset.grid(row=4, column=2)

tickmarks = Label(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
tickmarks.config(pady=20)
tickmarks.grid(row=4, column=1)

window.mainloop()
