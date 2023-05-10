class Question:
    def __init__(self, question, correct_answer, wrong_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers

    def get_correct_answer(self):
        return self.correct_answer
