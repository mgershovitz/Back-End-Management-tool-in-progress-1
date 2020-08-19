from flask import jsonify, request
import uuid


class Nurse:

    def register_nurse(self):
        # Create the nurse object
        nurse = {"_id": uuid.uuid4().hex,
                 "email": request.form.get('email'),
                 "id_num": request.form.get('id_num'),
                 "courses": request.form.get('courses'),
                 "name": request.form.get('name'),
                 "roles": request.form.get('roles'),
                 "work_years": request.form.get('work_years'),
                 "employment_percentage": request.form.get('employment_percentage'),
                 }

        return jsonify(nurse), 200

    def get_nurse(self, nurse_name):
        pass
