from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('base.html')
    #return "<h1>Index Main</h1>"

@main.route('/about')
def about():
    #return render_template('about.html')
    return "<h1>About Main page</h1>"