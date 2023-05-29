import views.quizview as quizview
from flask import request
import models.quizmodel as quizmodel
from classes.quiz import Quiz
from classes.question import Question
import random


def get_question_list(questions):
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
    return question_list


def is_user_top_10(user_score):
    top_10_scores = quizmodel.Scores.query.order_by(quizmodel.Scores.score.desc()).limit(10).all()
    user_score_in_top_10 = False
    user_score_dict = None
    if user_score is not None:
        user_place = quizmodel.Scores.query.filter(quizmodel.Scores.score >= user_score.score, quizmodel.Scores.id <
                                                   user_score.id).count()
        user_score_dict = {'id': user_score.id, 'place': user_place, 'initials': user_score.initials,
                           'score': user_score.score}
        if user_score in top_10_scores:
            user_score_in_top_10 = True
    return top_10_scores, user_place, user_score_dict, user_score_in_top_10


class QuizController:

    def __init__(self):
        self.num_questions = None
        self.quiz = None

    def select_number_of_questions(self):
        # method to be used in the quiz view to select the number of questions (home page)
        self.quiz = None
        return quizview.select_number_of_questions()

    def show_question_result(self):
        # method to be used in the quiz view to show the result of the user's answer
        user_answer = request.form['answer']
        is_correct = self.quiz.check_answer(user_answer)
        correct_answer = self.quiz.get_question().get_correct_answer()
        self.quiz.elevate_question_index()

        return quizview.show_question_result(is_correct, correct_answer, self.quiz.is_last_question())

    def show_question(self):
        # method to be used in the quiz view to show the question and possible answers
        if self.quiz is None:
            self.num_questions = int(request.form['num_questions'])
            self.initialize_quiz()
        question = self.quiz.get_question()
        possible_answers = quizmodel.QuestionAnswers.query.filter_by(question_id=question.get_question_id()).all()
        return quizview.show_question(question, possible_answers, self.quiz)

    def initialize_quiz(self):
        # get a random set of questions depending on how many questions the user wants
        lowest_id = quizmodel.Question.query.order_by(quizmodel.Question.id).first().id
        highest_id = quizmodel.Question.query.order_by(quizmodel.Question.id.desc()).first().id
        random_ids = random.sample(range(lowest_id, highest_id + 1), self.num_questions)
        questions = quizmodel.Question.query.filter(quizmodel.Question.id.in_(random_ids)).all()
        question_list = get_question_list(questions)
        self.quiz = Quiz(question_list)

    def show_score(self):
        return quizview.show_score(self.quiz.score)

    def show_high_scores(self):
        # method to be used in the quiz view to show the high scores
        user_score = None
        if request.method == 'POST':
            self._add_score_to_db()
            user_score = quizmodel.Scores.query.order_by(quizmodel.Scores.id.desc()).first()

        top_10_scores, user_place, user_score_dict, user_score_in_top_10 = is_user_top_10(user_score)

        score_list = []
        counter = 0
        for score in top_10_scores:
            counter += 1
            score_list.append({'id': score.id, 'place': counter, 'initials': score.initials, 'score': score.score})
        if user_score_in_top_10 is False and user_score is not None:
            score_list.append(
                {'id': user_score.id, 'place': user_place, 'initials': user_score.initials, 'score': user_score.score})

        return quizview.show_high_scores(score_list, user_score_dict)

    def _add_score_to_db(self):
        initials = request.form['initials']
        score = self.quiz.score
        record = quizmodel.Scores(initials=initials, score=score)
        quizmodel.db.session.add(record)
        quizmodel.db.session.commit()
