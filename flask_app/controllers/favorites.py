from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import book, author

@app.route('/fav_submit/invisible/post', methods=['post'])
def make_association_with_faving:
pass