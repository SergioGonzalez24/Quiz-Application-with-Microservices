class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = -1

    def get_question(self):
        self.question_index += 1
        return self.questions[self.question_index]

    def get_question_index(self):
        return self.question_index + 1

    def get_num_questions(self):
        return len(self.questions)

    def is_finished(self):
        return self.question_index == len(self.questions)

    def check_answer(self, answer):
        question = self.questions[self.question_index]

        if question.get_correct_answer() == answer:
            self.score += 1

        return question.get_correct_answer() == answer
