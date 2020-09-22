from DB.Models.nurse_user import NurseUser

# ****************************************************************************************************
# testing

# def test_login():
#     assert cs_prediction() == "hello"

#
# def test_nurse():
#     assert nurse() == render_template('nurse_screen.html', posts=posts)
#
#
# def test_register_nurse():
#     form = RegisterNurseForm()
#     assert register_nurse() == render_template('register_nurse.html', title='register_nurse', form=form)
#
#
# def test_home():
#     assert home() == render_template('home.html')


def test_get_nurse():
    assert NurseUser.get_nurse("1133069") == {'_id': '1133069', 'name': 'צביה כיאב', 'work_years': '45', 'role': 'main_nurse', 'email': 'admin@wolfson.com', 'id_num': '0', 'courses': 'מיילדות, על בסיסי, ניהול', 'employment_percentage': '100%', 'is_admin': True}
#########################################################################################################################
# check this user methods
# print(NurseUser.get_nurse("1133069"))
# print(NurseUser.get_all_nurses_names())
# print(Department.get_hospital_statistic_year("/19"))
# print(NurseStatistics.get_nurse("1133069"))
# print(Department.count_hospital_prognoza("AFTER", "19"))
# print all data in collection
# for doc in my_db.nurese_details_col.find():
#     print(doc)
# nurse = NurseStatistics("1133069")
# print(nurse.cs)
# hospital = Department("19")
# print(hospital.cs)
# print(NurseUser.get_nurse("1133069")._id)


# print(NurseUser().get_nurse('113069')['id_num']