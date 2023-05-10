import views.quizview as quizview
from flask import request
from models.quizmodel import Scores, Question, QuestionAnswers, db


class Quizcontroller:

    def __init__(self):
        self.num_questions = None

    def index(self):
        return 'hello'

    def add_score(self):
        try:
            # create tables if not exists.
            record = Scores(initials='hola', score=1)
            db.session.add(record)
            db.session.commit()
            return '==================SCORE ADDED=================='

        except Exception as e:
            print(e)
            return '==================SCORE NOT ADDED!!!=================='

    def create_tables(self):
        try:
            # create tables if not exists.
            db.create_all()
            db.session.commit()
            return '==================TABLES CREATED=================='

        except Exception as e:
            print(e)
            return '==================TABLES NOT CREATED!!!=================='

    def show_question_result(self):
        question_id = request.form['question_id']
        correct_answer = QuestionAnswers.query.filter_by(question_id=question_id, is_correct=1).first()
        user_answer = request.form['answer']

        return quizview.is_correct_question(correct_answer, user_answer)

    def show_question(self):
        first_question = Question.query.first()
        possible_answers = QuestionAnswers.query.filter_by(question_id=first_question.id).all()
        return quizview.show_question_result(first_question, possible_answers)

    def select_number_of_questions(self):
        return quizview.select_number_of_questions()

    def show_number_of_questions(self):
        self.num_questions = request.form['num_questions']
        return quizview.show_number_of_questions(self.num_questions)
