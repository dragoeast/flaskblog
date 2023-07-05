from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
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


class UpdateAccountForm(FlaskForm):
    username = StringField(label='Username',
                           validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField(label='Email',
                           validators=[DataRequired(), Email()])

    picture = FileField(label='Update Porfile Picture',
                        validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField(label='Update')



    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(message='That user is taken. Please chose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
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


class PostForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    content = TextAreaField(label='Content', validators=[DataRequired()])
    submit = SubmitField(label='Post')

class RequestResetForm(FlaskForm):
    email = StringField(label='Email',
                           validators=[DataRequired(), Email()])
    submit = SubmitField(label='Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            error_message = "There is no account with that email. You must register first."
            raise ValidationError(message=error_message)

class ResetPasswordForm(FlaskForm):
    password = PasswordField(label='Password',
                           validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password',
                           validators=[DataRequired(), EqualTo(fieldname='password')])
    submit = SubmitField(label='Reset Password')
