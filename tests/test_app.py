from flask import url_for
from flask_testing import TestCase

# forms not needed
from application import app, db
from application.models import Memberships, MealPlans
from flask import redirect, url_for, render_template, request

class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        
        sample_membership = Memberships(firstName="Elina", lastName="McGlinchey", userName="elinamcglinchey", primeMembership = True)
        # save users to database
        db.session.add(sample_membership)
        db.session.commit()

        sample_mealplan = MealPlans(recipeName = "Carbonara", meat = True, vegetarian = False, vegan = False, calories = 500, nutAllergy = True, otherAllergy = "N/A", membership_id = 1)
        #problem with line above - error/invalid syntax
        db.session.add(sample_mealplan)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality/routes.py
class TestViews(TestBase):


    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Customers', response.data)

    def test_mealindex_get(self):
        response = self.client.get(url_for('mealindex'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Meal Plans', response.data)
    
    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Customer', response.data)

    def test_addmeal_get(self):
        response = self.client.get(url_for('addmeal'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Meals', response.data)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update Customer info', response.data)

    def test_updatemeal_get(self):
        response = self.client.get(url_for('updatemeal', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update your meals info', response.data)


class TestDeleteCustomer(TestBase):
    
    def test_delete_customer(self):
        response = self.client.get(
            url_for('delete', id=1),
            data = dict(firstName = "Elina", lastName = "McGlinchey", userName = "elinamcglinchey", primeMembership = True)
        )
        assert len(Memberships.query.all()) == 1
        assert len(MealPlans.query.all()) == 1

class TestDeleteMeal(TestBase):
    def test_deletemeal_post(self):
        response = self.client.get(
            url_for('deletemeal',id=1),
            data = dict(message="deleted meal" ,membership_id=1)
        )
        assert len(MealPlans.query.all()) == 1

#Test update for customer and meal
#Test add for customer and meal