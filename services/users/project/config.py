import os
<<<<<<< HEAD

=======
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493

class BaseConfig:
    """Configuracion base del proyecto"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_secret_key'
<<<<<<< HEAD

=======
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493

class DevelopmentConfig(BaseConfig):
    """Configuracion de desarrollo"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
<<<<<<< HEAD

=======
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493

class TestingConfig(BaseConfig):
    """Configuracion de pruebas"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

<<<<<<< HEAD

=======
>>>>>>> 2abc7d3422678745f55e81dd56c9a9f8680e3493
class ProductionConfig(BaseConfig):
    """Configuracion de produccion"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
