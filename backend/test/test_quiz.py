import pytest
from classes.quiz import Quiz

"""
This is a test suite for a Quiz class that tests various methods such as get_question,
elevate_question_index, get_question_number, get_num_questions, is_finished, and is_last_question.

:param quiz: The `quiz` fixture is a function that returns an instance of the `Quiz` class, which
takes a list of questions as an argument. The questions are defined within the fixture. The fixture
is used in each of the test functions to create an instance of the `Quiz` class to test its
"""

@pytest.fixture
def quiz():
    """
    This function defines a list of questions and returns a Quiz object containing those questions.
    :return: A Quiz object with a list of questions.
    """
    questions = [
        # Define your questions here
        'Who wrote the Roman poem "Metamorphoses"?',
        'Which of these artists was known for their Impressionist style?',
        'What is the chemical formula for hydrochloric acid?',
        'What organ is responsible for producing insulin?',
        'What number is equivalent to 16 in hexadecimal?',
        'What substrate does the brain primarily feed on?',
        'Which virus was targeted by the first vaccine?',
        'What does a seismograph record?',
        'How tall was the tallest man in the world (credited)?',
        'By what other name is the skin known?',
        'How many legs do spiders have?',
        'In what state is uranium at room temperature?',
        'What is the symbol for potassium?',
        'Which of the following is a noble gas?',
        'What is the chemical symbol for iron?',
        'Who formulated the theory of general relativity?',
        'What is the sternocleidomastoid?',
        'How is the chemical compound H2O2 commonly known?',
        "Which part of the body does Crohn's disease affect?",
        'What are the lesions on the wall of the digestive tube called?',
        'What is keratin?',
        'What do the initials "www" stand for?',
        'What is cholesterol?',
        'Where are jellyfish with deadly venom found?',
        'What are axons a part of?',
        'Which of the following is not a blood group?',
        'How many Laws of Mendel are there?',
        'Who painted "The Mona Lisa"?',
        'What material was the beetle in Edgar Allan Poe story made of?',
        "In which city is Michelangelo's David located?"
        
    ]
    return Quiz(questions)

def test_get_question(quiz):
    """
    The function tests the get_question method of a quiz object to ensure it returns a string.
    
    :param quiz: The parameter "quiz" is likely an instance of a Quiz class, which contains a list of
    questions and answers, as well as methods for retrieving and checking answers. The test_get_question
    function is testing the get_question method of the Quiz class, which should return a string
    representing a question from the quiz
    """
    # Test the get_question method
    question = quiz.get_question()
    assert isinstance(question, str)

    """
    This function tests the elevate_question_index method of a quiz object by checking if the new index
    is incremented by one.
    
    :param quiz: The "quiz" parameter is likely an instance of a class that represents a quiz or a set
    of questions. The class probably has methods such as "get_question_index" and
    "elevate_question_index" that allow the user to navigate through the questions in the quiz. The
    purpose of the "
    """
def test_elevate_question_index(quiz):
    """
    This function tests the elevate_question_index method of a quiz object by checking if the new index
    is incremented by one.
    
    :param quiz: The "quiz" parameter is likely an instance of a class that represents a quiz or a set
    of questions. The class probably has methods such as "get_question_index" and
    "elevate_question_index" that allow the user to navigate through the questions in the quiz. The
    purpose of the "
    """
    # Test the elevate_question_index method
    initial_index = quiz.get_question_index()
    quiz.elevate_question_index()
    new_index = quiz.get_question_index()
    assert new_index == initial_index + 1

def test_get_question_number(quiz):
    """
    This function tests the get_question_number method of a quiz object to ensure it returns an integer.
    
    :param quiz: The parameter "quiz" is likely an instance of a Quiz class, which has a method called
    "get_question_number". This test is checking if the method returns an integer value
    """
    # Test the get_question_number method
    question_number = quiz.get_question_number()
    assert isinstance(question_number, int)

def test_get_num_questions(quiz):
    """
    This function tests the get_num_questions method of a quiz object to ensure it returns an integer.
    
    :param quiz: The parameter "quiz" is likely an instance of a class that represents a quiz. The test
    is checking the "get_num_questions" method of this class, which should return the number of
    questions in the quiz as an integer. The test then checks that the returned value is indeed an
    integer using the
    """
    # Test the get_num_questions method
    num_questions = quiz.get_num_questions()
    assert isinstance(num_questions, int)

def test_is_finished(quiz):
    """
    This function tests the is_finished method of a quiz object and checks if it returns a boolean
    value.
    
    :param quiz: The parameter "quiz" is likely an instance of a class that represents a quiz. The
    method being tested, "is_finished()", is probably a method of this class that checks whether the
    quiz has been completed or not. The test is checking whether the method returns a boolean value
    (True or False)
    """
    # Test the is_finished method
    finished = quiz.is_finished()
    assert isinstance(finished, bool)


def test_is_last_question(quiz):
    """
    The function tests the is_last_question method of a quiz object and checks if it returns a boolean
    value.
    
    :param quiz: The parameter "quiz" is likely an instance of a Quiz class or object, which has a
    method called "is_last_question". This test function is testing the functionality of that method by
    checking if it returns a boolean value
    """
    # Test the is_last_question method
    is_last = quiz.is_last_question()
    assert isinstance(is_last, bool)
