"""Routing for the homepage."""
import flask
import requests
from flask_login import login_required
from . import main_bp


@main_bp.route("/")
def show_homepage():
    """Display route for the homepage."""
    # Gather quote data from quotes API
    response = requests.get("https://type.fit/api/quotes")
    data = response.json()
    
    motivational_quote = {
        "text": data[0]["text"],
        "author": data[0]["author"]
    }
    if motivational_quote["text"][-1] == ".":
        motivational_quote["text"] = motivational_quote["text"][:-1]

    context = {
        "message": "Hello world through the blueprint's template!",
        "motivational_quote": motivational_quote
    }
    return flask.render_template("homepage.html", **context)