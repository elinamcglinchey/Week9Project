from application import db
from application.models import Memberships, MealPlans

db.drop_all()
db.create_all()

sample_membership = Memberships(
    userName = "Sample username",
    firstName = "Sample firstname",
    lastName = "Sample lastname",
    primeMembership = False
)

sample_mealplan = MealPlans(
    recipeName = "Sample recipe name",
    meat = True,
    vegetarian = False,
    vegan = False,
    calories = 500,
    nutAllergy = True,
    otherAllergy = "N/A"
)
db.session.add(sample_membership)
db.session.add(sample_mealplan)
db.session.commit()
