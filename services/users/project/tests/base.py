<<<<<<< HEAD
=======

>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
from flask_testing import TestCase

from project import create_app, db

app = create_app()

<<<<<<< HEAD

class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object(
                'project.config.TestingConfig'
                )
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
=======
class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app
    
    def setUp(self):
        db.create_all()
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
