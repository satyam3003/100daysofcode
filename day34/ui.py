THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
import time


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.initial_score = 0
        self.window = Tk()
        self.window.title('Quizify')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # --------------- Score card -----------
        self.score = Label(text="Scores: 0", bg=THEME_COLOR, fg='white')
        self.score.grid(row=0, column=1)

        # -------------- Canvas -----------------
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text='Question.....', width=250,
                                                     font=('Arial', 20, 'italic'),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # ---------------- Buttons ------------------
        true_image = PhotoImage(file='day34/images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.button_true)
        self.true_button.grid(row=3, column=0)

        false_image = PhotoImage(file='day34/images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.button_false)
        self.false_button.grid(row=3, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"Congratulations!\nYou have completed the quiz\nFinal Score: {self.initial_score} / 10")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def button_true(self):
        check_right = self.quiz.check_answer('True')
        if check_right:
            self.score_record()
        self.indicator_light(check_right)

    def button_false(self):
        check_right = self.quiz.check_answer('False')
        if check_right:
            self.score_record()
        self.indicator_light(check_right)

    def score_record(self):
        self.initial_score += 1
        self.score['text'] = f"Score: {self.initial_score}"

    def indicator_light(self, signal):
        if signal:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
