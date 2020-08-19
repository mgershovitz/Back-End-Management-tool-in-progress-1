from functools import wraps

from flask import render_template, flash, url_for, session
from werkzeug.utils import redirect

from src.Models.DTO.nurse import Nurse
from src.Models.DTO.user import User
from src.Models.run import app
from src.Models.forms import LoginForm, RegisterNurseForm

# from src.Models.db import my_db


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('home'))
    return wrap


# dummy data
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
@login_required
def nurse():
    return render_template('nurse_screen.html', posts=posts)


@app.route("/department")
@login_required
def department():
    return render_template('department.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@wolfson.com' and form.password.data == 'password':
            # if my_db.users_col.find({}, {form.email.data, form.password.data}):
            flash('You have been logged in!', 'success')
            # login_user(user)
            User().signup()
            return redirect(url_for('nurse'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    return User().logout()


@app.route("/register/nurse", methods=['GET', 'POST'])
@login_required
def register_nurse():
    form = RegisterNurseForm()
    if form.validate_on_submit():
        return Nurse().register_nurse()
    #     flash('You have been Register a Nurse!', 'success')
    # else:
    #    flash('Register Unsuccessful. Please check username and password', 'danger')
    return render_template('register_nurse.html', title='register_nurse', form=form)
