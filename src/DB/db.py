import pymongo
import pandas as pd

# creating new data base
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["my_database"]

# creating collections
nurse_details_col = my_db["nurse_details_col"]  # nurse personal data collection
nurse_statistic_col = my_db["nurses_statistic_col"]  # work statistic collection
hospital_statistic_col = my_db["hospital_statistic_col"]  # hospital_statistic collection
data_files_col = my_db['data_files_col']   # all the excel file paths with hospital and nurse statistic

# methods
# Function to insert data from csv
def read_data_from_csv(file_path):
    df = pd.read_csv(file_path, low_memory=False)
    data = df.to_dict('records')
    my_db.hospital_statistic_col.insert_many(data, ordered=False)



