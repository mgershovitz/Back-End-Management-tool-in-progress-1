from src.DB.db import hospital_statistic_col


class Department:
    def __init__(self, year):
        self.name = "midwife-wolfson"
        self.year = year
        self.number_of_living_births = Department.count_hospital_living_birth(year)
        self.number_of_births = Department.count_hospital_prognoza("", year)
        self.epi = Department.count_hospital_prognoza("Episiotomy", year)
        self.epidoral = Department.count_hospital_prognoza("EPIDURAL", year)
        self.cs = Department.count_hospital_prognoza("Section", year)
        self.vaccum = Department.count_hospital_prognoza("Vacuum", year)
        self.tolac_doVbac_percentange = Department.count_hospital_prognoza("AFTER", year)
        self.shoulder_dystocia_perstange = Department.count_hospital_prognoza("Shoulder", year)
        self.third_degree_tear = Department.count_hospital_prognoza("Grade 3", year)

    @staticmethod
    def get_hospital_statistic():
        all_statistics = []
        docs = hospital_statistic_col.find()
        for doc in docs:
            all_statistics.append(doc)
        return all_statistics

    @staticmethod
    def get_hospital_statistic_year(year):
        all_statistics = []
        query = {
            "זמן לידה": {
                "$regex": year,
            }
        }
        docs = hospital_statistic_col.find(query)
        for doc in docs:
            all_statistics.append(doc)
        return all_statistics

    @staticmethod
    def count_hospital_prognoza(prognoza, year):
        query = {
            "זמן לידה": {
                "$regex": year,
            },
            "אבחנות בהריון": {
                "$regex": prognoza,
            }
        }
        return hospital_statistic_col.count(query)

    # TODO: check why the num of living + number of dead not adds up to the total number of births.
    @staticmethod
    def count_hospital_living_birth(year):
        query = {
            "זמן לידה": {
                "$regex": year,
            },
            "Unnamed: 9": "חי"
        }
        return hospital_statistic_col.count(query)