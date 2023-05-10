import views.quizview as quizview
from flask import request
import models.quizmodel as quizmodel
from classes.quiz import Quiz
from classes.question import Question
import random


class Quizcontroller:

    def __init__(self):
        self.num_questions = None
        self.quiz = None

    """def index(self):
        return 'hello'

    def add_score(self):
        try:
            # create tables if not exists.
            record = quizmodel.Scores(initials='hola', score=1)
            quizmodel.db.session.add(record)
            quizmodel.db.session.commit()
            return '==================SCORE ADDED=================='

        except Exception as e:
            print(e)
            return '==================SCORE NOT ADDED!!!=================='

    def create_tables(self):
        try:
            # create tables if not exists.
            quizmodel.db.create_all()
            quizmodel.db.session.commit()
            return '==================TABLES CREATED=================='

        except Exception as e:
            print(e)
            return '==================TABLES NOT CREATED!!!=================='"""

    def show_question_result(self):
        question_id = request.form['question_id']
        correct_answer = quizmodel.QuestionAnswers.query.filter_by(question_id=question_id, is_correct=1).first()
        user_answer = request.form['answer']

        return quizview.is_correct_question(correct_answer, user_answer)

    def show_question(self):
        if self.quiz is None:
            self.num_questions = int(request.form['num_questions'])
            self.initialize_quiz()
        question = self.quiz.get_question()
        possible_answers = quizmodel.QuestionAnswers.query.filter_by(question_id=question.get_question_id()).all()
        return quizview.show_question_result(question, possible_answers, self.quiz)

    def select_number_of_questions(self):
        return quizview.select_number_of_questions()

    def show_number_of_questions(self):
        self.num_questions = request.form['num_questions']
        return quizview.show_number_of_questions(self.num_questions)

    def initialize_quiz(self):
        # a list of 10 random questions
        lowest_id = quizmodel.Question.query.order_by(quizmodel.Question.id).first().id
        highest_id = quizmodel.Question.query.order_by(quizmodel.Question.id.desc()).first().id
        random_ids = random.sample(range(lowest_id, highest_id+1), self.num_questions)
        questions = quizmodel.Question.query.filter(quizmodel.Question.id.in_(random_ids)).all()
        question_list = []
        for question in questions:
            question_id = question.id
            right_answer = quizmodel.QuestionAnswers.query.filter_by(question_id=question.id, is_correct=1).first()
            wrong_answers = quizmodel.QuestionAnswers.query.filter_by(question_id=question.id, is_correct=0).all()
            wrong_answers_list = []
            for wrong_answer in wrong_answers:
                wrong_answers_list.append(wrong_answer.answer)
            question = Question(question_id, question.question, right_answer.answer, wrong_answers_list)
            question_list.append(question)
        self.quiz = Quiz(question_list)

    def test_page(self):
        self.num_questions = 10
        self.initialize_quiz()
        pretty_quiz_questions = []
        for question in self.quiz.questions:
            pretty_question = {
                'question': question.get_question(),
                'right_answer': question.get_correct_answer(),
                'wrong_answers': question.get_wrong_answers()
            }
            pretty_quiz_questions.append(pretty_question)

        print(pretty_quiz_questions)
        return pretty_quiz_questions

