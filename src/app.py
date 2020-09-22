import os
from flask import Flask

from src.DB.Models.nurse_user import NurseUser
from src.DB.db import insert_admin_nurse

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

cwd = os.path.abspath('../')
files = os.listdir(cwd)

from src import routes
# from src.tests import tests_
# from src import visualization

# insert hospital statistic to the my_db
# DBCron().load_from_csv_to_db()

# insert admin nurse to nurse_details_col
if NurseUser().get_nurse("1133069"):
    pass
else:
    insert_admin_nurse('0')