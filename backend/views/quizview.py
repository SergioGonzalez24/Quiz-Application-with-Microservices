from flask import render_template


def is_correct_question(correct_answer, user_answer):

    if user_answer == correct_answer.answer:
        is_correct = True
    else:
        is_correct = False

    # Render the answer result template
    return render_template('answer_result.html', is_correct=is_correct, correct_answer=correct_answer)


def show_question_result(first_question, possible_answers):

    return render_template('question.html', question=first_question, possible_answers=possible_answers)