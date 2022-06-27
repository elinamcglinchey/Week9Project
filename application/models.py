from application import db

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default=False)
