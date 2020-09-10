from flask import url_for, request, session, jsonify
from werkzeug.utils import redirect
from src.DB.db import my_db, nurse_details_col


def start_session(userId):
    session['logged in'] = True
    session['user'] = userId
    return jsonify(userId), 200


# TODO: login with Encrypted password
def login(user):
    query = {"email": user.email, "id_num": user.password}
    result = nurse_details_col.find_one(query)
    if result:
        return start_session(user.id)
    else:
        print("401 - error invalid email or password"), 401


def logout():
    session.clear()
    return redirect(url_for('login'))


def is_admin(user):
    query = {"email": user.email, "id_num": user.password}
    result = nurse_details_col.find_one(query)
    if result["is_admin"]:
        return True
