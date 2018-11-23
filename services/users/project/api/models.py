from project import db


class User(db.Model):

    __tablename__ = 'users'

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


class Participante(db.Model):

    __tablename__ = 'participante'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(128), nullable=True)
    celular = db.Column(db.String(9), nullable=True)
    nivel = db.Column(db.Integer, default=0, nullable=True)
    fechanacimiento = db.Column(db.String(20), nullable=True)
    estado = db.Column(db.Boolean(), default=True, nullable=True)
    sexo = db.Column(db.Integer, default=0, nullable=True)

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'celular': self.celular,
            'nivel': self.nivel,
            'fechanacimiento': self.fechanacimiento,
            'estado': self.estado,
            'sexo': self.sexo,
        }

    def __init__(self,
                 nombre,
                 apellido,
                 email,
                 celular,
                 fechanacimiento,
                 sexo
                 ):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular
        self.fechanacimiento = fechanacimiento
        self.sexo = sexo


class Usuario(db.Model):

    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(128), nullable=False)
    clave = db.Column(db.String(128), nullable=False)
    estado = db.Column(db.Boolean(), default=True, nullable=False)
    tipocuenta = db.Column(db.Integer, default=1, nullable=False)
    idparticipante = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'clave': self.clave,
            'estado': self.estado,
            'tipocuenta': self.tipocuenta,
            'idparticipante': self.idparticipante
            }

    def __init__(self,
                 usuario,
                 clave,
                 idparticipante
                 ):
        self.usuario = usuario
        self.clave = clave
        self.idparticipante = idparticipante
