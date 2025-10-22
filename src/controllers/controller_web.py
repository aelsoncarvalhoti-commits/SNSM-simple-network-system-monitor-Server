from src import app
from flask import render_template
from ..repositories import log_repository

@app.route('/')
def home():

    data = log_repository.select_all_hosts()

    print(data)

    return render_template("hosts.html", data=data)