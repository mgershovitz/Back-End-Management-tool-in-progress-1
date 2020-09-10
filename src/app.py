import os
from flask import Flask
from datetime import datetime
from src.db_crone import DBCron

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

cwd = os.path.abspath('../')
files = os.listdir(cwd)

# from src.tests import tests_
# from src import routes
# from src import utils

# insert hospital statistic to the my_db
# DBCron().load_from_csv_to_db()