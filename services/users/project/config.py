
class BaseConfig:
    """Base congiruracion"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    pass

class TestingConfig(BaseConfig):
    """TEsting configuracion"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """production configuration"""
    pass

