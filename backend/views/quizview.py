from flask import render_template


def is_correct_question(correct_answer, user_answer):

    if user_answer == correct_answer.answer:
        is_correct = True
    else:
        is_correct = False

    # Render the answer result template
    return render_template('answer_result.html', is_correct=is_correct, correct_answer=correct_answer)


def show_question_result(first_question, possible_answers, quiz):

    return render_template('question.html', question=first_question, possible_answers=possible_answers, quiz=quiz)


def select_number_of_questions():

    return render_template('select_number_of_questions.html')


def show_number_of_questions(num_questions):

        return render_template('show_number_of_questions.html', num_questions=num_questions)