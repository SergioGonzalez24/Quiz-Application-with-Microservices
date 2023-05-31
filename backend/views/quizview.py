from flask import render_template


def show_question_result(is_correct, correct_answer, is_last_question):
    """
    Returns a fuction to render the answer result template.

    Parameters
    ----------
        is_correct : bool
            Whether the question was answered correctly or not.
        correct_answer : str
            The correct answer of the question.
        is_last_question : bool
            Whether the question is the las of the quiz.

    Returns
    -------
        Function : Renders the answer result template.
    """

    return render_template('answer_result.html',
                           is_correct=is_correct,
                           correct_answer=correct_answer,
                           last_question=is_last_question)


def show_question(first_question, possible_answers, quiz):
    """
    Returns a fuction to render a question of a quiz.

    Parameters
    ----------
        first_question : Question
            The quesition to render.
        possible_answers : List[str]
            Possible answers to render.
        quiz : Quiz
            The quiz which the question belongs to.

    Returns
    -------
        Function : Renders a question of a quiz.
    """

    return render_template('question.html',
                           question=first_question,
                           possible_answers=possible_answers,
                           quiz=quiz)


def select_number_of_questions():
    """
    Returns a fuction to render the section to select the number of questions of the quiz.

    Returns
    -------
        Function : Renders the section to select the number of questions of the quiz.
    """
    return render_template('select_number_of_questions.html')


def show_number_of_questions(num_questions):
    """
    Returns a fuction to render the selected number of questions.

    Parameters
    ----------
        num_questions : int
            Selected number of questions for the quiz.

    Returns
    -------
        Function : Renders a the selected number of questions.
    """

    return render_template('show_number_of_questions.html', num_questions=num_questions)


def show_score(score):
    """
    Returns a fuction to render the score of the quiz.

    Parameters
    ----------
        score -> int
            Final score of the quiz.

    Returns
    -------
        Function : Renders the score of the quiz.
    """

    return render_template('score.html', score=score)


def show_high_scores(scores, user_score):
    """
    Returns a fuction to render the score table.

    Parameters
    ----------
        scores : List[{id: int, place: int, initials: str, score: int}]
            List of high scores objects.
        user_score : {id: int, place: int, initials: str, score: int}
            Object that represents the user score.


    Returns
    -------
        Function : Renders the score table.
    """

    return render_template('high_scores.html', scores=scores, user_score=user_score)
