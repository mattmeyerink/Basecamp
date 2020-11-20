import flask
from . import account_bp


@account_bp.route("/")
def show_account():
    context = {

    }
    return flask.render_template("account.html", **context)