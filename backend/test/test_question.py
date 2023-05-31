# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#          A01745037 Gala Flores García
#          A01752219 Yunoe Sierra Diaz 
# 	       A01720627 Rodrigo Alfredo Mendoza España
#          A01745158 Erika Marlene García Sánchez
#          A01745446 Sergio González
#          A01752114 Antonio Oviedo Paredes

import pytest
from classes.question import Question


"""
This is a test module for the Question class, which tests various methods of the class using a
sample question.

:param sample_question: This is a pytest fixture that returns an instance of the Question class with
the following parameters:
"""
    
@pytest.fixture
def sample_question():
    return Question(1, "What is the capital of France?", "Paris", ["London", "Berlin", "Madrid"])

def test_get_correct_answer(sample_question):
    assert sample_question.get_correct_answer() == "Paris"

def test_get_question(sample_question):
    assert sample_question.get_question() == "What is the capital of France?"

def test_get_wrong_answers(sample_question):
    assert sample_question.get_wrong_answers() == ["London", "Berlin", "Madrid"]

def test_get_question_id(sample_question):
    assert sample_question.get_question_id() == 1
