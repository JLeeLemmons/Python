from flask_app.config.mysqlconnection import connectToMySQL

class User():
    def __init__ (self,data):
        self.id = data ['id']
        self.fullname = data ['full name']
        self.email = data ['email']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    def full_name(self):
        return f'{self.fullname}'

    @classmethod
    def get_all_users(cls):
        users = connectToMySQL("user_table").query_db('SELECT * FROM all_users;')

        results = []
        for user in users:
            results.append(cls(user))
        return results
    
    @classmethod
    def get_user_id(cls, data):
        query = 'SELECT * FROM all_users WHERE id = %(id)s;'
        results = connectToMySQL("user_table").query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def edit_user(cls, data):
        mysql = connectToMySQL("user_table")
        query = "UPDATE all_users SET full_name = %(fn)s, email = %(em)s WHERE id = %(id)s"
        updated_user=mysql.query_db(query,data)
        return updated_user







