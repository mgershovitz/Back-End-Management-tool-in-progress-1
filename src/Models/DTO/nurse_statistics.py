from src.Models.DTO.nurse import Nurse


class NurseStatistics(Nurse):
    def __init__(self, year, month, epi, epidoral, cs, vaccum, number_of_births, number_of_living_births,
                 tolac_doVbac_percentange, shoulder_dystocia_perstange, third_degree_tear):
        self.month = month
        self.epi = epi
        self.epidoral = epidoral
        self.year = year
        self.cs = cs
        self.year = year
        self.vaccum = vaccum
        self.number_of_births = number_of_births
        self.number_of_living_births = number_of_living_births
        self.tolac_doVbac_percentange = tolac_doVbac_percentange
        self.shoulder_dystocia_perstange = shoulder_dystocia_perstange
        self.third_degree_tear = third_degree_tear
