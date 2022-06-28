from application import db

class Memberships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30))
    firstName = db.Column(db.String(30),nullable = True)
    lastName = db.Column(db.String(30),nullable = True)
    primeMembership = db.Column(db.Boolean, default=False)
    
