from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6fa635614898f3c7c4ff3fb4f91c9e4e'

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
