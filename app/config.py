import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    PORT = int(os.environ.get("PORT", 8000))
    DEBUG_MODE = int(os.environ.get("DEBUG_MODE", 1))
    CSRF_ENABLED = True
    # SECRET_KEY = 'this-really-needs-to-be-changed'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
