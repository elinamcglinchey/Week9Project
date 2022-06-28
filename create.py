from application import db
from application.models import Customers

db.drop_all()
db.create_all()
sample_customer = Customers(
    userName = "Sample username",
    firstName = "Sample firstname",
    lastName = "Sample lastname",
    primeMembership = False
)
db.session.add(sample_customer)
db.session.commit()
