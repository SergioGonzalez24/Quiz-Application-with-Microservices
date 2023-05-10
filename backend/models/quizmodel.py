from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Creating the Inserttable for inserting data into the database


class Question(db.Model):

    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(255), nullable=False)
    answers = db.relationship('QuestionAnswers', backref='question',lazy=True)

    # method used to represent a class's objects as a string
    def __repr__(self):
        return f'<Question {self.id}>'


class QuestionAnswers(db.Model):

    __tablename__ = 'question_answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<QuestionAnswers {self.id}>'


class Scores(db.Model):

    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    initials = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Scores {self.id}>'

