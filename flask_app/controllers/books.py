from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import book, author

@app.route('/books')
def get_all():
    return render_template('index.html')