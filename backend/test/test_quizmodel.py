from app import create_app, db
from models.quizmodel import Question, QuestionAnswers, Scores


def test_question_model():
    # Create a question
    question = Question(question='What is the capital of France?')
    db.session.add(question)
    db.session.commit()

    # Retrieve the question from the database
    retrieved_question = Question.query.filter_by(question='What is the capital of France?').first()

    # Assert that the retrieved question is not None
    assert retrieved_question is not None
    # Assert that the retrieved question's ID is not None
    assert retrieved_question.id is not None

def test_question_answers_model():
    # Create a question
    question = Question(question='What is the capital of France?')
    db.session.add(question)
    db.session.commit()

    # Create a question answer
    answer = QuestionAnswers(question_id=question.id, answer='Paris', is_correct=True)
    db.session.add(answer)
    db.session.commit()

    # Retrieve the question answer from the database
    retrieved_answer = QuestionAnswers.query.filter_by(question_id=question.id, answer='Paris').first()

    # Assert that the retrieved answer is not None
    assert retrieved_answer is not None
    # Assert that the retrieved answer's ID is not None
    assert retrieved_answer.id is not None

def test_scores_model():
    # Create a score
    score = Scores(initials='AB', score=100)
    db.session.add(score)
    db.session.commit()

    # Retrieve the score from the database
    retrieved_score = Scores.query.filter_by(initials='AB', score=100).first()

    # Assert that the retrieved score is not None
    assert retrieved_score is not None
    # Assert that the retrieved score's ID is not None
    assert retrieved_score.id is not None
