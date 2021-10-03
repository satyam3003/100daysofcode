class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_have_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q. {self.question_no}: {current_question.text} (True/False)? ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"Thats wrong! \tCorrect answer is: {correct_answer.lower()}")
        print(f"Scores: {self.score} / {self.question_no} \n")
