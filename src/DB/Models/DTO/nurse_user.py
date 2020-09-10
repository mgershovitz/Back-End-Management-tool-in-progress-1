from flask import jsonify, request
import uuid
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from src.DB.db import my_db, nurse_details_col
from src.session_utils import start_session


class NurseUser:

    def __init__(self):
        self.id = None
        self.email = None
        self.name = None
        self.work_years = None
        self.id_num = None
        self.courses = None
        self.employment_percentage = None
        self.roles = None
        self.is_admin = False

    @classmethod
    def get_nurse(self, name):
        query = {"name": name}
        result_doc = nurse_details_col.find_one(query)
        return result_doc
    #   return NurseUser(result_doc.id_num, result_doc.email)

    @classmethod
    def get_all_nurses_names(collection):
        all_nurses = []
        nurses_names = collection.find({}, {"name"})
        for nurse in nurses_names:
            all_nurses.append(nurse)
        return all_nurses


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
                # "is_admin": request.form.get('is_admin'),
                }
        # Encrypt the password
        user['id_num'] = pbkdf2_sha256.encrypt(user['id_num'])
        nurse_details_col.insert(user)
        print("registered new nurse")
        return start_session(user)

    def get_is_admin(self):
        if self.is_admin:
            return True