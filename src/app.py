import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from src.tests import tests_
from src import routes
from src import utils


