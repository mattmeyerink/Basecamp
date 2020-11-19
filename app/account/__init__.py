import flask


account_bp = flask.Blueprint('account', __name__, url_prefix='/account',
                              template_folder='account_templates')

from . import routes
