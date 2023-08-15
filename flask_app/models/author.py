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
