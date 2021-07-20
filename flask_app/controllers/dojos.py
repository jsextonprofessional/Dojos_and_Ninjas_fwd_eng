from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# redirects to homepage
@app.route('/')
def index():
    return redirect("/dojos")

# homepage - required page 1
@app.route('/dojos')
def dojos_home():
    dojos = Dojo.get_all_dojos()
    return render_template("dojo.html", dojos = dojos)

# ninjas page - required page 2 - displays form for new Ninjas to join a dojo
@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("ninja.html", dojos = dojos)

# takes form data from ninjas page, adds to database, and redirects to dojo show
@app.route('/process_ninja', methods=['POST'])
def process_ninja_form():
    Ninja.add_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo-select']}")
# 
# @app.route('/process_dojo', methods=['POST'])

# dojo show page - required page 3
@app.route('/dojos/<int:dojo_id>')
def dojo_show(dojo_id):
    data = {
        'id': dojo_id
    }
    ninjas = Ninja.get_all_ninjas_by_dojo_id(data)
    dojo = Dojo.get_dojo_by_id(data)
    return render_template("dojo_show.html", dojo = dojo, ninjas = ninjas)

# @app.route('/dojos/<int:dojo_id>')
# def dojo_show(dojo_id):
#     data = {
#         'id': dojo_id
#     }
#     dojo = Dojo.get_dojo_by_id(data)
#     return render_template("dojo_show.html", dojo = dojo)