import flask


main_bp = flask.Blueprint('main', __name__)

@main_bp.route("/")
def show_homepage():
    return "Homepage from blueprint new"
