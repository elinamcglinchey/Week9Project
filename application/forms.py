from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class Foodform(FlaskForm):
    food = StringField("Food")
    completed = BooleanField("Completed", default=False)
    submit = SubmitField("Submit")
