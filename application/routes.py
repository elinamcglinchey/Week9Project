from application import app, db
from application.models import Memberships, MealPlans
from application.forms import CustomerForm, MealsForm 
from flask import redirect, url_for, render_template, request

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    membership = Memberships.query.all()
    return render_template("customer.html", memberships=membership)

@app.route('/mealindex')
def mealindex():
    meal = MealPlans.query.all()
    return render_template("meals.html", meals=meal)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods=['GET','POST'])
def add():
    form = CustomerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            customerData = Memberships(
                firstName = form.firstName.data,
                lastName = form.lastName.data,
                userName = form.userName.data,
                primeMembership = form.primeMembership.data
            )
            db.session.add(customerData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addcustomer.html', form=form)

@app.route('/addmeal', methods=['GET','POST'])
def addmeal():
    form = MealsForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            recipeNameData = MealPlans(
                recipeName = form.recipeName.data,
                meat = form.meat.data,
                vegetarian = form.vegetarian.data,
                vegan = form.vegan.data,
                calories = form.calories.data,
                nutAllergy = form.nutAllergy.data,
                otherAllergy = form.otherAllergy.data,
                membership_id= form.membership_id.data
            )
            db.session.add(recipeNameData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addmeals.html', form=form)


@app.route('/customerindex')
def customerindex():
    membership = Memberships.query.all()
    return render_template("listofcustomers.html", memberships=membership)

@app.route('/active/<int:id>')
def active(id):
    membership = Memberships.query.get(id)
    membership.active = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/inactive/<int:id>')
def inactive(id):
    membership = Memberships.query.get(id)
    membership.active = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods= ['GET', 'POST'])
def update(id):
    form = CustomerForm()
    membership = Memberships.query.get(id)
    Customer = Memberships.query.all()
    if request.method == 'POST':
        if form.validate_on_submit():
            membership.firstName = form.firstName.data
            membership.lastName = form.lastName.data
            membership.userName = form.userName.data
        # membership.customer = form.customer.data
        
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.firstName.data = membership.firstName
        form.lastName.data = membership.lastName
        form.userName.data = membership.userName
    return render_template('update.html', form=form)

@app.route('/updatemeal/<int:id>', methods= ['GET', 'POST'])
def updatemeal(id):
    form = MealsForm()
    meal= MealPlans.query.get(id)
    Recipe = MealPlans.query.all()
    if request.method == 'POST':
        if form.validate_on_submit():
            meal.recipeName = form.recipeName.data
            meal.meat = form.meat.data
            meal.vegetarian = form.vegetarian.data
            meal.vegan = form.vegan.data
            meal.calories = form.calories.data
            meal.nutAllergy = form.nutAllergy.data
            meal.otherAllergy = form.otherAllergy.data
            #meal.membership_id = form.membership_id.data
        
        db.session.commit()
        return redirect(url_for('mealindex'))
    elif request.method == 'GET':
        form.recipeName.data = meal.recipeName
        form.meat.data = meal.meat
        form.vegetarian.data = meal.vegetarian
        form.vegan.data = meal.vegan
        form.calories.data = meal.calories
        form.nutAllergy.data = meal.nutAllergy
        form.otherAllergy.data = meal.otherAllergy
        form.membership_id = meal.membership_id
    return render_template('updatemeal.html', meal=meal, form=form)


@app.route('/delete/<int:id>')
def delete(id):
    membership = Memberships.query.get(id)
    db.session.delete(membership)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/deletemeal/<int:id>')
def deletemeal(id):
    meal = MealPlans.query.get(id)
    db.session.delete(meal)
    db.session.commit()
    return redirect(url_for('mealindex'))