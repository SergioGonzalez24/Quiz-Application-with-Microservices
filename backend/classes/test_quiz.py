import pytest
from quiz import Quiz

@pytest.fixture
def quiz():
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
    # Test the get_question method
    question = quiz.get_question()
    assert isinstance(question, str)

def test_elevate_question_index(quiz):
    # Test the elevate_question_index method
    initial_index = quiz.get_question_index()
    quiz.elevate_question_index()
    new_index = quiz.get_question_index()
    assert new_index == initial_index + 1

def test_get_question_number(quiz):
    # Test the get_question_number method
    question_number = quiz.get_question_number()
    assert isinstance(question_number, int)

def test_get_num_questions(quiz):
    # Test the get_num_questions method
    num_questions = quiz.get_num_questions()
    assert isinstance(num_questions, int)

def test_is_finished(quiz):
    # Test the is_finished method
    finished = quiz.is_finished()
    assert isinstance(finished, bool)


def test_is_last_question(quiz):
    # Test the is_last_question method
    is_last = quiz.is_last_question()
    assert isinstance(is_last, bool)
