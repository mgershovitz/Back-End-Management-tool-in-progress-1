from functools import wraps

from flask import render_template, flash, url_for, session, jsonify
from werkzeug.utils import redirect

from src import session_utils
from src.DB.Models.DTO.nurse_user import NurseUser
from src.run import app
from src.forms import LoginForm, RegisterNurseForm, InsertNewBirthData
from src.tests.dummy_data import posts


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


@app.route("/")
@login_required
def home():
    return redirect(url_for("login"))

@app.route("/nurse/screen")
@login_required
def nurse():
    return render_template('nurse_screen.html', posts=posts)

@app.route("/nurses/screen")
@login_required
def nurses():
    return render_template('nurses_screen.html', posts=posts)


@app.route("/cs_prediction",  methods=['GET', 'POST'])
@login_required
def cs_prediction():
    form = InsertNewBirthData()
    if form.validate_on_submit():
        return render_template('cs_prediction.html', title='Cs_prediction', form=form) #TODO: fix it
    else:
        return "in progress"


@app.route("/department")
# @login_required
def department():
    return render_template('department.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user = NurseUser()
        login_user.email = form.email.data
        login_user.password = form.password.data
        if session_utils.login(login_user):
            if session_utils.is_admin(login_user):
                flash('You have been logged in!', 'success')
                return redirect(url_for('nurses'))
            else:
                flash('You have been logged in!', 'success')
                return redirect(url_for('nurse'))
        else:
             flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    return session_utils.logout()


@app.route("/register/nurse", methods=['GET', 'POST'])
@login_required
def register_nurse():
    form = RegisterNurseForm()
    if form.validate_on_submit():
        if NurseUser().register_nurse():
            flash('You have been Register a Nurse!', 'success')
            return redirect(url_for('nurse'))
        else:
            flash('Register Unsuccessful. Please check username and password', 'danger')
    else:
        return render_template('register_nurse.html', title='register_nurse', form=form)
