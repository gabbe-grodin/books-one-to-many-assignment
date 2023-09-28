from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author, book

class Favorite:
    db='books'
    def __init__(self, data):
        self.author_id=data['author_id'],
        self.book_id=data['book_id']