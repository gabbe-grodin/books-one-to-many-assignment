from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import book, author

@app.route('/')
def home():
    return redirect("/books")

@app.route('/books')
def show_all_books():
    all_books=book.Book.get_all_books()
    print(all_books[0], "*"*20)
    return render_template('index.html',book_list=all_books)

@app.route('/add/book', methods=['POST'])
def add_book():
    book.Book.add_book_to_db(request.form)
    return redirect('/books')