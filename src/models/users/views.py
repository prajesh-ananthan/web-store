from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect

import src.models.users.errors as UserErrors
from src.models.users.user import User

__author__ = "Prajesh Ananthan"

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        # Check the login is valid
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("user/login.html")  # Send the user an error when the login fails


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("user/register.html")  # Send the user an error when the login fails


@user_blueprint.route('/alerts')
def user_alerts():
    return "You are now in the alerts page"


@user_blueprint.route('/logout')
def logout_user():
    pass


@user_blueprint.route('/check_alert/<string:user_id>')
def check_user_alerts(user_id):
    pass
