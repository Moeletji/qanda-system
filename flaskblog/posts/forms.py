# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Question', validators=[DataRequired()])
    content = TextAreaField('Answer', validators=[DataRequired()])
    question_type = SelectField(
        'Question Type',
        choices=[('none', 'None'), ('text_question', 'Text Question'), ('numeric_question', 'Numeric Question'), ('binary_question', 'Binary Question')]
    )
    submit = SubmitField('Post Questions and Answers')
    
class AnswerForm(FlaskForm):
    answer = StringField('Answer')
    submit = SubmitField('Post Answers')