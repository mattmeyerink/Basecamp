import flask


weather_bp = flask.Blueprint('weather', __name__, url_prefix='/weather',
                             template_folder='weather_templates')

from . import routes
