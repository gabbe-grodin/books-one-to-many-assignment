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
            SELECT * FROM authors
            ORDER BY authors.name"""
        result = connectToMySQL(cls.db).query_db(query)
        authors = []
        for author in result:
            authors.append(cls(author))
        # print("HERE ARE ALL THE AUTHORS:", authors)
        return authors
    
    @classmethod
    def get_one_author_with_favored_books(cls):
    # def get_one_author_with_favored_books(cls,data):
        # query ="""
        #     SELECT * FROM authors
        #     LEFT JOIN favorites
        #     ON favorites.author_id = authors.id
        #     LEFT JOIN books
        #     ON favorites.book_id = books.id
        #     WHERE authors.id = %(id)s"""
        # data={
        #     "id": ["favorites.id"],
        #     "title": ["title"],
        #     "pages": ["pages"],
        #     "created_at": ["favorites.created_at"],
        #     "updated_at": ["favorites.updated_at"]}
        # results = connectToMySQL(cls.db).query_db(query,data)
        # this_authors_favs = []
        # for a_book in results:
        #     this_authors_favs.favorite_books.append(cls(a_book))
        # print("HERE ARE THIS AUTHORS FAVORITE BOOKS:", this_authors_favs)
        # return this_authors_favs
        pass

    @classmethod
    def get_one_author_by_id(cls,id):
        query="""
            SELECT * FROM authors
            WHERE authors.id = %(id)s"""
        data={
            "id": id
        }
        result = connectToMySQL(cls.db).query_db(query,data)
        this_author = result[0]
        return this_author