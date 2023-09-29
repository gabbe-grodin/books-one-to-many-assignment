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
        query ="""SELECT * FROM authors
            ORDER BY authors.name"""
        result = connectToMySQL(cls.db).query_db(query)
        authors = []
        for author in result:
            authors.append(cls(author))
        # print("HERE ARE ALL THE AUTHORS:", authors)
        return authors


    @classmethod
    def get_one_author_with_favored_books(cls,id):
        # alias used in query below is same name as added class attribute - is that okay? andrew says i can do without below alias and just deleting it shouldn't break this code. try...
        query ="""SELECT * FROM authors
            LEFT JOIN favorites
            ON authors.id = favorites.author_id
            LEFT JOIN books AS favorite_books
            ON favorites.book_id = favorite_books.id
            WHERE authors.id = %(id)s;"""
        data = {
            "id":id}
        results = connectToMySQL(cls.db).query_db(query, data) # Results should be a row for every time this author object favorites, a new book object
        print(results)
        this_author = cls(results[0]) # Create an instance of the author class
        print(this_author)
        for book_row in results: # make instances of books this authored faved and add them into our list of this authors favorite books
            if book_row['favorite_books.id'] != None:
                fav_book_data= {
                    "id": book_row["favorite_books.id"],
                    "title": book_row["title"],
                    "pages": book_row["pages"],
                    "created_at": book_row["favorite_books.created_at"],
                    "updated_at": book_row["favorite_books.updated_at"],
                    "author_id": book_row["author_id"]}
                this_author.favorite_books.append(book.Book(fav_book_data))
        print("HERE ARE THIS AUTHORS FAVORITE BOOKS:", this_author)
        return this_author


    # !!! Should I move this class method to a favorite model?
    @classmethod
    def add_a_favorite(cls, data):
        query = """INSERT INTO favorites(author_id, book_id)
            VALUES(%(author_id)s, %(book_id)s);"""
        result = connectToMySQL(cls.db).query_db(query, data)
        # faving_author = cls(result[0])
        # print(faving_author)
        # return faving_author
        print("RRRRRRREEEEEEEEEEEESSSSSUUUULLLLT:",result)
        return result