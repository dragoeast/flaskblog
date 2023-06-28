from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm

from flaskblog.models import User, Post

posts = [
    {
        'author': 'Krisztian Markella',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 25, 2023',
    },
    {
        'author': 'Christian Markella',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 26, 2023',
    },
    {
        'author': 'Mark Markella',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'June 27, 2023',
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(message=f"Account created for {form.username.data}!", category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@test.com" and\
           form.password.data == "password":
            flash(message="Successful login", category='success')
            return redirect(url_for('home'))
        else:
            flash(message='Login Unsuccessful. Please check email and password')
    return render_template('login.html', title='Login', form=form)
