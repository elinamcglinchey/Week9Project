from application import db
from application.models import Meals

db.drop_all()
db.create_all()
sample_meal = Meals(
    food = "Sample meal",
    completed = False
)
db.session.add(sample_meal)
db.session.commit()
