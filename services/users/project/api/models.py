<<<<<<< HEAD


from project import db


class User(db.Model):

    __tablename__ = 'users'
=======
from sqlalchemy.sql import func

from project import db

class User(db.Model):

    __tablename__ =  'users'
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
<<<<<<< HEAD

=======
    
    
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
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

<<<<<<< HEAD

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
=======
class Jugador(db.Model):

    __tablename__='jugador'

    idjugador=db.Column(db.Integer,primary_key=True, autoincrement= True)
    nombre= db.Column(db.String(100), nullable=False)
    apellido =db.Column(db.String(100), nullable=False)
    usuario= db.Column(db.String(20), nullable=True)
    clave= db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(128), nullable=True)
    celular = db.Column(db.String(9), nullable=True)
    nivel = db.Column(db.Integer, default= 0, nullable=True)
    fechanacimiento= db.Column(db.Date(), nullable=True)
    estado= db.Column(db.Boolean(),default=True, nullable=False)
    tipocuenta= db.Column(db.String(50), nullable=False)
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493

    def to_json(self):
        return {
            'idjugador': self.idjugador,
            'nombre': self.username,
            'apellido': self.apellido,
            'usuario': self.usuario,
<<<<<<< HEAD
            'clave': self.clave,
            'email': self.email,
=======
            'clave':self.clave,
            'email' : self.email,
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
            'celular': self.celular,
            'nivel': self.nivel,
            'fnacimiento': self.fechanacimiento,
            'estado': self.estado,
            'tipocuenta': self.tipocuenta
        }
<<<<<<< HEAD
=======

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




>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
