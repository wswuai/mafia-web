class Config(object):
    ELASTICSEARCH_SERVER = ['192.168.6.24']
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    DEBUG = True

