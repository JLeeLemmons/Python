from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconn import connectToMySQL

from flask_app.models.user import User 

@app.route("/users")
def index():
    # mysql = connectToMySQL("users_cr")
    # users = mysql.query_db('SELECT * FROM users;')

    return render_template("index.html", users = User.get_all_users())


@app.route("/users/add")
def create_user(): 
    
    return render_template("form.html")
    


@app.route("/users/create", methods=["POST"])
def add_user_to_db():
    data = {
        'fn': request.form['fname'],
        'em': request.form['email']
    }
    user_id = User.add_user_to_db(data)
    return redirect(f"/show/user/{user_id}")


@app.route("/delete/user/<int:user_id>")
def delete_user(user_id):  
    data = {
        "id": user_id
    }
    User.destroy(data)

    return redirect ("/users")


@app.route("/edit/user/<int:user_id>")
def edit_user(user_id):
    data = {
        "id": user_id
    }
    return render_template('edit.html', edit_user= User.get_by_id(data))

@app.route("/edit/update/<int:user_id>", methods=["POST"])
def edit_update(user_id):
    data = {
        'fn': request.form['fname'],
        'em': request.form['email'],
        'id': user_id
    }
    User.edit_user(data)
    return redirect("/users")
    

@app.route("/show/user/<int:user_id>")
def show_user(user_id):
    data = {
        'id': user_id
    }
    
    return render_template('show.html', user = User.get_by_id(data))