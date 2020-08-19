from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3c690aa66f07182f1e510c3b2af275e0exit()'

from src.Models import routes
