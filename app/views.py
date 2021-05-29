from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/journal')
def journal():
    return render_template("journal.html")

@app.route('/affirmations')
def affirmations():
    return render_template("affirmations.html")

@app.route('/reset_password')
def reset_password():
    return render_template("reset_password.html")


@app.route('/account')
def account():
    return render_template("account.html")


@app.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")


@app.route('/sign_up2')
def sign_up2():
    return render_template("sign_up2.html")

