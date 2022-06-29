from flask import url_for

from application import app, db
from application.models import Memberships, MealPlans
from application.forms import CustomerForm, MealsForm
from flask import redirect, url_for, render_template, request