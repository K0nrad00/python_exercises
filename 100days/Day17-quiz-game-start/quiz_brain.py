# from main import question_bank # circular import not allowed

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        # current_question = 0
    ## MY method - # circular import not allowed
    # def next_question(self):
    #     current_question = self.question_list[self.question_number]+1
    #     return input(f"Q.{current_question}: {question_bank[self.question_number].text} (True/False)")

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    ## Her method:
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score +=1
        else:
            print("That is wrong")
            # self.still_has_questions()
        print(f"The correct answer was {correct_answer}, the score: {self.score}/{self.question_number}")
        # print("\n")
