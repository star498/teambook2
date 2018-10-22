from flask import Blueprint
from flask import render_template

jugador_blueprint = Blueprint('jugador', __name__)


@jugador_blueprint.route('/jugador/ping', methods=['GET'])
def ping_pong():
    return render_template('jugador/index.html')
