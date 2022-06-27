from application import app, db
from application.models import Meals
from application.forms import TaskForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def index():
    todo = Meals.query.all()
    # empstr = ""
    # for t in todo:
    #     empstr += f'{t.id} {t.task}  {t.completed} <br>' 
    # return empstr
    return render_template("task.html", todos=meal)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/add', methods=['GET','POST'])
def add():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            taskData = Meals(
                task = form.task.data,
                completed = form.completed.data
            )
            db.session.add(taskData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addtask.html', form=form)

@app.route('/complete/<int:id>')
def complete(id):
    meal = Meals.query.get(id)
    meal.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:id>')
def incomplete(id):
    meal = Meals.query.get(id)
    meal.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods= ['GET', 'POST'])
def update(id):
    form = TaskForm()
    meal = Meals.query.get(id)
    if form.validate_on_submit():
        meal.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = meal.task
    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    todo = Meals.query.get(id)
    db.session.delete(meal)
    db.session.commit()
    return redirect(url_for('index'))
