from sqlalchemy.sql import func

from project import db

class User(db.Model):

    __tablename__ =  'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)


    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'active': self.active
        }

    def __init__(self, username, email):
        self.username = username
        self.email = email



class Jugador(db.Model):

    __tablename__ = 'jugador'

    idjugador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(20), nullable=True)
    clave = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(128), nullable=True)
    celular = db.Column(db.String(9), nullable=True)
    nivel = db.Column(db.Integer, default=0, nullable=True)
    fechanacimiento = db.Column(db.Date(), nullable=True)
    estado = db.Column(db.Boolean(), default=True, nullable=False)
    tipocuenta = db.Column(db.String(50), nullable=False)

    def to_json(self):
        return {
            'idjugador': self.idjugador,
            'nombre': self.username,
            'apellido': self.apellido,
            'usuario': self.usuario,
            'clave': self.clave,
            'email': self.email,
            'celular': self.celular,
            'nivel': self.nivel,
            'fnacimiento': self.fechanacimiento,
            'estado': self.estado,
            'tipocuenta': self.tipocuenta
        }

    def __init__(self, nombre, apellido, usuario, clave, celular, fechanacimiento, tipocuenta):
        self.nombre= nombre
        self.apellido = apellido
        self.usuario= usuario
        self.clave= clave
        self.celular= celular
        self.fechanacimiento= fechanacimiento
        self.tipocuenta= tipocuenta

    def __init__(self, nombre, apellido, email , tipocuenta, celular):
        self.nombre= nombre
        self.apellido = apellido
        self.email=email
        self.tipocuenta= tipocuenta
        self.celular = celular


class Cuenta(db.Model):

    __tablename__ =  'TBK_CUENTA'

    id_cuenta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario= db.Column(db.String(128), nullable=False)
    clave = db.Column(db.String(128), nullable=False)
    estado = db.Column(db.Boolean(), default=True, nullable=False)
    tipo_cuenta = db.Column(db.Integer,  nullable=False)


    def to_json(self):
        return {
            'id_cuenta': self.id_cuenta,
            'usuario': self.usuario,
            'clave': self.clave,
            'estado': self.estado,
            'tipo_cuenta': self.tipo_cuenta        }


