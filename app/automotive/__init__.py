from flask import Blueprint

automotive = Blueprint('automotive',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       url_prefix='/automotive')

from . import routes
