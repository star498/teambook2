
import unittest
from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Participante

import coverage

#configuracion de coverage
COV= coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
        ]

    )
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Ejecuta las pruebas sin cobertura de codigo"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def seed_db():

    db.session.add(Participante(nombre='estrella', apellido='barrientos', email='estrella@upeu.edu.pe', celular='celular', fechanacimiento='12-15-18' ,sexo=1))
    db.session.commit()

@cli.command()
def cov():

    tests= unittest.TestLoader().discover('project/tests')
    result= unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Resumen de covertura:")
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


if __name__=='__main__':
    cli()
