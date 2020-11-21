import flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient
from config import Config

# Create instances of db and db migration
db = SQLAlchemy()
migrate = Migrate()

# Initialize settings for login
login = LoginManager()
login.login_view = 'authentication.login'
client = WebApplicationClient(Config.GOOGLE_CLIENT_ID)

def create_app():
    """Creates the flask application."""
    # Initialize the flask app
    app = flask.Flask(__name__)

    # Retrieve configuration settings 
    app.config.from_object(Config)

    # Initialize the db and db migration 
    db.init_app(app)
    migrate.init_app(app, db)

    # Set up login infastructure
    login.init_app(app)

    # Pull in all of the blueprints 
    from blueprints.main import main_bp
    app.register_blueprint(main_bp)

    from blueprints.news import news_bp
    app.register_blueprint(news_bp)

    from blueprints.sports import sports_bp
    app.register_blueprint(sports_bp)

    from blueprints.weather import weather_bp
    app.register_blueprint(weather_bp)

    from blueprints.account import account_bp
    app.register_blueprint(account_bp)

    from blueprints.authorization import auth_bp
    app.register_blueprint(auth_bp)

    # Create the db
    with app.app_context():
        db.create_all()

    return app
