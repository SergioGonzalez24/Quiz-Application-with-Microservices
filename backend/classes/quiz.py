class Quiz:
    """
    Represents a quiz that manages a list of questions and tracks the user's score and progress.

    Attributes
    ----------
        questions : List[Question]
            A list of Question objects representing the questions in the quiz.
        score : int
            The score of the user taking the quiz.
        question_index : int
            The index of the current question.

    Methods
    -------
        get_question() -> Question
            Returns the current question.
        elevate_question_index()
            Increments the question index by 1.
        get_question_number() -> int
            Returns the current question number for display.
        get_question_index() -> int
            Returns the current question index.
        get_num_question() -> int
            Returns the number of questions in the quiz.
        if_finished() -> bool
            Checks if the quiz is finished.
        check_answer(answer) -> bool
            Checks if the inptu answer is correct.
        is_last_question() ->
            Checks if the current question is the last question.
    """

    def __init__(self, questions):
        """
        Constructs all the necessary attributes for the Quiz object.

        Parameters
        ----------
            questions : List[Question]
                A list of Question objects to include in the quiz.
        """
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        """
        Returns the current question.

        Returns
        -------
            Question : Current question.
        """

        return self.questions[self.question_index]

    def elevate_question_index(self):
        """
        Increments the question index by 1.
        """
        self.question_index += 1

    def get_question_number(self):
        """
        Returns the current question number.

        Returns
        -------
            int : Current question number.
        """
        return self.question_index + 1

    def get_question_index(self):
        """
        Returns the current question index.

        Returns
        -------
            int : Current question index.
        """
        return self.question_index

    def get_num_questions(self):
        """
        Returns the number of questions in the quiz.

        Returns
        -------
            int : Quiz length.
        """
        return len(self.questions)

    def is_finished(self):
        """
        Checks if the quiz is finished.

        Returns
        -------
            bool : Whether the quiz is finished or not.
        
        """
        return self.question_index == len(self.questions)

    def check_answer(self, answer):
        """
        Checks if the inptu answer is correct.

        Parameters
        ----------
            answer : str
                The answer to be checked with the actual correct answer.

        Returns
        -------
            bool : Whether the given answer is right or wrong.
        """
        question = self.questions[self.question_index]

        if question.get_correct_answer() == answer:
            self.score += 1

        return question.get_correct_answer() == answer

    def is_last_question(self):
        """
        Checks if the current question is the last question.

        Returns
        -------
            bool : Whether the current question is the last one or not.
        """
        return self.question_index == len(self.questions)
