# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#          A01745037 Gala Flores García
#          A01752219 Yunoe Sierra Diaz 
# 	       A01720627 Rodrigo Alfredo Mendoza España
#          A01745158 Erika Marlene García Sánchez
#          A01745446 Sergio González
#          A01752114 Antonio Oviedo Paredes

# test_quizmodel.py
"""
This is a test file for the quizmodel module, which tests the creation and representation of a
Question object using pytest fixtures.

:param new_question: This is a pytest fixture that creates a new instance of the Question model and
adds it to the in-memory SQLite database for testing. The fixture yields the created question object
for use in the tests, and then deletes it from the database after the tests are complete
"""

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
