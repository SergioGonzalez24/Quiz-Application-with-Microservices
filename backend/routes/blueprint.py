# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#          A01745037 Gala Flores García
#          A01752219 Yunoe Sierra Diaz 
# 	       A01720627 Rodrigo Alfredo Mendoza España
#          A01745158 Erika Marlene García Sánchez
#          A01745446 Sergio González
#          A01752114 Antonio Oviedo Paredes

from flask import Blueprint
from controllers.quizcontroller import QuizController

quizcontroller = QuizController()

blueprint = Blueprint('blueprint', __name__)


blueprint.route('/question', methods=['POST', 'GET'])(quizcontroller.show_question)
blueprint.route('/question_result', methods=['POST'])(quizcontroller.show_question_result)
blueprint.route('/', methods=['GET', 'POST'])(quizcontroller.select_number_of_questions)
blueprint.route('/score', methods=['GET'])(quizcontroller.show_score)
blueprint.route('/high_scores', methods=['GET', 'POST'])(quizcontroller.show_high_scores)
