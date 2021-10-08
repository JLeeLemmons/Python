from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User 
from flask_app.models.painting import Painting


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/users/register", methods=["POST"])
def register_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email_address': request.form['email_address'],
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password']
    }

    valid = User.validate_registration(data)

    if valid:
        User.create_user(data)
        flash('Account created, log in now!')


    return redirect('/')



@app.route("/users/login", methods=["POST"])
def login_user():
    data = {
        'email_address': request.form['email_address']
    }
    user = User.get_user_by_email(data)

    if user == None:
        flash('Email is invalid')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password is incorrect!')
        return redirect('/')
    session['user_id'] = user.id
    session['user_email'] = user.email
    session['user_first_name'] = user.first_name
    session['user_last_name'] = user.last_name

    return redirect('/paintings')


@app.route('/paintings')
def main_page():
    data = {
        'id' : session['user_id']
    }
    user = User.get_user_by_id(data)
    paintings = Painting.get_all_paintings(data)

    return render_template('main_page.html', user = user, paintings = paintings )


@app.route('/edit/painting/<int:id>')
def edit_painting(id):
    data = {
        'id': id
    }
    painting = Painting.edit_painting(data)[0]
    print(painting)

    return render_template ('edit.html', painting = painting )

@app.route('/edit/painting/update/<int:id>', methods = ['POST'])
def update_painting (id):
    data = {
        'id':id, 
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        }
    painting = Painting.update_painting(data)

    return redirect('/paintings')

@app.route("/add/new/painting")
def add_a_painting():
    return render_template('add_painting.html')

@app.route('/create/painting', methods = ['POST'])
def create_painting():
    data = {
        'title': request.form['title'],
        'price': request.form['price'],
        'description': request.form['description'],
        'users_id': session['user_id']
    }

    valid = Painting.confirm_input(data)
    
    if not valid:
        return redirect('/create/painting')
    painting = Painting.add_painting(data)
        

    return redirect('/paintings')

@app.route('/show/painting/<int:id>')
def show_car(id):
    data = {
        'id': id
    }
    painting = Painting.edit_painting(data)[0]
   
    return render_template('show.html', painting= painting)

@app.route('/delete/painting/<int:id>')
def delete_car(id):
    data = {
        'id':id
    }
    painting = Painting.delete_painting(data)
    return redirect('/paintings')

@app.route("/logout")
def logout(): 
    session.clear() 
    return redirect("/")



