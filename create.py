from application import db
from application.models import Memberships

db.drop_all()
db.create_all()
sample_membership = Memberships(
    userName = "Sample username",
    firstName = "Sample firstname",
    lastName = "Sample lastname",
    primeMembership = False
)
db.session.add(sample_membership)
db.session.commit()
