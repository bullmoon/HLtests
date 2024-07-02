from flask import render_template, url_for
from . import automotive

@automotive.route('/')
def index():
    return render_template('automotive/index.html')
    #return "<h1>Automotive Index Main</h1>"

@automotive.route('/2')
def index():
    return render_template('index.html')

@automotive.route('/about')
def about():
    return render_template('automotive/about.html')
    #return "<h1>About automotive page</h1>"