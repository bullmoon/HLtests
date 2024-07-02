from flask import Flask, render_template, request, redirect, url_for

def create_app():
    app = Flask(__name__)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app