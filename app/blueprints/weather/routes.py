import flask
from . import weather_bp


@weather_bp.route("/")
def show_weather():
    context = {

    }
    return flask.render_template("weather.html", **context)