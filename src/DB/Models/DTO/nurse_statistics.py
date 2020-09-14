from src.DB.Models.DTO.nurse_user import NurseUser
from src.DB.db import hospital_statistic_col


class NurseStatistics(NurseUser):
    def __init__(self, id):
        self._id = id
        self.number_of_births = NurseStatistics.count_prognoza(id, "")
        self.number_of_living_births = NurseStatistics.count_living(id)
        self.epi = NurseStatistics.count_prognoza(id, "Episiotomy")
        self.epidoral = NurseStatistics.count_prognoza(id, "EPIDURAL")
        self.cs = NurseStatistics.count_prognoza(id, "Section")
        self.vaccum = NurseStatistics.count_prognoza(id, "Vacuum")
        self.tolac_toVbac_percentange = NurseStatistics.count_prognoza(id, "AFTER")
        self.shoulder_dystocia_perstange = NurseStatistics.count_prognoza(id, "Shoulder")
        self.third_degree_tear = NurseStatistics.count_prognoza(id, "Grade 3")

    @staticmethod
    def get_nurse_statistic_all_records(id):
        nurse_statistics = []
        query = {
            "צוות רפואי": {
                  "$regex": id,
            }
        }
        my_doc = hospital_statistic_col.find(query)
        for doc in my_doc:
            nurse_statistics.append(doc)
        return nurse_statistics


    @staticmethod
    def count_living(id):
        query = {
            "צוות רפואי": {
                "$regex": id,
            },
            "Unnamed: 9": "חי"
        }
        return hospital_statistic_col.count(query)

    @staticmethod
    def count_prognoza(id, prognoza):
        query = {
            "צוות רפואי": {
                "$regex": id,
            },
            "אבחנות בהריון": {
                "$regex": prognoza,
            }
        }
        return hospital_statistic_col.count(query)
