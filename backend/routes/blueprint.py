from flask import Blueprint
from controllers.quizcontroller import Quizcontroller

quizcontroller = Quizcontroller()

blueprint = Blueprint('blueprint', __name__)


blueprint.route('/question', methods=['POST', 'GET'])(quizcontroller.show_question)
blueprint.route('/question_result', methods=['POST'])(quizcontroller.show_question_result)
blueprint.route('/', methods=['GET', 'POST'])(quizcontroller.select_number_of_questions)
blueprint.route('/score', methods=['GET'])(quizcontroller.show_score)
blueprint.route('/high_scores', methods=['GET', 'POST'])(quizcontroller.show_high_scores)
