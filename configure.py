import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET = os.environ.get('SECRET_KEY') or 'You will never guess!!'
    SQLALCHEMY_COMMIT_ON_TEAR_DOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'dev-data.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'test-data.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'prod-data.sqlite')

class HerokuConfig(ProductionConfig):
    @classmethod
    def init_app(app):
        ProductionConfig.init_app(app)
        

config = {
    'test': TestingConfig,
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'heroku': HerokuConfig
}
