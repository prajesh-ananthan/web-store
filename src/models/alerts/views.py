from flask import Blueprint

__author__ = "Prajesh Ananthan"

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/new', methods=['POST'])
def create_alert():
    pass


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
    pass


@alert_blueprint.route('/alert/<string:alert_id>')
def get_alert_page(alert_id):
    pass


@alert_blueprint.route('/user/alert/<string:alert_id>')
def get_alerts_for_user(alert_id):
    pass
