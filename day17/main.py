# # ------------ Making Classes and using attributes and methods --------------
#
# class Users: #making class Users
#     def __init__(self,user_id,name):  #initializing class , self necessary
#         self.id = user_id    # these 4 are attributes
#         self.name = name
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):   # this is a method
#         user.followers += 1
#         self.following += 1
#
#     def unfollow(self, user):  # this is a method
#         user.followers -= 1
#         self.following -= 1
#
#
# user1 = Users(5, 'Satyam')   # making an object using class these 2 attributes a re compulsory to add as we made it in init
# user2 = Users(2, 'Smritu')
# print(user1, user1.name, user1.id)
# user1.follow(user2)  # this is the method which we are using to follow
# print(f"name: {user1.name} following: {user1.following}, followers: {user1.followers}")
# print(f"name: {user2.name} following: {user2.following}, followers: {user2.followers}")


# ----------------------- Q and A game ----------------------
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    q_text = item['question']
    q_ans =  item['correct_answer']
    question_bank.append(Question(q_text,q_ans))

quiz = QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()
print(f"You have completed the Quiz!\nYour final score is {quiz.score} of {quiz.question_no}")


