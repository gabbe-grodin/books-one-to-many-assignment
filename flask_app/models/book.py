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
    def get_one_book_with_favoring_authors(cls, faving_author_data):
        query = """
            SELECT * FROM books
            LEFT JOIN favorites
            ON books.id = favorites.book_id
            LEFT JOIN authors AS faved_by
            ON favorites.author_id = faved_by.id
            WHERE books.id = %(id)s;"""
        result = connectToMySQL(cls.db).query_db(query, faving_author_data)
        this_book = cls(result[0])
        for row in result:
            if row['authors.id']:
                faving_author_data = {
                    "id": row["authors.id"],
                    "name": row["name"],
                    "created_at": row["authors.created_at"],
                    "updated_at": row["authors.updated_at"],
                    "book_id": row["book_id"]}
                this_book.faved_by.append(author.Author(faving_author_data))
        print("One book and authors who faved it:", result)
        return this_book
        
