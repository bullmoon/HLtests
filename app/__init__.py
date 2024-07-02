from flask import Flask

def create_app():
    app = Flask(__name__)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    #from .automotive import automotive as automotive_blueprint
    #app.register_blueprint(automotive_blueprint, url_prefix='/automotive')

    return app
