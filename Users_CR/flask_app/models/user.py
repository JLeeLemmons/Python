from flask_app.config.mysqlconn import connectToMySQL

class User(): 
    def __init__ (self, data):
        self.id = data ['id']
        self.fullname = data ['full_name']
        self.email = data ['email']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    def full_name(self):
        return f'{self.fullname}'

    @classmethod 
    def get_all_users(cls):
        mysql = connectToMySQL("users_cr")
        users = mysql.query_db('SELECT * FROM users;')

        results = []
        for user in users:
            results.append(cls(user))

        return results

    @classmethod
    def add_user_to_db(cls, data): 
        mysql = connectToMySQL("users_cr")
        query = "INSERT INTO users (full_name, email) VALUES (%(fn)s,%(em)s);" 
        new_user= mysql.query_db(query,data) #It returns an id of a recently created record.
        print(new_user)
        return new_user

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL("users_cr").query_db(query, data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        # Data coming back is always a list.
        results = connectToMySQL("users_cr").query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def edit_user(cls, data):
        mysql = connectToMySQL("users_cr")
        query = "UPDATE users SET full_name = %(fn)s, email = %(em)s WHERE id = %(id)s"
        updated_user= mysql.query_db(query,data)
        return updated_user



