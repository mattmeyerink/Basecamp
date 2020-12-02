"""Routes for sports scores blueprint."""
import flask
from datetime import date
import requests
from . import sports_bp
from config import Config
from pprint import pprint


@sports_bp.route("/")
def show_sportsfeed():
    """Routing for page to display all of the scores."""
    # Determine the current date
    today = date.today()

    # Make the API call for todays games
    response = requests.get(f"https://api.sportradar.us/ncaamb/" +
                            f"trial/v7/en/games/{str(today.year)}/" +
                            f"{str(today.month)}/{str(today.day)}/" +
                            f"schedule.json?api_key={Config.SPORTRADAR_API_KEY}")
    game_data = response.json()
    pprint(game_data)

    scores = None
    context = {
        "scores": scores
    }
    return flask.render_template("sports.html", **context)