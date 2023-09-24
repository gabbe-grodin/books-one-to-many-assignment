from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author



class Book:
    db='books'
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.pages=data['pages']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.faved_by=[]

    @classmethod
    def add_new_book(cls,data):
        query="""
            INSERT INTO books(title,pages)
            VALUES(%(title)s,%(pages)s)"""
        data={
            "title":data["title"],
            "pages":data["pages"]}
        result=connectToMySQL(cls.db).query_db(query,data)
        return result
    
    @classmethod
    def get_all_books(cls):
        query="""
            SELECT * FROM books"""
        result=connectToMySQL(cls.db).query_db(query)
        print("RESULTS: ", result)
        books=[]
        for book in result:
            books.append(cls(book))
        print("HERE ARE ALL THE BOOKS:",books)
        return books