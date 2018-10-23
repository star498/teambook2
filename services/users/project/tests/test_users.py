import json
import unittest
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user

<<<<<<< HEAD

=======
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
class TestUserService(BaseTestCase):
    """Tests para el servicio Users."""
    def test_users(self):
        """comprobado que la ruta /ping funcione correctamente."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!!!', data['mensaje'])
        self.assertIn('satisfecho', data['estado'])
<<<<<<< HEAD

=======
    
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
    def test_add_user(self):
        """Asegurese de que se pueda agregar un nuevo usuario a la db."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'abel',
                    'email': 'abel.huanca@upeu.edu.pe'
<<<<<<< HEAD
                }), content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn(
                'abel.huanca@upeu.edu.pe a sido agregado',
                data['mensaje']
                )
            self.assertIn('satisfecho', data['estado'])

    def test_add_user_invalid_json(self):
        """Asegurando de que se lance un error
         cuando el objeto JSON esta vacío."""
=======
                }),content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('abel.huanca@upeu.edu.pe a sido agregado', data['mensaje'])
            self.assertIn('satisfecho', data['estado'])

    def test_add_user_invalid_json(self):
        """Asegurando de que se lance un error cuando el objeto JSON esta vacío."""
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Carga invalida', data['mensaje'])
            self.assertIn('fallo', data['estado'])

    def test_add_user_invalid_json_keys(self):
        """
<<<<<<< HEAD
        Asegurando que se produce un error si el objeto JSON no tiene
         una clave de nombre de usuario."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'email': 'abel.huanca@upeu.edu.pe'}),
                content_type='application/json'
=======
        Asegurando que se produce un error si el objeto JSON no tiene una clave de nombre de usuario.
        """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'email':'abel.huanca@upeu.edu.pe'}),
                content_type = 'application/json'
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Carga invalida.', data['mensaje'])
            self.assertIn('fallo', data['estado'])

    def test_add_user_duplicate_email(self):
        """Asegurando que se produce un error si el email ya existe."""
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
<<<<<<< HEAD
                    'username': 'abel',
=======
                    'username':'abel',
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
                    'email': 'abel.huanca@upeu.edu.pe'
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'abel',
                    'email': 'abel.huanca@upeu.edu.pe'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                'Disculpe, ese email ya existe.', data['mensaje'])
            self.assertIn('fallo', data['estado'])
<<<<<<< HEAD

=======
    
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
    def test_single_user(self):
        """Asegurando que el usuario único se comporte correctamente."""
        user = add_user('abel', 'abel.huanca@upeu.edu.pe')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('abel', data['data']['username'])
            self.assertIn('abel.huanca@upeu.edu.pe', data['data']['email'])
            self.assertIn('satisfactorio', data['estado'])

    def test_all_users(self):
        """Asegurando obtener todos los usuarios correctamente."""
        add_user('abel', 'abel.huanca@upeu.edu.pe')
        add_user('fredy', 'abelthf@gmail.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('abel', data['data']['users'][0]['username'])
<<<<<<< HEAD
            self.assertIn(
                'abel.huanca@upeu.edu.pe',
                data['data']['users'][0]['email']
                )
            self.assertIn(
                'fredy',
                data['data']['users'][1]['username']
                )
            self.assertIn(
                'abelthf@gmail.com',
                data['data']['users'][1]['email']
                )
            self.assertIn('satisfecho', data['estado'])

    def test_single_user_no_id(self):
        """asegurese de que se arroje
        un error si no se proporciona identificacion"""
        with self.client:
            response = self.client.get(
                '/users/blah'
                )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
=======
            self.assertIn('abel.huanca@upeu.edu.pe', data['data']['users'][0]['email'])
            self.assertIn('fredy', data['data']['users'][1]['username'])
            self.assertIn('abelthf@gmail.com', data['data']['users'][1]['email'])
            self.assertIn('satisfecho', data['estado'])
    
    def test_single_user_no_id(self):
        """asegurese de que se arroje un error si no se proporciona identificacion"""
        with self.client:
            response =self.client.get('/users/blah')
            data= json.loads(response.data.decode())
            self.assertEqual(response.status_code,404)
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
            self.assertIn("Usuario no existe", data['mensaje'])
            self.assertIn("fallo", data['estado'])

    def test_single_user_incorrect_id(self):
<<<<<<< HEAD
        """asegurese de que sea rroje un error
        si la identificacion no existe."""
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("Usuario no existe", data['mensaje'])
            self.assertIn("fallo", data['estado'])

    def test_main_no_users(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All Users', response.data)
        self.assertIn(b'<p>NO HAY USUARIOS!</p>', response.data)

    def test_main_with_users(self):

        add_user('sol', 'solmamani@upeu.edu.pe')
        add_user('igor', 'igorchipana@upeu.edu.pe')
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Users', response.data)
            self.assertNotIn(b'<p>NO HAY USUARIOS!</p>', response.data)
            self.assertIn(b'igor', response.data)
            self.assertIn(b'sol', response.data)

    def test_main_add_user(self):

        with self.client:
            response = self.client.post(
                '/', data=dict(
                    username='igor',
                    email='igorchipana@upeu.edu.pe'
                    ),
                follow_redirects=True
                )

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Users', response.data)
            self.assertNotIn(b'<p>NO HAY USUARIOS!</p>', response.data)
            self.assertIn(b'igor', response.data)


if __name__ == '__main__':
    unittest.main()
=======
        """asegurese de que sea rroje un error si la identificacion no existe."""
        with self.client:
            response= self.client.get('/users/999')
            data= json.loads(response.data.decode())
            self.assertEqual(response.status_code,404)
            self.assertIn("Usuario no existe", data['mensaje'])
            self.assertIn("fallo", data['estado'])


if __name__ == '__main__':
    unittest.main()
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
