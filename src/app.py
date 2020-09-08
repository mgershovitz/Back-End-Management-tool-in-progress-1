import os
from flask import Flask
from src.DB import db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from src.tests import tests_
from src import routes
from src import utils

# insert hospital statistic to the my_db
# for file in files:
#     if file.endswith('.csv'):
#         db.read_data_from_csv(os.path.abspath(file))

# db.read_data_from_csv('testing_csv.csv')
