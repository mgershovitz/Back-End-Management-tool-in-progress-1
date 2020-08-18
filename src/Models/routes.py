class Routes:
    my_routes = {"login_route": "/login",
                 "login_user_route": "/login/<username>",
                 "nurse_personal_data_route": "/nurse/personal/data/<nursename>",
                 "nurse_statistic_route": "/nurse/statistics/<nursename>",
                 "all_nurses_names_route": "/nurse/name/all/admin",
                 "department_statistics": "/department/statistics",
                 "admin_route": "nurse/is/admin/<nurseid>",
                 "nurse_update_data_route": "nurse/update/personal/data/<nurse>",
                 }

    def __init__(self):
        pass

