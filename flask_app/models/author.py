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
    def get_one_author_with_favored_books(cls,data):
        query ="""
            SELECT * FROM authors
            LEFT JOIN favorites
            ON authors.id = favorites.author_id
            LEFT JOIN books AS favorite_books
            ON favorites.book_id = favorite_books.id
            WHERE authors.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data) # Result will be a list of book        objects with the faving author attached to each row
        # print(results)
        this_author = Author(results[0]) # Create an instance of the author class
        data.faved_by = this_author
        print(this_author)
        for book_row in results: # make instances of books this authored faved and add them into our list of this authors favorite books
            if book_row['books.id']:
                data= {
                    "id": book_row["faved_by.id"],
                    "title": book_row["title"],
                    "pages": book_row["pages"],
                    "created_at": book_row["faved_by.created_at"],
                    "updated_at": book_row["faved_by.updated_at"]}
                this_author.favorite_books.append(cls(data))
        print("HERE ARE THIS AUTHORS FAVORITE BOOKS:", this_author)
        return this_author
        

    # @classmethod
    # def get_one_author_by_id(cls,id):
    #     query="""
    #         SELECT * FROM authors
    #         WHERE authors.id = %(id)s"""
    #     data={
    #         "id": id
    #     }
    #     result = connectToMySQL(cls.db).query_db(query,data)
    #     this_author = result[0]
    #     return this_author