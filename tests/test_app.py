from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Memberships, MealPlans
from flask import redirect, url_for, render_template, request