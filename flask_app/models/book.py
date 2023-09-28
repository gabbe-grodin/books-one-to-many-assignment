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
            SELECT * FROM books
            ORDER BY books.title"""
        results=connectToMySQL(cls.db).query_db(query)
        # print("RESULTS: ", results)
        books=[]
        for book in results:
            books.append(cls(book))
        # print("HERE ARE ALL THE BOOKS:",books)
        return books
    
    @classmethod
    def get_one_book_with_favoring_authors(cls, id):
        query = """
            SELECT * FROM books
            LEFT JOIN favorites
            ON books.id = favorites.book_id
            LEFT JOIN authors AS faved_by
            ON favorites.author_id = faved_by.id
            WHERE books.id = %(id)s;"""
        data = {
            "id": id
        }
        results = connectToMySQL(cls.db).query_db(query, data) # Results will be a row fo every time the one book object is faved by a new author object list of author objects attached to the faved book object
        this_book = cls(results[0])
        print(this_book)
        for faving_author in results:
            if faving_author['faved_by.id'] != None:
                faving_author_data = {
                    "id": faving_author["faved_by.id"],
                    "name": faving_author["name"],
                    "created_at": faving_author["faved_by.created_at"],
                    "updated_at": faving_author["faved_by.updated_at"],
                    "book_id": faving_author["book_id"]}
                this_book.faved_by.append(author.Author(faving_author_data))
        print("One book and authors who faved it:", this_book)
        return this_book
        
