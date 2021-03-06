from flask import jsonify, request, url_for
from cryptography.fernet import Fernet
from werkzeug.utils import redirect
# import uuid

from DB.db import nurse_details_col
from keys.key import key


class NurseUser:
    def __init__(self):
        self._id = None
        self.email = None
        self.name = None
        self.work_years = None
        self.id_num = None
        self.courses = None
        self.employment_percentage = None
        self.role = None
        self.is_admin = False

    @staticmethod
    def get_nurse(id):
        query = {"_id": id}
        result_doc = nurse_details_col.find_one(query)
        return result_doc

    @staticmethod
    def get_all_nurses_names():
        all_nurses = []
        nurses_names = nurse_details_col.find({}, {"name"})
        for nurse in nurses_names:
            all_nurses.append(nurse)
        return all_nurses

    @staticmethod
    def get_all_nurses(collection):
        all_nurses = []
        nurses_names = collection.find()
        for nurse in nurses_names:
            all_nurses.append(nurse)
        return all_nurses

    @staticmethod
    def register_nurse():
        # hashed = generate_password_hash(request.form.get('id_num'), "sha256")
        # Create the user object
        user = {"_id": request.form.get('nurse_license_id'),
                "email": request.form.get('email'),
                "id_num": request.form.get('id_num'),
                "courses": request.form.get('courses'),
                "name": request.form.get('name'),
                "roles": request.form.get('roles'),
                "work_years": request.form.get('work_years'),
                "employment_percentage": request.form.get('employment_percentage'),
                "is_admin": False,
                }
        # Encrypt the password
        original_id_num = user['id_num'].encode()
        f = Fernet(key)  # the key is in bytes
        encrypted = f.encrypt(original_id_num)  # Encrypt the bytes. The returning object is of type bytes
        user['id_num'] = encrypted
        try:
            nurse_details_col.insert(user)
            print("registered new nurse")
            return True
        except:
            print("nurse is already in the db")
            return redirect(url_for('register_nurse'))

    @staticmethod
    def delete_nurse_id(id):
        nurse_details_col.delete_one({'_id': id})
        return 1;
