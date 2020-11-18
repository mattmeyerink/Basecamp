import flask
from main import main_bp
from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main_bp)
