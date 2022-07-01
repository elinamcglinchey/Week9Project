from application import db

class Memberships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30))
    firstName = db.Column(db.String(30),nullable = True)
    lastName = db.Column(db.String(30),nullable = True)
    primeMembership = db.Column(db.Boolean, default=False)
    mealPlans = db.relationship('MealPlans', backref='membership')

class MealPlans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipeName = db.Column(db.String(30), nullable=False)
    meat = db.Column(db.Boolean, nullable=False)
    vegetarian = db.Column(db.Boolean, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    nutAllergy = db.Column(db.Boolean, nullable=False)
    otherAllergy = db.Column(db.String(30), nullable=False)
    membership_id = db.Column(db.Integer, db.ForeignKey('memberships.id'), nullable=False)


    
