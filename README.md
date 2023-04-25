# Quiz-Application-with-Microservices
Write a quiz application that allows testing the user's knowledge about design patterns and refactorings.

Requirements
 Application Code and Functionality
 The application must comprise at least two microservices plus the web client code that integrates them all and provides the user interface.
The application backend must be written in python.
See Django and Flask for examples of how!
 Each microservice must be implemented as an AWS Lambda function, and provide a RESTful API with JSON requests and responses.
See here for example of creating lambdas from blueprints
Can create APIs using https://fastapi.tiangolo.com/tutorial/
This tutorial could be very useful as a way to create the app in AWS.
 Each microservice should have its own independent persistent data store (if it actually needs one), shared with no other microservice. For read-only data stores, you can use plain text files (for example YAML or JSON files). For read & write data stores, you can use the Amazon DynamoDB or any DB you like. 
 It is recommended to use the Model–View–Controller (MVC) architectural pattern or some relative (MTV, etc)
Each class must be unit-tested and there should be documentation in the README about how to run the test suite.
 The user interface must be intuitive and easy to use. You may use a web front-end framework (for example Bootstrap or W3.CSS) if you like.
 The application must allow the user to select how many different questions (between one and ten) the user wants to answer.
 The questions must be selected randomly from a bank of at least 30 multiple choice items. Questions must be related to software architecture, design patterns, or other software trivia. Sources:
SourceMaking web site (Design Patterns and AntiPatterns)
Slides in class
Other blogs or sites about system design
 Each question must appear all by itself in the browser window.
Once the user answers a question, the application must give the user the corresponding feedback, indicating if the answer was right or wrong, and displaying the correct answer if the user’s choice was wrong. After this, the user can proceed to see and answer the next question.
Once all questions have been answered, the application must display the final score. Also, a score table with the initials and scores (in descending order) of all previous users should be displayed.
Finally, the user should be given the option to restart the quiz application.
 Documentation
 You must write the documentation for your application’s design and architecture.
 Your README.md must contain these sections:
General overview
Diagram(s) of the system and its constituent parts. (This can just be an updated version of project 1.)
Patterns used, and WHY those patterns were chosen. (This can be updated version from project 1, with the addition of your architectural decisions) 
How to install and run the application (including url where hosted)
Acknowledgments and References, if relevant
 Every class and method written must be adequately documented


 All the source files must include at the top the authors’ personal information (name and student id) within comments. For example:
# Final Project: Quiz Application with Microservices
# Date: 28-Nov-2022
# Authors:
#          A01160611 Thursday Rubinstein
#          A01777771 Stephen Strange


There may be an element of group feedback. That is, each student will report whether you think their teammates did a “fair” amount of work. Be sure to contribute to your project, because if you are reported to have not contributed, your grade will suffer. 
