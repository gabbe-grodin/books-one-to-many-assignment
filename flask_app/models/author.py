from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book



class Author:
    db = 'books'
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.fav_books=[]

    @classmethod
    def add_new_author(cls, data):
        query="""INSERT INTO authors(name)
            VALUES(%(name)s)"""
        data={
            "name": data["name"]}
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def get_all_authors(cls):
        query ="""
            SELECT * FROM authors"""
        result = connectToMySQL(cls.db).query_db(query)
        authors = []
        for author in result:
            authors.append(cls(author))
            print("HERE ARE ALL THE AUTHORS:", authors)
        return authors