from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.dojo import Dojo 
from flask_app.models.ninja import Ninja


@app.route("/")
def index():
    return render_template("index.html", dojos = Dojo.get_all_dojos())

@app.route("/", methods =["POST"])
def create_dojo():
    data = {
        'dn': request.form['dojo']
    }
    new_dojo = Dojo.add_dojo_to_db(data)
    return redirect("/")






#Ninjas Routes..........

@app.route("/dojo/ninjas/<int:id>")
def dojo_ninjas_by_id(id):
    data = {
        'id' : id
    }
    return render_template('dojo.html', ninjas = Ninja.get_by_id(data), dojos = Dojo.get_by_id(data))


@app.route("/dojo/ninjas/add")
def add_ninjas():
    return render_template("ninja.html")


@app.route("/dojo/ninjas/create", methods=["POST"])
def create_ninja_to_db():
    data = {
    "fn": request.form["first_name"],
    "ln": request.form["last_name"],
    "age": request.form["age"],
    "dojo": request.form["dojos_id"]
    }
    ninja_id = Ninja.create_ninja_to_db(data)
    return redirect("/")






