class Question:
    def __init__(self, question_id, question, correct_answer, wrong_answers):
        self.question_id = question_id
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers

    def get_correct_answer(self):
        return self.correct_answer

    def get_question(self):
        return self.question

    def get_wrong_answers(self):
        return self.wrong_answers

    def get_question_id(self):
        return self.question_id
