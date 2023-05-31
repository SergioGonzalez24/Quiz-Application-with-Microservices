# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#          A01745037 Gala Flores García
#          A01752219 Yunoe Sierra Diaz 
# 	       A01720627 Rodrigo Alfredo Mendoza España
#          A01745158 Erika Marlene García Sánchez
#          A01745446 Sergio González
#          A01752114 Antonio Oviedo Paredes

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Creating the Inserttable for inserting data into the database


class Question(db.Model):
    """
    Class to represent a question in the database

    Class atributes
    ---------------
        __tablename__ : str
            The name of the table in the database.
        id : Column
            ID column in the database.
        question : Column
            Question column in the database.
        answer : Relationship
            Relatiionship in the database betwwn QuestionAnswer and question
    """

    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(255), nullable=False)
    answers = db.relationship('QuestionAnswers', backref='question',lazy=True)

    # method used to represent a class's objects as a string
    def __repr__(self):
        """
        Represents a question object as a string.

        Returns
        -------
            str : Question representation.
        """
        return f'<Question {self.id}>'


class QuestionAnswers(db.Model):
    """
    Class to represent all the possible answers for a question, one of which is correct.

    Class atributes
    ---------------
        __tablename__ : str
            The name of the table in the database.
        id : Column
            ID column in the database.
        question_id : Column
            Foreign key column of question_id in the database.
        answer : Column
            Answer column of the database.
        is_correct : Column
            Column in the database that tells wether an answer is right or wrong.
    """

    __tablename__ = 'question_answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        """
        Represents a QuestionAnswer object as a string

        Returns
        -------
            str : QuestionAnswer representation.
        """
        return f'<QuestionAnswers {self.id}>'


class Scores(db.Model):
    """
    Class to represent the scores of the users

    Class atributes
    ---------------
        __tablename__ : str
            The name of the table in the database.
        id : Column
            ID column in the database.
        initials : Column
            Initials of users column in the database.
        score : Column
            Score of users column in the database.
    """

    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    initials = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """
        Represents a Scores object as a string.

        Returns
        -------
            str : Scores representation.
        """
        return f'<Scores {self.id}>'

