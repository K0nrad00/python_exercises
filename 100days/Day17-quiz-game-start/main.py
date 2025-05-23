from question_model import Question
from data import  question_data
from quiz_brain import QuizBrain

question_bank = []

for row in question_data:
    # print(row)
    question_text = Question(q_text=row["text"], q_answer=row["answer"])
    # question_bank.append(row["text"], row["answer"])
    question_bank.append(question_text)

# print(question_bank[0].text, question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    print("\n")
    quiz.next_question()
    # quiz.check_answer()

print("That's all the questions!")
print(f"The final score is:  {quiz.score}/{len(question_bank)}")

# https://opentdb.com/