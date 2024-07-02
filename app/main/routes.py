from flask import render_template, url_for
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return "<h1>About Main page</h1>"
