"""Blueprint for the homescreen."""
import flask


main_bp = flask.Blueprint('main', __name__, template_folder="main_templates")

from . import routes
