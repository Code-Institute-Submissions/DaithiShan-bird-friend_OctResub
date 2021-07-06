from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, \
    Length
from models import User

#Customised registration form class from student project - https://github.com/cjcon90/hot-dogz

class RegisterForm(FlaskForm):
    username = StringField('Username',
                           validators=[
                               DataRequired(message="Please enter a username"),
                               Length(min=2, max=12,
                                      message="Please enter a username "
                                              "between 2 and 12 characters "
                                              "long")])
    email = StringField('Email',
                        validators=[
                            DataRequired(message="Please enter an email"),
                            Email(
                                message="Please enter a valid email address"),
                            Length(max=100, message="Email is too long "
                                                    "(100 character max)")])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(
                                     message="Please enter a password")])
    password2 = PasswordField(
        'Repeat Password',
        validators=[
            DataRequired(message="Please double check password"),
            EqualTo('password', message="Passwords don't match! "
                                        "Please try again")])
    submit = SubmitField('Register')