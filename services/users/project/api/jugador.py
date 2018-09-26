from flask import Blueprint, jsonify, request
from flask import render_template
from sqlalchemy import exc
from project.api.models import Jugador
from project import db
from project import templates

jugador_blueprint=Blueprint('jugador', __name__)

@jugador_blueprint.route('/jugador/ping', methods=['GET'])
def ping_pong():
	return render_template('jugador/index.html')