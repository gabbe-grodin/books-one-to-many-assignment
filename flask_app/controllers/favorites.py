from flask import redirect, request
from flask_app import app
from flask_app.models import author, book



@app.route('/book/add/favorite', methods=['POST'])
def make_association_from_one_book():
    data = {
        "author_id": request.form['author'], # comes from name in form
        "book_id": request.form['book']}
    author.Author.add_a_favorite(data)
    return redirect(f"/book/{request.form['book']}")



@app.route('/author/add/favorite', methods=['POST'])
def make_association_from_one_author_page():
    data = {
        "author_id": request.form['author'], # comes from name in form
        "book_id": request.form['book']}
    print("*************DATA***********",data)
    author.Author.add_a_favorite(data)
    return redirect(f"/author/{request.form['author']}")