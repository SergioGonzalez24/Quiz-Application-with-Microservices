import pytest
from question import Question

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
