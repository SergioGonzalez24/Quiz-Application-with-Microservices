from flask import render_template


def show_question_result(is_correct, correct_answer, is_last_question):
    # Render the answer result template
    return render_template('answer_result.html', is_correct=is_correct, correct_answer=correct_answer,
                           last_question=is_last_question)


def show_question(first_question, possible_answers, quiz):
    return render_template('question.html', question=first_question, possible_answers=possible_answers, quiz=quiz)


def select_number_of_questions():
    return render_template('select_number_of_questions.html')


def show_number_of_questions(num_questions):
    return render_template('show_number_of_questions.html', num_questions=num_questions)


def show_score(score):
    return render_template('score.html', score=score)


def show_high_scores(scores):
    return render_template('high_scores.html', scores=scores)
