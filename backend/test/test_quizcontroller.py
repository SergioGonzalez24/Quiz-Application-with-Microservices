# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#          A01745037 Gala Flores García
#          A01752219 Yunoe Sierra Diaz 
# 	       A01720627 Rodrigo Alfredo Mendoza España
#          A01745158 Erika Marlene García Sánchez
#          A01745446 Sergio González
#          A01752114 Antonio Oviedo Paredes

# The TestQuizController class contains unit tests for the QuizController class.
from classes.question import Question
from controllers.quizcontroller import QuizController
from classes.quiz import Quiz

# The TestQuizController class contains unit tests for the select_number_of_questions and show_score
# methods of the QuizController class.

class TestQuizController:
    
    # Tests that the select_number_of_questions method returns the expected template.
    def test_select_number_of_questions(self, mocker):
        """
        This is a unit test for the select_number_of_questions function in the QuizController class.
        
        :param mocker: mocker is a library used for mocking and patching in Python unit tests. It allows
        you to replace parts of your code with mock objects, which can be useful for testing code that
        interacts with external systems or dependencies
        """
        mocker.patch('views.quizview.select_number_of_questions', return_value='select_number_of_questions.html')
        quiz_controller = QuizController()
        result = quiz_controller.select_number_of_questions()
        assert result == 'select_number_of_questions.html'

    # Tests that the select_number_of_questions method handles the edge case of selecting 0 questions.
    def test_select_number_of_questions_zero(self, mocker):
        """
        This is a unit test for the select_number_of_questions method of the QuizController class in
        Python.
        
        :param mocker: a library used for mocking objects and functions in unit tests
        """
        mocker.patch('views.quizview.select_number_of_questions', return_value='select_number_of_questions.html')
        quiz_controller = QuizController()
        quiz_controller.num_questions = 0
        result = quiz_controller.select_number_of_questions()
        assert result == 'select_number_of_questions.html'

    # Tests that the select_number_of_questions method handles the edge case of selecting a negative number of questions.
    def test_select_number_of_questions_negative(self, mocker):
        """
        This is a unit test function that tests the select_number_of_questions method of the
        QuizController class when the number of questions is negative.
        
        :param mocker: mocker is a library used for mocking and patching in Python unit tests. It allows
        you to replace parts of your code with mock objects, which can be useful for testing code that
        interacts with external systems or dependencies
        """
        mocker.patch('views.quizview.select_number_of_questions', return_value='select_number_of_questions.html')
        quiz_controller = QuizController()
        quiz_controller.num_questions = -1
        result = quiz_controller.select_number_of_questions()
        assert result == 'select_number_of_questions.html'


    # Tests that the show_score method returns the expected template and data.
    def test_show_score(self, mocker):
        """
        This is a unit test for the `show_score` function in a `QuizController` class that checks if the
        function returns the expected value.
        
        :param mocker: mocker is a library used for mocking and patching in Python unit tests. It allows you
        to replace parts of your code with mock objects, which can be useful for testing code that interacts
        with external systems or dependencies
        """
        mocker.patch('views.quizview.show_score', return_value='score.html')
        quiz_controller = QuizController()
        quiz_controller.quiz = Quiz([Question(question_id=1, question='What is 1+1?', correct_answer='2', wrong_answers=['3', '4'])])
        quiz_controller.quiz.score = 1
        result = quiz_controller.show_score()
        assert result == 'score.html'

