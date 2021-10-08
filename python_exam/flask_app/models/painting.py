from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
import re

bcrypt = Bcrypt(app)

class Painting():
    def __init__(self, data):
        self.painting_id = data['painting_id']
        self.title = data['title']
        self.price = data['price']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
    
    @classmethod
    def get_all_paintings(cls, data):
        mysql = connectToMySQL('final_exam')
        query= "SELECT * FROM users LEFT JOIN paintings ON users.id = paintings.users_id"
        paintings = mysql.query_db(query, data)


        results = []
        for painting in paintings:
            
            results.append(cls(painting))

        return results
    
    @classmethod
    def edit_painting(cls, data):
        mysql = connectToMySQL('final_exam')
        query = "SELECT * FROM paintings WHERE painting_id = %(id)s;"
        painting = mysql.query_db(query,data)
        return painting
    
    @classmethod
    def update_painting(cls, data):
        mysql = connectToMySQL('final_exam')
        query = "UPDATE paintings SET title = %(title)s, description = %(description)s, price = %(price)s WHERE painting_id = %(id)s" 
        results = mysql.query_db(query,data)
        painting = cls(results[0])
        return painting
    
    @classmethod
    def add_painting(cls, data):
        mysql = connectToMySQL('final_exam')
        query = "INSERT INTO paintings (title, price, description, users_id) VALUES (%(title)s, %(price)s, %(description)s, %(users_id)s)"
        new_painting = mysql.query_db(query, data)

        return new_painting
    
    @classmethod
    def delete_painting(cls, data):
        mysql = connectToMySQL('final_exam')
        query = "DELETE FROM paintings WHERE painting_id = %(id)s"
        painting = mysql.query_db(query, data)

        return painting

    @staticmethod 
    def confirm_input(data):
        is_valid = True
        if len(data['title']) < 0: 
            is_valid = False
            flash('price needs to be greater than 0')
        if len(data['price']) < 0:
            is_valid = False
            flash('make needs to be filled out')
        if len(data['description']) <= 10:
            is_valid = False
            flash('Please add some descriptive words here')
        return is_valid

    

