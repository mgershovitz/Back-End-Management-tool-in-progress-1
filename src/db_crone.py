# Once a day, run a job, go to folder /src look for new files (against db table of data files) and update db
import os
from datetime import datetime
from DB import db
from DB.db import data_files_col

class DBCron:
    def __init__(self):
        self.cron_interval = "24 hours"
        self.data_files_col = data_files_col
        self.db = db


    def load_from_csv_to_db(self):
        cwd = os.path.abspath('../data_files')
        files = os.listdir(cwd)
        for file in files:
            if file.endswith('.csv'):
                if not data_files_col.find_one({"file_name": file}):
                    try:
                        db.read_data_from_csv("../data_files" + file)
                        db.data_files_col.insert_one({"file_name": file, "date": datetime.now(), "status": True})
                        print("file inserted to db")
                    except:
                        print("Error in inserting file: " + file)
                else:
                    print("file" + file + " is already in db")
            else:
                pass


# TODO: plan how new csv files are inserted to the program
# TODO: automation of load from csv so it will action once a day