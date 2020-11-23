import flask
import requests
from flask_login import login_user, logout_user, current_user
from . import auth_bp
from app import client, Config
from .models import User



@auth_bp.route("/login")
def login():
    """Route to display login page template."""
    return flask.render_template("login.html")

@auth_bp.route("/google-login")
def google_login():
    """Route to initiate google login."""
    # Find what URL to use for google login
    google_provider_cfg = requests.get(Config.GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Construct request for information from google login to callback function
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=flask.request.base_url + "/callback",
        scope=["openid", "email", "profile"]
    )
    return flask.redirect(request_uri)

@auth_bp.route("/google-login/callback")
def google_callback():
    """Callback for Google Authentication."""
    # Recieve google authorization code
    code = request.args.get("code")

    # Find the URL to ask for the user info tokens
    google_provider_cfg = requests.get(Config.GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare the request for tokens
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=flask.request.base_url,
        code=code
    )

    # Send the request for tokens with appropriate keys
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(Config.GOOGLE_CLIENT_ID, Config.GOOGLE_CLIENT_SECRET)
    )

    # Parse the recieved tokens
    client.parse_request_body_response(json)
    
    # Use tokens to find URL from Google that has profile information
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # Ensure that email was verified with google
    if userinfo_response.json().get("email_verified"):
        users_email = userinfo_response.json()["email"]
        users_picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "Failed to authenticate with Google"
                
    # If the user is not already in our db, add them
    user = User.query.filter_by(email=users_email).first()

    # If the users info was not already present in the local db add them.
    if not user_present:
        user = User()
        user.from_dict({"email": users_email, "given_name": users_name})

    login_user(user)

    return flask.redirect(flask.url_for("main.show_homepage"))