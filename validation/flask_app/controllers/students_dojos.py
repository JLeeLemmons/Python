from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.student import Student

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/student/create", methods = ['POST'])
# def create_student():
#     if not Student.validate_student(request.form):
#         return(redirect('/'))
#     Student.save(request.form)
#     return redirect("/")


@app.route("/student/create", methods = ['POST'])
def create_student():
    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['fav_language'],
        'comment' : request.form ['comment']
    }
    print(request.form)
    new_student = Student.add_student_to_db(data)
    return redirect("/show")

@app.route("/show")
def show_student_info():
    return render_template("show.html", students = Student.get_student_info())




