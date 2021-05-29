'''
from flask import render_template,make_response, request,\
    jsonify,redirect,url_for

from app import app
from .forms import ContactForm,QuizForm


@app.route('/')
def index():
    return render_template("affirmations.html")

@app.route('/sign_in')
def sign_in():
    return render_template("index.html")

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

@app.route('/test_api',methods=['GET'])
def test_api():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(my_dict), 200, headers)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )
@app.route("/quiz_form")
def quiz_form():
    form = QuizForm()
    return render_template('quiz_form.html', quiz_form = form)
'''
