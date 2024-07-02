from flask import Blueprint

main = Blueprint('main', __name__,
                 template_folder='templates',
                 static_folder='static',
                 url_prefix='/')

from . import routes
