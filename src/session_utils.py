from flask import url_for, session, jsonify
from werkzeug.utils import redirect
from src.DB.db import nurse_details_col
from cryptography.fernet import Fernet

from src.keys.key import key


def start_session(userId):
    session['logged in'] = True
    session['user'] = userId
    if is_admin_id(userId):
        session['admin'] = True
    return jsonify(userId), 200


# TODO: login with Encrypted password
def login(email, password):
    query = {"email": email}
    result = nurse_details_col.find_one(query)
    encrypted = result['id_num']
    f = Fernet(key)   # the key is in bytes
    decrypted = f.decrypt(encrypted)
    print(str(decrypted, 'utf-8'))
    if str(decrypted, 'utf-8') == password:
        return start_session(result["_id"])
    else:
        print("401 - error invalid email or password"), 401


def logout():
    session.clear()
    return redirect(url_for('login'))


def is_admin_id(id):
    if 'is_admin' in session:
        return session["is_admin"]
    else:
        query = {"_id": id}
        result = nurse_details_col.find_one(query)
        if result["is_admin"]:
            return True
        else:
            print("not admin")
            return False


