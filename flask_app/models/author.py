from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book



class Author:
    db = 'books'
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.favorite_books=[]

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
    
    @classmethod
    def get_one_author_with_favored_books(cls, id):
        query ="""
            SELECT * FROM books
            LEFT JOIN favorites
            ON favorites.book_id = books.id
            LEFT JOIN authors
            ON favorites.author_id = authors.id
            WHERE books.id = %(id)s"""
        data={
            "id": data["id"]}
        results = connectToMySQL(cls.db).query_db(query,id)
        favorite_books = [] # why do i need this when i have line 13? or what is the difference?
        for row in results:
            favorite_books.append(cls(book))
        print("HERE ARE THIS AUTHORS FAVORITE BOOKS:", favorite_books)
        return favorite_books