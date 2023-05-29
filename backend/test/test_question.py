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