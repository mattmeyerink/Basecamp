import flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'authentication.login'
moment = Moment()

def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)

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

    with app.app_context():
        db.create_all()

    return app
