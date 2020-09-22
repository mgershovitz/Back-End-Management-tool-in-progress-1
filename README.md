This Project is a back-end project in Python.

Overview:
A nursing management tool.

Design summery:
Programing languages: Python, HTML, Css
Using Flask, MongoDB, bootstraps

Progress:
1. Creating a server
2. Creating DB and collections
3. Routes
4. Basic front-end design for the web
5. Implement of methods: register new nurse, login, logout, department methods, and NurseUser methods(get_nurse(), get_all_nurses(), delete_nurse().
6. Redirect to different screens for admin nurse
7. Insert hospital statistics to the DB
8. Display data

Next things we need to do:
1. Create fake hospital db for example to demonstrate the connection between this program and the real hospital db, create script that intakes data from this db 
2. visualization of the statistics

POC:
* Login to the system by:
   as admin:  Username: admin@wolfson.com  Password: 0  
   as not admin:  Username: miki@wilfson.com  Password: 555
* Register new nurse.
* See nurse data.

Run locally:
1. Clone project
2. Install requirements -
pip install -r requirements.txt
3. Run program from src folder
python src/run.py