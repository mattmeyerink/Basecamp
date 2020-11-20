import flask
import requests
from . import auth_bp
from app import client


@auth_bp.route("/login")
def login():
    """Route to login through Google."""
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
