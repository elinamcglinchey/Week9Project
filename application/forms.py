from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class Foodform(FlaskForm):
    food = StringField("Task")
    completed = BooleanField("Completed", default=False)
    submit = SubmitField("Submit")
