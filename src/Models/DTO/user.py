from flask import Flask, jsonify, request, session, url_for
import uuid
# from flask_login import login_manager
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from werkzeug.utils import redirect

from src.Models.DB.db import my_db
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

class User:

    def start_session(self, user):
        session['logged in'] = True
        session['user'] = user
        return jsonify(user), 200

    def login(self):
        user = my_db.users_col.find_one({'email': request.form.get('email')})    #TODO: fix save the data from register murse in the db so this method will work
        # if user and pbkdf2_sha256.verfiy(request.form.get('password'), user['id_num']):
        return self.start_session(user)
        # return jsonify({"error", "invalid email or password"}), 401

    def logout(self):
        session.clear()
        return redirect(url_for('login'))

    def register_nurse(self):
        # Create the user object
        user = {"_id": uuid.uuid4().hex,
                 "email": request.form.get('email'),
                 "id_num": request.form.get('id_num'),
                 "courses": request.form.get('courses'),
                 "name": request.form.get('name'),
                 "roles": request.form.get('roles'),
                 "work_years": request.form.get('work_years'),
                 "employment_percentage": request.form.get('employment_percentage'),
                 }

        # Encrypt the password
        user['id_num'] = pbkdf2_sha256.encrypt(user['id_num'])
        return self.start_session(user)

    # def get_nurse(self, nurse_name):
    #     pass


# def signup(self):
    #
    #     # Create the user object
    #     user = {"_id": uuid.uuid4().hex,
    #             "email": request.form.get('email'),
    #             "password": request.form.get('password'),
    #             }
    #
    #     # Encrypt the password
    #     user['password'] = pbkdf2_sha256.encrypt(user['password'])
    #     return self.start_session(user)