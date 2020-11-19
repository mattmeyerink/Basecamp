import flask


sports_bp = flask.Blueprint('sports', __name__, url_prefix='/sports',
                            template_folder='sports_templates')

from . import routes
