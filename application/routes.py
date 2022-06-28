from application import app, db
from application.models import Memberships
from application.forms import CustomerForm 
from flask import redirect, url_for, render_template, request

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    membership = Memberships.query.all()
    return render_template("customer.html", memberships=membership)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods=['GET','POST'])
def add():
    form = CustomerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            customerData = Memberships(
                userName = form.customer.data,
                firstName = form.customer.data,
                lastName = form.customer.data,
                primeMembership = form.customer.data
            )
            db.session.add(customerData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addcustomer.html', form=form)

@app.route('/customerindex')
def customerindex():
    customers = Memberships.query.all()
    return render_template("listofcustomers.html")

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
            membership.username = form.username.data
        # membership.customer = form.customer.data
        
        db.session.commit()
        return redirect(url_for('customerindex'))
    elif request.method == 'GET':
        form.firstName.data = membership.firstName
        form.lastName.data = membership.lastName
        form.username.data = membership.username
    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    membership = Memberships.query.get(id)
    db.session.delete(membership)
    db.session.commit()
    return redirect(url_for('index'))
