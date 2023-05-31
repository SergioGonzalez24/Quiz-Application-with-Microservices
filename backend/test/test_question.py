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
    """
    The function creates a sample question object with a question, correct answer, and list of incorrect
    answers.
    :return: A function that creates a question object with the following attributes: 
    - ID: 1
    - Question: "What is the capital of France?"
    - Correct answer: "Paris"
    - List of incorrect answers: ["London", "Berlin", "Madrid"]
    """
    return Question(1, "What is the capital of France?", "Paris", ["London", "Berlin", "Madrid"])

def test_get_correct_answer(sample_question):
    """
    This function tests if the method `get_correct_answer()` of an object `sample_question` returns the
    correct answer "Paris".
    
    :param sample_question: Unfortunately, I cannot provide a complete answer without more context. It
    seems that the code snippet is testing a method called `get_correct_answer()` of a class that is not
    shown in the code. The `assert` statement checks if the output of `get_correct_answer()` is equal to
    the string "
    """
    assert sample_question.get_correct_answer() == "Paris"

def test_get_question(sample_question):
    """
    The function tests if the get_question method of a sample_question object returns the expected
    question.
    
    :param sample_question: It is likely that `sample_question` is an instance of a class that
    represents a question, and `get_question()` is a method of that class that returns the actual
    question text. The assertion in the test is checking whether the returned question text matches the
    expected value, which is "What is the
    """
    assert sample_question.get_question() == "What is the capital of France?"

def test_get_wrong_answers(sample_question):
    """
    The function tests if the method `get_wrong_answers()` of an object `sample_question` returns a list
    of wrong answers.
    
    :param sample_question: Unfortunately, I cannot see the definition of the `sample_question` object
    in your code snippet. Can you provide more context or code so I can understand what it is?
    """
    assert sample_question.get_wrong_answers() == ["London", "Berlin", "Madrid"]

    """
    This function tests whether the get_question_id method of a sample_question object returns the
    expected value of 1.
    
    :param sample_question: Unfortunately, as an AI language model, I do not have access to the context
    or the definition of the `sample_question` object. Can you please provide more information about it?
    """
def test_get_question_id(sample_question):
    assert sample_question.get_question_id() == 1
