"""Blueprint for the newsfeed."""
import flask


news_bp = flask.Blueprint('news', __name__, url_prefix='/news', 
                          template_folder='news_templates')

from . import routes
