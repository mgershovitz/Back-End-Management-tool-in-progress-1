import pymongo
import csv
import pandas as pd
import json

# creating new data base
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["my_database"]
nurse_details_col = my_db["nurses"]  # create new collection
nurse_work_data_col = my_db["nurses_work_data_2019"]  # create new collection
dict_2019 = {"_id": "04577766555", "name": "zvia", "numberOfBirths": 100, "twins": 5, "epi": 30, "surgeries": 10}
my_dict = {"_id": "04577766555", "name": "zvia", "work_years": "45", "role": "main_nurse"}
# nurse_details_col.insert_one(my_dict)
# nurse_work_data_col.insert_one(dict_2019)
my_big_dict = [
    {"_id": "00000000000", "name": "dina", "work_years": "40", "role": "vp_main_nurse"},
    {"_id": "10000000000", "name": "irena", "work_years": "40", "role": "nurse"},
    {"_id": "20000000000", "name": "ruth", "work_years": "30", "role": "nurse"},
    {"_id": "30000000000", "name": "nurit", "work_years": "30", "role": "nurse"},
    {"_id": "40000000000", "name": "einat", "work_years": "3", "role": "nurse"}
]
# r = nurse_details_col.insert_many(my_big_dict)

# # check if the data base was created
# print(my_client.list_database_names())
#
# db_list = my_client.list_database_names()
# if "my_database" in db_list:
#     print("The database exists.")
#
# # check if the collection was created
# print(my_db.list_collection_names())
#
# print("the first document is: ")
# doc = nurse_details_col.find_one()  # print the first document
# print(doc)
#
# # different ways to find data in the collection
# for doc in nurse_details_col.find():  # print all the documents
#     print(doc)
# for doc in nurse_details_col.find({}, {"_id": 0, "name": 1}):
#     print(doc)

# query
# print("nurses that their is ruth: ")
# my_query = {"name": "ruth"}
# my_doc = nurse_details_col.find(my_query)
# for doc in my_doc:
#     print(doc)
#
# print("nurses that their name bigger than i are: ")
# my_query_names_gt_i = {"name": {"$gt": "i"}}
# my_doc = nurse_details_col.find(my_query_names_gt_i)
# for doc in my_doc:
#     print(doc)

# print("nurses that their role starts with m are")
# my_regex_query = {"role": {"$regex": "^m"}}
# my_doc = nurse_details_col.find(my_regex_query)
# for doc in my_doc:
#     print(doc)

# sort
# print("sorted list by work years")
# my_doc = nurse_details_col.find().sort("work_years")
# for doc in my_doc:
#     print(doc)

# update values
# print("the updated list is: ")
# my_query = {"role": "main_nurse"}
# new_values = {"$set": {"role": "Main_nurse"}}
# nurse_details_col.update_one(my_query, new_values)
# for doc in nurse_details_col.find():
#     print(doc)

# delete one
# my_query = {"name": "nurit"}
# nurse_details_col.delete_one(my_query)
# print("the updated list is: ")
# for doc in nurse_details_col.find():
#     print(doc)


#get nurse personal data
def get_nurse_data(nursename):
    my_query = {"name": nursename}
    my_doc = nurse_details_col.find(my_query)
    for doc in my_doc:
        return doc

def update_nurse_data():
    pass  #TODO: IMPLEMENT THIS METHOD

# Function to insert data from csv

#
# def read_data_from_csv(file_path):
#     df = pd.read_csv(file_path)
#     data = df.to_dict('records')
#     my_db.nurses_work_data_2019.insert_many(data, ordered=False)


print("***************************testing************************************************")
print(get_nurse_data("dina"))
