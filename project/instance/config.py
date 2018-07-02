import os


PROJECT_DIR = os.path.abspath(__file__).rsplit('/',3)[0]


HOST = os.getenv('APP_HOST', '0.0.0.0')
PORT = os.getenv('APP_PORT', '8000')



class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET', 'This is my secret')

    DB = {
        'engine': 'mssql+pyodbc',
        'user': os.getenv('DB_USER'),
        'pass': os.getenv('DB_PASS'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'name': os.getenv('DB_NAME'),
        'driver': 'ODBC+Driver+17+for+SQL+Server'
    }

    SQLALCHEMY_DATABASE_URI = (
        '%(engine)s://%(user)s:%(pass)s@%(host)s:%(port)s/%(name)s?driver=%(driver)s'
    ) % DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + PROJECT_DIR + '/test_db/polls.db'
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
