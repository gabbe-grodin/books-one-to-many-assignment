from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import book, author

# ! INDEX
# ! SHOW ALL AUTHORS (READ)
# ! FORM VIEW
@app.route('/')
def home():
    all_authors = author.Author.get_all_authors()
    return render_template('index.html', all_authors = all_authors)

# ! INVISIBLE (CREATE)
@app.route('/author/create', methods=['POST'])
def add_author():
    author.Author.add_new_author(request.form)
    return redirect("/")
    # return redirect(f"/author/{request.form['id']}")






# ! SHOW ONE AUTHOR (READ)
# ! SHOW ALL FAVORED BOOKS
# ! FORM VIEW
@app.route('/author/<int:author_id>')
def view_one_author_and_fav_books(author_id):
    this_authors_fav_books = author.Author.get_one_author_with_favored_books(author_id)
    all_books=book.Book.get_all_books() # this doesn't need to pass anything. it only populates a list of all books.
    return render_template('one_author.html', this_author = this_authors_fav_books, all_books = all_books)






# # ! INVISIBLE (CREATE)
# @app.route('/author/<int:author_id>/picks/fav', methods=['POST']) # Do I need to use the ID variable in this route?
# def this_author_picks_a_favorite(book_id):
#     # data = {
#     #     "book_id": book_id
#     # }
#     this_authors_fav_books = book.Book.add_a_favorite(book_id)
#     return redirect(f"/author/{request.form['author_id']}")