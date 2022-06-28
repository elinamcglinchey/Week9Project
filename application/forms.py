from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField

class CustomerForm(FlaskForm):
   customer = StringField("Customer")
   firstName = StringField("First Name")
   lastName = StringField("Last Name")
   userName = StringField("Username")
   password = StringField("Password")
   primeMembership = BooleanField("Prime Membership")
   submit= SubmitField("Submit")

class MealsForm(FlaskForm):
   recipeName = StringField("Recipe Name")
   meat = BooleanField("Meat eater")
   vegetarian = BooleanField("Vegetarian")
   vegan = BooleanField("Vegan")
   calories = IntegerField("Number of calories per meal")
   nutAllergy = BooleanField("Nut allergies")
   otherAllergy = StringField("Any other known allergies")
   submit= SubmitField("Submit")
