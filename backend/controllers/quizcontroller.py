# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#          A01745037 Gala Flores García
#          A01752219 Yunoe Sierra Diaz 
# 	       A01720627 Rodrigo Alfredo Mendoza España
#          A01745158 Erika Marlene García Sánchez
#          A01745446 Sergio González
#          A01752114 Antonio Oviedo Paredes

import random
import views.quizview as quizview
from flask import request
import models.quizmodel as quizmodel
from classes.quiz import Quiz
from classes.question import Question


def get_question_list(questions):
    """
    Retrieves a list of formatted questions.

    Parameters
    ----------
    questions : List[Question]
        A list of question objects.

    Returns
    -------
    List[Question] : A list of Question instances containing the formatted questions.
    """
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
    """
    Checks if the user's score is among the top 10 scores.

    Parameters
    ----------
    user_score : dict
        The user's score object.

    Returns
    -------
        top_10_scores : dict 
            Top 10 scores in the database.
        user_place : int
            User palace in the score table.
        user_score_dict : dict
            User score table information.
        user_score_in_top_10 : bool
            Whether the user score is placed in the top 10.
    """
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
    """
    Quiz Controller class that makes the connection between the view and the model.

    Attributes
    ---------
        num_questions : int
            Number of quiestions of the quiz.
        quiz : Quiz
            A Quiz instance

    Methods
    -------
        select_number_of_question() -> Function
            Returns a function that displays and handles the functionality for selecting the number of questions.
        show_question_result() -> Function
            Returns a function that displays the result of the user's answer.
        show_question() -> Function
            Returns a function used to displays a question and possible answers.
        initialize_quiz()
            Initialize all the quiz information.
        show_score() -> Function
            Returns a function that displays the user's score.
        show_high_score() -> Function
            Returns a function that displays the score table.
        _add_score_to_db()
            Adds a new score to the database.
    """

    def __init__(self):
        """
        Parameters initialization.
        """
        self.num_questions = None
        self.quiz = None

    def select_number_of_questions(self):
        """
        Method to be used in the quiz view to select the number of questions (home page).

        Returns
        -------
            Function : Displays and handles the functionality for selecting the number of questions.
        """
        self.quiz = None
        return quizview.select_number_of_questions()

    def show_question_result(self):
        """
        Method to be used in the quiz view to show the result of the user's answer.

        Returns
        -------
            Function : Displays the result of the user's answer.
        """

        user_answer = request.form['answer']
        is_correct = self.quiz.check_answer(user_answer)
        correct_answer = self.quiz.get_question().get_correct_answer()
        self.quiz.elevate_question_index()

        return quizview.show_question_result(is_correct, correct_answer, self.quiz.is_last_question())

    def show_question(self):
        """
        Method to be used in the quiz view to show the question and possible answers.

        Returns
        -------
            Function : Displays a question and possible answers.
        """

        if self.quiz is None:
            self.num_questions = int(request.form['num_questions'])
            self.initialize_quiz()
        question = self.quiz.get_question()
        possible_answers = quizmodel.QuestionAnswers.query.filter_by(question_id=question.get_question_id()).all()
        return quizview.show_question(question, possible_answers, self.quiz)

    def initialize_quiz(self):
        """
        Initialize the quiz with a random set of questions depending on how many questions the user wants.
        """
        
        lowest_id = quizmodel.Question.query.order_by(quizmodel.Question.id).first().id
        highest_id = quizmodel.Question.query.order_by(quizmodel.Question.id.desc()).first().id
        random_ids = random.sample(range(lowest_id, highest_id + 1), self.num_questions)
        questions = quizmodel.Question.query.filter(quizmodel.Question.id.in_(random_ids)).all()
        question_list = get_question_list(questions)
        self.quiz = Quiz(question_list)

    def show_score(self):
        """
        Method to be used in the quiz view to show the user's score.

        Returns
        -------
            Function : Displays the user's score.
        """
        return quizview.show_score(self.quiz.score)

    def show_high_scores(self):
        """
        Method to be used in the quiz view to show the high scores.

        Returns
        -------
            Function : Displays the score tamble.
        """

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
        """
        Adds a new score to the database.
        """
        initials = request.form['initials']
        score = self.quiz.score
        record = quizmodel.Scores(initials=initials, score=score)
        quizmodel.db.session.add(record)
        quizmodel.db.session.commit()
