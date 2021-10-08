from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():
    def __init__ (self, data):
        self.id = data ['id']
        self.name = data ['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_dojos(cls):
        mysql= connectToMySQL("dojos_ninjas")
        dojos = mysql.query_db('SELECT * FROM dojos;')

        results = []
        for dojo in dojos:
            results.append(cls(dojo))
        
        return results
    
    @classmethod
    def add_dojo_to_db(cls, data):
        mysql = connectToMySQL('dojos_ninjas')
        query = "INSERT INTO dojos (name) VALUES (%(dn)s);"
        new_dojo = mysql.query_db(query,data)
        return new_dojo
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojos_ninjas").query_db(query,data)
        return cls(results[0])

    

