"""Form object declaration."""
from flask_wtf import FlaskForm,Form
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired,Email,Required


# Form ORM
class QuizForm(FlaskForm):
    test_field = StringField('Test Field', validators=[Required()])
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    """Contact form."""
    # name = StringField(
    #     'Name',
    #     [DataRequired()]
    # )
    # email = StringField(
    #     'Email',
    #     [
    #         # Email(message=('Not a valid email address.')),
    #         DataRequired()
    #     ]
    # )
    # body = TextField(
    #     'Message',
    #     [
    #         DataRequired(),
    #         Length(min=4,
    #         message=('Your message is too short.'))
    #     ]
    # )
    # recaptcha = RecaptchaField()
    # submit = SubmitField('Submit')
    pass