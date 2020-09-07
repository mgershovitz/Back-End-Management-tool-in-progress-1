from flask import render_template
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from src.DB.db import my_db
from src.forms import RegisterNurseForm
from src.routes import cs_prediction, nurse, register_nurse, home

# dummy data
posts = [
    {
        'nurse_name': 'Nurit Lev',
        'role': 'Nurse',
        'work_years': '14',
        'employment_percentage': '100%'
    },
    {
        'nurse_name': 'Tali Queen',
        'role': 'Nurse',
        'work_years': '35',
        'employment_percentage': '100%'
    },
]

# dummy data for db
dict_2019 = {"_id": "04577766555", "name": "zvia", "numberOfBirths": 100, "twins": 5, "epi": 30, "surgeries": 10}
my_dict = {"_id": "04577766555", "name": "zvia", "work_years": "45", "role": "main_nurse"}
nurse_personal_data_dict = [
    {"_id": "00000000000", "name": "dina", "work_years": "40", "role": "vp_main_nurse"},
    {"_id": "10000000000", "name": "irena", "work_years": "40", "role": "nurse"},
    {"_id": "20000000000", "name": "ruth", "work_years": "30", "role": "nurse"},
    {"_id": "30000000000", "name": "nurit", "work_years": "30", "role": "nurse"},
    {"_id": "40000000000", "name": "einat", "work_years": "3", "role": "nurse"}
]
users_dict = [
    {"email": "yasmin.schryer@gmail.com", "password": pbkdf2_sha256.encrypt("039762364")},
    {"email": "yony_oz@yahoo.com", "password": pbkdf2_sha256.encrypt("200079580")},
    {"email": "nurit@gmail.com", "password": pbkdf2_sha256.encrypt("044")},
    {"email": "zvia@gmail.com", "password": pbkdf2_sha256.encrypt("144")},
    {"email": "dina@gmail.com", "password": pbkdf2_sha256.encrypt("244")},
    {"email": "tali@gmail.com", "password": pbkdf2_sha256.encrypt("344")},
]
data_file_dict = [
    {"path": "thepath", "date": "date", "status": True}  # if the file was read the status is true, else it's False
]


# inserting data to the db
def insert_one_data_to_collections(collection_name, data):
    my_db.collection_name.insert_one(data)


def insert_many_data_to_collections(collection_name, data):
    my_db.collection_name.insert_many(data)


# testing
# insert_one_data_to_collections(nurse_work_data_col, dict_2019)
# insert_one_data_to_collections(nurse_details_col, my_dict)
# insert_many_data_to_collections(nurse_details_col, nurse_personal_data_dict)
# insert_many_data_to_collections(users_col, users_dict)


def test_login():
    assert cs_prediction() == "hello"


def test_nurse():
    assert nurse() == render_template('nurse_screen.html', posts=posts)


def test_register_nurse():
    form = RegisterNurseForm()
    assert register_nurse() == render_template('register_nurse.html', title='register_nurse', form=form)


def test_home():
    assert home() == render_template('home.html')


# printing db testing
# check if the collection was created
print("the collection name are: ")
print(my_db.list_collection_names())