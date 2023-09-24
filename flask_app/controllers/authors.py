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
    return redirect('/')

# ! SHOW ONE AUTHOR (READ)
# ! SHOW ALL FAVORED BOOKS
# ! FORM VIEW
@app.route('/author/<int:id>')
def view_one_author(id):
    this_author = author.Author.get_one_author_with_favored_books(id)
    return render_template('one_author.html', author = this_author)
