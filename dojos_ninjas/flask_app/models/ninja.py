from flask_app.config.mysqlconnection import connectToMySQL

class Ninja():
    def __init__ (self, data):
        self.id = data ['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.age = data ['age']
        self.updated_at = data ['updated_at']
        self.dojos_id = data ['dojos_id']

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM ninjas WHERE dojos_id = %(id)s;"
        results = connectToMySQL("dojos_ninjas").query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def create_ninja_to_db(cls, data):
        mysql = connectToMySQL("dojos_ninjas")
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES (%(fn)s,%(ln)s,%(age)s, %(dojo)s);"

        new_ninja = mysql.query_db(query,data)
        return new_ninja

    @classmethod
    def get_all_ninjas(cls):
        mysql= connectToMySQL("dojos_ninjas")
        ninjas = mysql.query_db('SELECT * FROM ninjas;')

        results = []
        for ninja in ninjas:
            results.append(cls(ninja))
        
        return results
    
    

