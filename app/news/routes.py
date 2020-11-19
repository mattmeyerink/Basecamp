import flask
from . import news_bp


@news_bp.route("/")
def show_newsfeed():
    context = {

    }
    return flask.render_template("news.html", **context)
