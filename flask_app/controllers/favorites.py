from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import book, author

# ! INVISIBLE (CREATE)
@app.route('/favorite', methods=['POST'])
def fav_a_book(data):
    return redirect(f'/author/{request.form["author_id"]}')
