# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#          A01745037 Gala Flores García
#          A01752219 Yunoe Sierra Diaz 
# 	       A01720627 Rodrigo Alfredo Mendoza España
#          A01745158 Erika Marlene García Sánchez
#          A01745446 Sergio González
#          A01752114 Antonio Oviedo Paredes

class Question:
    """
    A class used to represent a question with its ID, question content, 
    correct answer, and wrong answers.

    Attributes
    ----------
        question_id : int
            The unique ID of the question.
        question : str
            The content of the question.
        correct_answer : str
            The correct answer of the question.
        wrong_answers : List[str]
            A list of wrong answers for the question.

    Methods
    -------
        get_correct_answer() -> str
            Returns the correct answer of the question.
        get_question() -> str
            Returns the content of the question.
        get_wrong_answers() -> List[str]
            Returns a list that contains the wrong answers for the question.
        get_question_id() -> int
            Returns the unique ID of the question.
    """

    def __init__(self, question_id, question, correct_answer, wrong_answers):
        """
        Constructs all the necessary attributes for the question object.

        Parameters
        ----------
            question_id : int
                Unique ID of the question.
            question : str
                Question content.
            correct_answer : str
                Correct answer of the question.
            wrong_answer : List[str]
                List of wrong answers for the question.
        """
        self.question_id = question_id
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers

    def get_correct_answer(self):
        """
        Retrieves the correct answer of the question.

        Returns
        -------
            str : Correct answer of the cuestion.
        """
        return self.correct_answer

    def get_question(self):
        """
        Retrieves the content of the question.

        Returns
        -------
            str : Content of the question.
        """
        return self.question

    def get_wrong_answers(self):
        """
        Retrieves the wrong answers for the question.

        Returns
        -------
            List[str] : List of wrong answers.
        """
        return self.wrong_answers

    def get_question_id(self):
        """
        Retrieves the ID of the question.

        Returns
        -------
            int : Unique ID of the question.
        """
        return self.question_id
