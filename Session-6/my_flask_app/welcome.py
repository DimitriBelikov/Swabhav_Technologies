from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def welcome():
    return f'Welcome to my Webapp {datetime.now()}'

@app.route('/', methods=['GET'])
def add_contact():
    pass