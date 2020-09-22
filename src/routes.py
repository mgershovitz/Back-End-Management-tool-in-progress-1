from functools import wraps
from flask import render_template, flash, url_for, session, jsonify
from werkzeug.utils import redirect
import json

from src import session_utils
from src.DB.Models.department import Department
from src.DB.Models.nurse_statistics import NurseStatistics
from src.DB.Models.nurse_user import NurseUser
from src.DB.db import nurse_details_col
from src.run import app
from src.forms import LoginForm, RegisterNurseForm, InsertNewBirthData


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
    if 'user' in session:
        nurse = []
        nurse.append(NurseUser.get_nurse(session['user']))
        if 'user' in session:
            id = session['user']
        nurse_statistics = NurseStatistics(id)
        return render_template('nurse_screen.html', posts=nurse, posts_nurse=nurse_statistics)


@app.route("/nurses/screen")
@login_required
def nurses():
    nurses_names = NurseUser.get_all_nurses_names()
    return render_template('nurses_screen.html', posts=nurses_names)


@app.route("/cs_prediction",  methods=['GET', 'POST'])
@login_required
def cs_prediction():
    form = InsertNewBirthData()
    if form.validate_on_submit():
        print("validates!")
    else:
        print("in progress")
    return render_template('bleeding_prediction.html', title='bleeding_prediction', form=form) #TODO: fix it


@app.route("/department")
@login_required
def department():
    if 'admin' in session:
        admin_n = session['admin']
    else:
        admin_n = False
    return render_template('department.html', posts=Department(""), posts_admin=admin_n, url='../static/images/pie.png',
                           url2='../static/images/bar.png')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if session_utils.login(form.email.data, form.password.data):
            if 'admin' in session:
                flash('You have been logged in!', 'success')
                return redirect(url_for('nurses'))
            else:
                flash('You have been logged in!', 'success')
                return redirect(url_for('nurse'))
        else:
             flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form, url="../static/images/baby_bg_img.jpg")


@app.route("/logout")
def logout():
    return session_utils.logout()


@app.route("/register/nurse", methods=['GET', 'POST'])
@login_required
def register_nurse():
    form = RegisterNurseForm()
    if form.validate_on_submit():
        # if NurseUser().register_nurse() == 1:
        #     flash('Register Unsuccessful. Please check the the licence id, nurse is already in the system', 'danger')
        #     return redirect(url_for('register_nurse'))
        if NurseUser().register_nurse():
            flash('You have been Register a Nurse!', 'success')
            return redirect(url_for('nurses'))
        else:
            flash('Register Unsuccessful.', 'danger')
    else:
        return render_template('register_nurse.html', title='register_nurse', form=form)


@app.route("/delete/nurse/<id>", methods=['GET', 'POST'])
@login_required
def delete_nurse(id):
    NurseUser.delete_nurse_id(id)
    return redirect(url_for('nurses'))

# create Rest Api


# TODO: fix the encoding of hebrew charcthers or replace to english
@app.route("/nurse/<id>", methods=['GET'])
def get_nurse_route(id):
    nurse = NurseUser.get_nurse(id)             # the _id is the licence number of the nurse
    return jsonify(nurse)


# TODO: fix the encoding of hebrew charcthers or replace to english
@app.route("/nurse/all", methods=['GET'])
def get_all_nurses_data():
    all_nurses = NurseUser.get_all_nurses(nurse_details_col)
    return jsonify(all_nurses)


# TODO: fix the encoding of hebrew charcthers or replace to english
@app.route("/nurse/all/names", methods=['GET'])
def get_all_nurses_name():
    all_nurses_names = NurseUser.get_all_nurses_names()
    return jsonify(all_nurses_names)


# the _id is the licence number of the nurse
@app.route("/nurse/statistic/", methods=['GET'])
def get_nurse_statistic():
    if 'user' in session:
        id = session['user']
        nurse_statistics = NurseStatistics(id)
        return jsonify(nurse_statistics.__dict__)


@app.route("/hospital/statistic/", methods=['GET'])
def get_hospital_statistic_all():
    hospital_statistics = Department("")
    return jsonify(hospital_statistics.__dict__)


@app.route("/hospital/statistic/<year>", methods=['GET'])
def get_hospital_statistic_year_routes(year):
    hospital_statistics = Department(year)
    return json.dumps(hospital_statistics.__dict__)

