from flask import Blueprint, jsonify, request, render_template

from project.api.models import Participante, Usuario
from project import db

from sqlalchemy import exc

login_blueprint = Blueprint(
     'login', __name__, template_folder='./templates',
     static_url_path='', static_folder='./static')


@login_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'estado': 'satisfactorio',
        'mensaje': 'pong!!!'
    })


@login_blueprint.route('/users/u', methods=['GET', 'POST'])
def inicio():
    return render_template('index.html')


@login_blueprint.route('/users/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        usuario = request.form['user']

    return render_template('principal.html', usuario=usuario)


@login_blueprint.route('/users/crearjugador', methods=['GET', 'POST'])
def crearjugador():
    post_data = request.get_json()
    response_object = {
        'estado': 'fallo',
        'mensaje': 'Datos no validos.'
    }
    if not post_data:
        return jsonify(response_object), 400
    nombre = post_data.get('nombre')
    apellido = post_data.get('apellido')
    email = post_data.get('email')
    celular = post_data.get('celular')
    fechanacimiento = post_data.get('fechanacimiento')
    sexo = post_data.get('sexo')
    usuario =  post_data.get('usuario')
    clave =  post_data.get('clave')

    try:
        jugador = Participante.query.filter_by(email=email).first()
        if not jugador:
            jugadorcreate = Participante(
             nombre=nombre,
             apellido=apellido,
             email=email,
             celular=celular,
             fechanacimiento=fechanacimiento,
             sexo=sexo)
            db.session.add(jugadorcreate)
            db.session.commit()
            idjugador = jugadorcreate.id
            db.session.add(Usuario(
                 usuario=usuario,
                 clave=clave,
                 idparticipante=idjugador))
            db.session.commit()
            response_object['estado'] = 'satisfactorio'
            response_object['mensaje'] = f'{email} ha sido agregado!'
            return jsonify(response_object), 201
        else:
            response_object['mensaje'] = 'Disculpe. Este email ya existe.'
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400


@login_blueprint.route('/users/jugadores/<jugador_id>', methods=['GET'])
def get_single_jugador(jugador_id):
    """Obteniendo detalles de un unico usuario"""
    response_object = {
        'estado': 'fallo',
        'mensaje': 'jugador no existe'
    }

    try:
        jugador = Participante.query.filter_by(id=int(jugador_id)).first()
        if not jugador:
            return jsonify(response_object), 404
        else:
            response_object = {
                'estado': 'satisfactorio',
                'data': {
                    'id': jugador.id,
                    'nombre': jugador.nombre,
                    'apellido': jugador.apellido,
                    'email': jugador.email,
                    'celular': jugador.celular,
                    'nivel': jugador.nivel,
                    'fechanacimiento': jugador.fechanacimiento,
                    'sexo': jugador.sexo,
                    'estado': jugador.estado
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@login_blueprint.route('/users/crearcuenta', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        celular = request.form['celular']
        fechanacimiento = str(request.form['fechanacimiento'])
        sexo = int(request.form['sexo'])
        usuario = request.form['usuario']
        clave = request.form['clave']
       
        jugadorcreate = Participante(
             nombre=nombre,
             apellido=apellido,
             email=email,
             celular=celular,
             fechanacimiento=fechanacimiento,
             sexo=sexo)
        db.session.add(jugadorcreate)
        db.session.commit()
        idjugador = jugadorcreate.id
        db.session.add(Usuario(
             usuario=usuario,
             clave=clave,
             idparticipante=idjugador))
        db.session.commit()
    
    participantes = Participante.query.all()
    return render_template(
         'index.html',
         participantes=participantes)


@login_blueprint.route('/users/jugadores', methods=['GET'])
def get_all_jugadores():
    """Get all users"""
    response_object = {
        'estado': 'satisfactorio',
        'data': {
            'jugadores':
            [jugadores.to_json() for jugadores in Participante.query.all()]
        }
    }
    return jsonify(response_object), 200
