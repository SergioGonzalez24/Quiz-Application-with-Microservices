import views.quizview as quizview
from flask import request
from models.quizmodel import Scores, Question, QuestionAnswers, db


def index():
    return {'hello'}


def add_score():
    try:
        # create tables if not exists.
        record = Scores(initials='hola', score=1)
        db.session.add(record)
        db.session.commit()
        return '==================SCORE ADDED=================='

    except Exception as e:
        print(e)
        return '==================SCORE NOT ADDED!!!=================='


def create_tables():
    try:
        # create tables if not exists.
        db.create_all()
        db.session.commit()
        return '==================TABLES CREATED=================='

    except Exception as e:
        print(e)
        return '==================TABLES NOT CREATED!!!=================='


def show_question_result():
    question_id = request.form['question_id']
    correct_answer = QuestionAnswers.query.filter_by(question_id=question_id, is_correct=1).first()
    user_answer = request.form['answer']

    return quizview.is_correct_question(correct_answer, user_answer)


def show_question():
    first_question = Question.query.first()
    possible_answers = QuestionAnswers.query.filter_by(question_id=first_question.id).all()
    return quizview.show_question_result(first_question, possible_answers)