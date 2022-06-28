from application import app, db
from application.models import Customers
from application.forms import CustomerForm 
from flask import redirect, url_for, render_template, request

@app.route('/')
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
                customer = form.customer.data,
                completed = form.completed.data
            )
            db.session.add(customerData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addcustomer.html', form=form)

@app.route('/complete/<int:id>')
def complete(id):
    membership = Memberships.query.get(id)
    membership.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:id>')
def incomplete(id):
    membership = Memberships.query.get(id)
    membership.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods= ['GET', 'POST'])
def update(id):
    form = CustomerForm()
    membership = Memberships.query.get(id)
    if form.validate_on_submit():
        membership.food = form.customer.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.customer.data = membership.customer
    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    membership = Memberships.query.get(id)
    db.session.delete(membership)
    db.session.commit()
    return redirect(url_for('index'))
