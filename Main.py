from data import question_data
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def quiz_questions(self):
        print(self.text)

    def quiz_check(self,user_answer):
        return user_answer == self.answer.lower()
score = 0
for i in range(len(question_data)):
    question = Question(question_data[i]["text"], question_data[i]["answer"])
    question.quiz_questions()
    user_answer = input("Enter your answer for the question: True/False: ").lower()
    print()
    if question.quiz_check(user_answer):
        score +=1

print(f"Your score is {score}")