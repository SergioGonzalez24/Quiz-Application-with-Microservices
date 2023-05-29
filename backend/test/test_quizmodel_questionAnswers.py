from models.quizmodel import QuestionAnswers

"""
Code Analysis

Main functionalities:
The QuestionAnswers class is used to represent the answers to a question in a quiz or survey. It is related to the Question class through a foreign key, allowing for easy retrieval of all answers associated with a particular question. The class stores the answer text and a boolean value indicating whether it is the correct answer or not.

Methods:
- __repr__: returns a string representation of the object, including its id.
- None

Fields:
- id: an auto-incrementing integer primary key for the answer.
- question_id: a foreign key referencing the id of the associated question.
- answer: a string field storing the text of the answer.
- is_correct: a boolean field indicating whether the answer is the correct one for the associated question.
"""

class TestQuestionAnswers:
    # Tests that a QuestionAnswers object can be created with valid inputs.
    def test_create_question_answers_valid_input(self, mocker):
        # Arrange
        question_mock = mocker.Mock()
        question_mock.id = 1
        answer = "This is a valid answer"
        is_correct = True
        question_answer = QuestionAnswers(question_id=question_mock.id, answer=answer, is_correct=is_correct)

        # Act
        result = str(question_answer)

        # Assert
        assert result == f'<QuestionAnswers {question_answer.id}>'