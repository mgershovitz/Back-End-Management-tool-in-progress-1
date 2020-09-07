# Once a day, run a job, go to folder/s3/etc... look for new files (against db table of data files) and update db


class DBCron:
    def __init__(self):
        self.cron_interval = "24 hours"
        self.data_files_collection_name
        self.db

    def load_from_csv_to_db(self):
        pass

