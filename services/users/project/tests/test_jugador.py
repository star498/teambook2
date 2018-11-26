from project import db
from project.api.models import Participante

import json

from project.tests.base import BaseTestCase


def add_participante(nombre, apellido, email, celular, fechanacimiento, sexo):
    participante = Participante(
         nombre=nombre,
         apellido=apellido,
         email=email,
         celular=celular,
         fechanacimiento=fechanacimiento,
         sexo=sexo)
    db.session.add(participante)
    db.session.commit()
    return participante


class TestJugadorService(BaseTestCase):
    """Prueba para el servicio jugador."""
    def test_jugador(self):
        """Asegurando que la ruta /ping se comporta correctamente."""
        response = self.client.get('/users/login/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!!!', data['mensaje'])
        self.assertIn('satisfactorio', data['estado'])

    def test_add_jugador(self):
        """Asegurando de que se pueda agregar un nuevo usuario a la base de
        datos."""
        with self.client:
            response = self.client.post(
                '/users/crearjugador',
                data=json.dumps({
                    'nombre': 'estrella',
                    'apellido': 'barrientos',
                    'email': 'estrella@upeu.edu.pe',
                    'celular': 'celular',
                    'fechanacimiento': '12-15-18',
                    'sexo': 1
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn(
                    'estrella@upeu.edu.pe ha sido agregado!',
                    data['mensaje']
                    )
            self.assertIn('satisfactorio', data['estado'])

    def test_add_jugador_invalid_json(self):
        """Asegurando de que se arroje un error si el objeto json esta
        vacio."""
        with self.client:
            response = self.client.post(
                '/users/crearjugador',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Datos no validos.', data['mensaje'])
            self.assertIn('fallo', data['estado'])

    def test_single_jugador(self):
        """Asegurando de que el usuario individual se comporte
        correctamente."""
        jugador = add_participante(
            'sol123',
            'apellido',
            'sol@upeu.edu.pe',
            '54654654',
            '12-12-15', 1)
        with self.client:
            response = self.client.get(f'/users/jugadores/{jugador.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('sol', data['data']['nombre'])
            self.assertIn('sol@upeu.edu.pe', data['data']['email'])
            self.assertIn('satisfactorio', data['estado'])

    def test_add_jugador_duplicate_email(self):
        """Asegurando de que se produce un error si el correo electronico ya
        existe."""
        with self.client:
            self.client.post(
                '/crearjugador',
                data=json.dumps({
                    'nombre': 'estrella',
                    'apellido': 'barrientos',
                    'email': 'estrella@upeu.edu.pe',
                    'celular': 'celular',
                    'fechanacimiento': '12-15-18',
                    'sexo': 1
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/users/crearjugador',
                data=json.dumps({
                    'nombre': 'estrella',
                    'apellido': 'barrientos',
                    'email': 'estrella@upeu.edu.pe',
                    'celular': 'celular',
                    'fechanacimiento': '12-15-18',
                    'sexo': 1
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                'Disculpe. Este email ya existe.', data['mensaje'])
            self.assertIn('fallo', data['estado'])

    def test_single_jugador_no_id(self):
        """Asegurando de que se lanze un error si no se proporciona un id."""
        with self.client:
            response = self.client.get('/users/jugadores/blash')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('jugador no existe', data['mensaje'])
            self.assertIn('fallo', data['estado'])

    def test_single_jugador_incorrect_id(self):
        """Asegurando de que se lanze un error si el id no existe."""
        with self.client:
            response = self.client.get('/users/jugadores/1')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('jugador no existe', data['mensaje'])
            self.assertIn('fallo', data['estado'])

    def test_add_user_invalid_json_keys(self):
        """
        Asegurando de que se produce un error si el objeto JSON no tiene
        un key de nombre de usuario.
        """
        with self.client:
            response = self.client.post(
                '/users/crearjugador',
                data=json.dumps({'email': 'estrella@upeu.edu.pe'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Datos no validos.', data['mensaje'])
            self.assertIn('fallo', data['estado'])

    def test_all_jugadores(self):
        """Asegurarse de que todos los usuarios se comporte correctamente."""
        add_participante(
             'sol123',
             'apellido',
             'sol@upeu.edu.pe',
             '54654654',
             '12-12-15',
             1)
        with self.client:
            response = self.client.get('/users/jugadores')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['jugadores']), 1)
            self.assertIn('sol123', data['data']['jugadores'][0]['nombre'])
            self.assertIn(
                'sol@upeu.edu.pe', data['data']['jugadores'][0]['email'])
            self.assertIn('satisfactorio', data['estado'])

