<<<<<<< HEAD
from flask import Blueprint, jsonify, request, render_template
=======
from flask import Blueprint, jsonify, request
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493

from sqlalchemy import exc
from project.api.models import User
from project import db


<<<<<<< HEAD
users_blueprint = Blueprint('users', __name__, template_folder='./templates')


@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        db.session.add(User(username=username, email=email))
        db.session.commit()
    users = User.query.all()
    return render_template('index.html', users=users)

=======
users_blueprint=Blueprint('users', __name__)
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493

@users_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'estado': 'satisfecho',
        'mensaje': 'pong!!!'
<<<<<<< HEAD
        })
=======
})
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493


@users_blueprint.route('/users', methods=['POST'])
def add_user():
<<<<<<< HEAD
    post_data = request.get_json()
    response_object = {
        'estado': 'fallo',
        'mensaje': 'Carga invalida.'
    }
    if not post_data:
        return jsonify(response_object), 400
    username = post_data.get('username')
    email = post_data.get('email')
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email))
            db.session.commit()
            response_object['estado'] = 'satisfecho'
            response_object['mensaje'] = f'{email} a sido agregado'
            return jsonify(response_object), 201
        else:
            response_object['mensaje'] = 'Disculpe,ese email ya existe.'
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400

=======
	post_data= request.get_json()
	response_object = {
		'estado':'fallo',
		'mensaje': 'Carga invalida.'
	}
	if not post_data:
		return jsonify(response_object),400
	username= post_data.get('username')
	email=post_data.get('email')
	try:
		user= User.query.filter_by(email=email).first()
		if not user:
			db.session.add(User(username=username,email=email))
			db.session.commit()
			response_object['estado']='satisfecho'
			response_object['mensaje']=f'{email} a sido agregado'
			return jsonify(response_object),201
		else:
			response_object['mensaje']='Disculpe, ese email ya existe.'
			return jsonify(response_object),400
	except exc.IntegrityError as e:
		db.session.rollback()
		return jsonify(response_object),400
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493

@users_blueprint.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    """Obteniendo detalles del usuario único"""
    response_object = {
        'estado': 'fallo',
        'mensaje': 'Usuario no existe'
    }
    try:
        user = User.query.filter_by(id=int(user_id)).first()
<<<<<<< HEAD
        if not user:
=======
        if  not user:
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
            return jsonify(response_object), 404
        else:
            response_object = {
                'estado': 'satisfactorio',
                'data': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'active': user.active
                    }
            }
            return jsonify(response_object), 200
    except ValueError:
<<<<<<< HEAD
        return jsonify(response_object), 404
=======
    	return jsonify(response_object), 404
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493


@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    """Obteniendo todos los usuarios"""
    response_object = {
        'estado': 'satisfecho',
        'data': {
            'users': [user.to_json() for user in User.query.all()]
        }
    }
<<<<<<< HEAD
    return jsonify(response_object), 200
=======
    return jsonify(response_object), 200
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
