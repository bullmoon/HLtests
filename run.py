#from flask import Flask, Blueprint, render_template
from app import create_app

app = create_app()

#main = Blueprint('main', __name__)

#@main.route('/')
#def index():
#    return "<h1>Hello World!</h1>"


#app = Flask(__name__)
#app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
