from flask import render_template
from flask_login import login_required

from . import home


@home.route('/')
@login_required
def affirmations():
    return render_template("affirmations.html")

@home.route('/sign_in')
def sign_in():
    """
    Render the homepage template on the / route
    """
    return render_template('index.html')

@home.route('/journal')
def journal():
    return render_template("journal.html")

@home.route('/dashboard')
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    print("*"*80)
    print("index page")
    return render_template('dashboard.html', title="Dashboard")