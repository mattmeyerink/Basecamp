import flask
import requests
from . import auth_bp
from app import client
from flask_login import login_user, logout_user, current_user


@auth_bp.route("/login")
def login():
    """Route to display login page template."""
    return flask.render_template("login.html")

@auth_bp.route("/google-login")
def google_login():
    """Route to initiate google login."""
    # Find what URL to use for google login
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Construct request for information from google login to callback function
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"]
    )
    
    return flask.redirect(request_uri)
