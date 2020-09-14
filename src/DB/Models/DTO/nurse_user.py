from flask import jsonify, request
import uuid
# from passlib.handlers.pbkdf2 import pbkdf2_sha256
# from werkzeug.security import generate_password_hash
from src.DB.db import nurse_details_col
from src.session_utils import start_session


class NurseUser:

    def __init__(self, id):
        self._id = id
        self.email = None
        self.name = None
        self.work_years =None
        self.id_num = None
        self.courses = None
        self.employment_percentage = None
        self.role = None
        self.is_admin = None


    @staticmethod
    def get_nurse(id):
        query = {"_id": id}
        result_doc = nurse_details_col.find_one(query)
        #nurse = NurseUser(id)
        #return nurse
        return result_doc

    @staticmethod
    def get_all_nurses_names():
        all_nurses = []
        nurses_names = nurse_details_col.find({}, {"name"})
        for nurse in nurses_names:
            all_nurses.append(nurse)
        return all_nurses

    # TODO: fix this method
    @classmethod
    def get_all_nurses(self, collection):
        all_nurses = []
        nurses_names = collection.find()
        for nurse in nurses_names:
            all_nurses.append(nurse)
        return all_nurses


    def register_nurse(self):
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
        # user['id_num'] = pbkdf2_sha256.hash(user['id_num'])
        nurse_details_col.insert(user)
        print("registered new nurse")
        return start_session(user)
