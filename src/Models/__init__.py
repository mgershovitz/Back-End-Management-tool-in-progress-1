from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3c690aa66f07182f1e510c3b2af275e0exit()'

from src.Models import routes
from src.Models import utils
from src.Models.DB import db

# insert hospital statistic to the my_db
db.read_data_from_csv('total_statistic.csv')

# print all the docs in hospital collection
for doc in db.my_db.hospital_statistic_col.find():
    print(doc)
