from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField

class CustomerForm(FlaskForm):
   customer = StringField("Customer")
   firstName = StringField("First Name")
   lastName = StringField("Last Name")
   username = StringField("Username")
   password = StringField("Password")
   primeMembership = BooleanField("Prime Membership")
   submit= SubmitField("Submit")
