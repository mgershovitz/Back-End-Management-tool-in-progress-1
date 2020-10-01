import os
from flask import Flask

from DB.Models.nurse_user import NurseUser
from DB.db import insert_admin_nurse

ROOT_UESR_ID = '0'
SECRET_KEY_PATH = 'SECRET_KEY'

app = Flask(__name__)
app.config[SECRET_KEY_PATH] = os.getenv(SECRET_KEY_PATH)


cwd = os.path.abspath('../')
files = os.listdir(cwd)

import routes
# import tests_app
import visualization

# insert hospital statistic to the my_db
# DBCron().load_from_csv_to_db()

# insert admin nurse to nurse_details_col
if NurseUser().get_nurse("1133069"):
    pass
else:
    insert_admin_nurse(ROOT_UESR_ID)
