# test_quizmodel.py

# test_quizmodel.py

import pytest
from app import create_app, db
from models.quizmodel import Question

@pytest.fixture(scope='module')
def app():
    app = create_app()  # Replace with your Flask application creation code
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory SQLite database for testing
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def new_question(app):
    with app.app_context():
        question = Question(question='Sample question')
        db.session.add(question)
        db.session.commit()
        yield question
        db.session.delete(question)
        db.session.commit()

def test_question_creation(new_question):
    assert new_question.id is not None
    assert new_question.question == 'Sample question'

def test_question_representation(new_question):
    assert repr(new_question) == f'<Question {new_question.id}>'
