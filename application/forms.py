from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class Taskform(FlaskForm):
    task = StringField("Task")
    completed = BooleanField("Completed", default=False)
    submit = SubmitField("Submit")
