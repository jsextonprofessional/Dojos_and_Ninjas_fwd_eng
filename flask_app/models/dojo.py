from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_model').query_db(query)
        dojos = []
        for item in results:
            dojos.append(Dojo(item))
        return dojos
