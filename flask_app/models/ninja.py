from flask_app.config.mysqlconnection import connectToMySQL

class Ninja():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.ago = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_model').query_db(query)
        ninjas = []
        for item in results:
            ninjas.append(cls(item))
        return ninjas
