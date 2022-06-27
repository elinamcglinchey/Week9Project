from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class Foodform(FlaskForm):
    food = StringField("Food")
    completed = BooleanField("Completed", default=False)
    submit = SubmitField("Submit")

 class CustomerForm(FlaskForm):
    firstName = StringField("First Name")
    lastName = StringField("Last Name")
    username = StringField("Username")
    password = StringField("Password")
    submit= SubmitField("Submit")
