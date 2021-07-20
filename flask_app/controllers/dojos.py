from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return render_template("dojo.html")

@app.route('/ninjas')
def ninja():
    return render_template("ninja.html")

@app.route('/dojos/1')
def dojos():
    return render_template("dojo_show.html")