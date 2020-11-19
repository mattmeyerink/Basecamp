import flask
from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)

from main import main_bp
app.register_blueprint(main_bp)

from news import news_bp
app.register_blueprint(news_bp)

from sports import sports_bp
app.register_blueprint(sports_bp)

from weather import weather_bp
app.register_blueprint(weather_bp)

from account import account_bp
app.register_blueprint(account_bp)
