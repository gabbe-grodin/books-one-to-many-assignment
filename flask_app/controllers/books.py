from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import book, author

# @app.route('/')
# def books():
#     return redirect("/books")

# ! SHOW ALL BOOKS (READ)
# ! FORM VIEW
@app.route('/books')
def show_all_books():
    all_books=book.Book.get_all_books()
    # print(all_books[0], "*"*20)
    return render_template('books.html',book_list = all_books)

# ! INVISIBLE (CREATE)
@app.route('/book/create', methods=['POST'])
def add_book():
    book.Book.add_new_book(request.form)
    return redirect('/books')

# ! SHOW ONE BOOK (READ)
# ! SHOW ALL AUTHORS WHO HAVE FAVORED IT (READ)
# ! FORM VIEW (dropdown of all authors who haven't yet favored?)
@app.route('/book/<int:id>')
def show_one_book_with_faving_authors(id):
    this_book = book.Book.get_one_book_with_favoring_authors(id)
    return render_template('one_book.html', book = this_book)