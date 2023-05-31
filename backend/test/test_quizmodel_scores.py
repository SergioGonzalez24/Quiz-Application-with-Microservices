# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#          A01745037 Gala Flores García
#          A01752219 Yunoe Sierra Diaz 
# 	       A01720627 Rodrigo Alfredo Mendoza España
#          A01745158 Erika Marlene García Sánchez
#          A01745446 Sergio González
#          A01752114 Antonio Oviedo Paredes

from models.quizmodel import Scores

"""
Code Analysis

Main functionalities:
The Scores class is a model that represents a database table for storing scores. It has three fields: id, initials, and score. The id field is an auto-incrementing primary key, while the initials and score fields are strings and integers, respectively. The main functionalities of this class are to create, read, update, and delete scores in the database.

Methods:
- __repr__(self): returns a string representation of the Scores object, which includes the object's id.
- None

Fields:
- id: an auto-incrementing primary key for the Scores table.
- initials: a string field that stores the initials of the player who achieved the score.
- score: an integer field that stores the score achieved by the player.
"""

class TestScores:
    # Tests that a Scores object can be created with valid initials and score values.
    def test_create_scores_object(self):
        """
        Shiver me timbers! Let's test if we can create a Scores object with valid initials and score values.
        """
        # Arrange
        initials = "AA"
        score = 100

        # Act
        scores_obj = Scores(initials=initials, score=score)

        # Assert
        assert scores_obj.initials == initials
        assert scores_obj.score == score