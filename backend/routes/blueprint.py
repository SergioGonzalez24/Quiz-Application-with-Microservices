from flask import Blueprint
from controllers.quizcontroller import index, create_tables, add_score, \
    show_question, show_question_result

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/add_score', methods=['GET'])(add_score)
blueprint.route('/create_tables', methods=['GET'])(create_tables)
blueprint.route('/question', methods=['GET'])(show_question)
blueprint.route('/question_result', methods=['POST'])(show_question_result)