import flask
from . import sports_bp


@sports_bp.route("/")
def show_sportsfeed():
    context = {

    }
    return flask.render_template("sports.html", **context)