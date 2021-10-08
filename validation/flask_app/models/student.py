from flask_app.config.mysqlconnection import connectToMySQL

class Student():
    def __init__ (self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.fav_language = data ['fav_language']
        self.comment = data ['comment']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def add_student_to_db(cls, data):
        mysql = connectToMySQL('dojo_survey')
        query = "INSERT INTO students (name, location, fav_language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        new_student = mysql.query_db(query, data)
        return new_student
    
    @classmethod
    def get_student_info(cls):
        mysql= connectToMySQL('dojo_survey')
        students= mysql.query_db("SELECT * FROM students;")
        print(students)

        results = []
        for student in students:
            results.append(cls(student))
        
        return results

    @staticmethod
    def validate_student(student):
        is_valid = True
        if len(student['name']) < 2:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if len(student['location']) < 4:
            flash("Location must be at least 3 characters long.")
            is_valid = False
        if len(student['fav_location']) < 2:
            flash("Language must be filled out.")
            is_valid = False
        if len(student['comment']) < 1:
            flash("Please make sure to place a comment.")
            is_valid = False
        return is_valid
        
    
    