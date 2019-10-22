# qanda-system

## Description

The solution is a Q and A system which was adapted from a blog implementation using Pythin 3.6 and Flask. The platform allows 
users to Post question and Answers of their choice and then other users' can answer their questions to check their general knowledge.

The idea is to crowd-source the best quetions and answers by letting users generate data for the answer bot to predict the correct answers
without the user who posed having to verify the answer(s)

The system provides user management functionality and the ability to create questions and answers for
users.

There login is authenticated and functionality to recover account and set account information is provided by the 
system.

The project makes use of ORM SQLAlchemy for persisting data and Flask as the microframework delivering the backend and front end functionality. Flask Mail was used for sending emails..

### Run the project

* Clone the repository and ensure python 3 is installed.
* Navigate to the repo using CLI and execute command 'pip install -r requirements.txt'
* Once all the projects dependencies are installed, execute command 'python run.py'

After this the, the project should be running on http://localhost:5000 using your browser to access the system.

#### Testing functionality

After creating an account, and successful login; The user will be shown the questions and answers which they have previously posted.
These can be edited or deleted by clicking on the question and answer entry on the user interface.

To post a new question, the navbar option "New Question And Answer" can be used to add a new set.

To answer question from other users, the navbar option "New Answer" will guide the user to a page of questions to answer.

Optional:
* To use email recovery, set environment variables EMAIL_USER and EMAIL_PASSWORD to ensure you can make use of the 
password recovery functionality before running the project.


## Libraries used:
* Flask:  For creating a web application
* Flask Main:  For sending emails when a user has forgot their password
* Flask SQLAlchemy: The Object Relational Mapper Of Choice
* Flask-Bcrypt:  For ensuring the passwords are stored securely by being encrypted
* Flask-WTF: For common form functionality 
* Flask-Login: For login functionality e.g. getting the current user and checking for authentication

## Missing Functionality

* Providing test results for users after they provided answers
* Adding machine learning by training a bot using NLTK, Numpy, Pandas and TensorFlow to create a bot which can predict the
correct answers without the user's intervention.
