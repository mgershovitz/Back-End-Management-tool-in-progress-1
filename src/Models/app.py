from flask import Flask, url_for, render_template, flash
from werkzeug.utils import redirect

from src.Models.forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '3c690aa66f07182f1e510c3b2af275e0exit()'

posts = [
    {
        'nurse_name': 'Nurit Lev',
        'role': 'Nurse',
        'work_years': '14',
        'employment_percentage': '100%'
    },
    {
        'nurse_name': 'Tali Queen',
        'role': 'Nurse',
        'work_years': '35',
        'employment_percentage': '100%'
    },
]


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/nurse/screen")
def nurse():
    return render_template('nurse_screen.html', posts=posts)


@app.route("/department")
def department():
    return render_template('department.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@wolfson.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    try:
        from waitress import serve
        serve(app, host='0.0.0.0', port=8888)
    except:
        print('unable to open port')


