from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import book, author

@app.route('/')
def home():
    return redirect('/books')

# @app.route('/authors')
# def get_all():
#     return render_template('authors.html')