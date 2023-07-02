from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField(label='Username',
                           validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField(label='Email',
                           validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',
                           validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password',
                           validators=[DataRequired(), EqualTo(fieldname='password')])
    submit = SubmitField(label='Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(message='That user is taken. Please chose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(message='That email is taken. Please chose a different one.')


class LoginForm(FlaskForm):
    email = StringField(label='Email',
                           validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',
                           validators=[DataRequired()])
    remember = BooleanField(label='Remember Me')
    submit = SubmitField(label='Log In')
    