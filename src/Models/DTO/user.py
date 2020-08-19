from flask import Flask, jsonify, request, session, url_for
import uuid
from flask_login import login_manager
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from werkzeug.utils import redirect


class User:

    def start_session(self, user):
        session['logged in'] = True
        session['user'] = user
        return jsonify(user), 200

    # def login(self):
    #     user = {"_id": uuid.uuid4().hex,
    #             "email": request.form.get('email'),
    #             "password": request.form.get('password'),
    #             }
    #     #
    #     # # Encrypt the password
    #     # user['password'] = pbkdf2_sha256.encrypt(user['password'])
    #     return jsonify(user), 200


    def signup(self):

        # Create the user object
        user = {"_id": uuid.uuid4().hex,
                "email": request.form.get('email'),
                "password": request.form.get('password'),
                }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt( user['password'])
        return self.start_session(user)

    def logout(self):
        session.clear()
        return redirect(url_for('home'))


