from flask import Blueprint
from controllers.quizcontroller import Quizcontroller

quizcontroller = Quizcontroller()

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(quizcontroller.index)
blueprint.route('/add_score', methods=['GET'])(quizcontroller.add_score)
blueprint.route('/create_tables', methods=['GET'])(quizcontroller.create_tables)
blueprint.route('/question', methods=['POST'])(quizcontroller.show_question)
blueprint.route('/question_result', methods=['POST'])(quizcontroller.show_question_result)
blueprint.route('/select_number_of_questions', methods=['GET'])(quizcontroller.select_number_of_questions)
blueprint.route('/show_number_of_questions', methods=['POST'])(quizcontroller.show_number_of_questions)