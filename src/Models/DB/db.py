import collections

import pymongo
import csv
import pandas as pd
import json

# creating new data base
from passlib.handlers.pbkdf2 import pbkdf2_sha256

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["my_database"]


# creating collections
nurse_details_col = my_db["nurses"]  # nurse personal data collection
nurse_work_data_col = my_db["nurses_work_data_2019"]  # work statistic collection
users_col = my_db["users"]  # user collection
hospital_statistic_col = my_db["hospital_statistic"] # hospital_statistic collection

# dummy data
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


# inserting data to the db
nurse_details_col.insert_one(my_dict)
nurse_work_data_col.insert_one(dict_2019)
nurse_personal_data = nurse_details_col.insert_many(nurse_personal_data_dict)
users = users_col.insert_many(users_dict)


# get nurse personal data
def get_nurse_data(nursename):
    my_query = {"name": nursename}
    my_doc = nurse_details_col.find(my_query)
    for doc1 in my_doc:
        return doc1

# ******************************************************************************************
# Function to insert data from csv

def read_data_from_csv(file_path):
    df = pd.read_csv(file_path, low_memory=False)
    data = df.to_dict('records')
    my_db.hospital_statistic_col.insert_many(data, ordered=False)


# print("***************************testing************************************************")
# # check if the data base was created
# print(my_client.list_database_names())

# db_list = my_client.list_database_names()
# if "my_database" in db_list:
#     print("The database exists.")
#
# check if the collection was created
print("the collection name are: ")
print(my_db.list_collection_names())

# print all users documents
# print("The users are: ")
# for doc in users_col.find():
#     print(doc)
#
# print(get_nurse_data("dina"))


# ******************************************************************************************

#print all hospital statistic documents
# print("The hospital statistic are: ")
# for doc in hospital_statistic_col.find():
#     print(doc)