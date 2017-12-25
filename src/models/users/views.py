from flask import Blueprint

__author__ = "Prajesh Ananthan"

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login')
def login_user():
    pass


@user_blueprint.route('/register')
def register_user():
    pass


@user_blueprint.route('/alerts')
def user_alerts():
    pass


@user_blueprint.route('/logout')
def logout_user():
    pass


@user_blueprint.route('/check_alert/<string:user_id>')
def check_user_alerts(user_id):
    pass
