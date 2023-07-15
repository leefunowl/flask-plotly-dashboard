import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
    
class Config(object):

    DEBUG = False
    TESTING = False
    
    ROUTES_PATHNAME_PREFIX = '/dashboard/'
    
    # DB_URL = os.environ.get('DB_URI')
    DB_URL = 'sqlite:///' + os.path.join(basedir, 'data/data.db') + '?check_same_thread=False'
    
    SECRET_KEY = os.environ.get('APP_SECRET_KEY')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_BINDS = {
        'dashboard': DB_URL,
        'auth':DB_URL,
    }

    RAW_TEST_DATA_DIR = os.path.join(basedir, 'data/raw-data')

    # SQLALCHEMY_ENGINE_OPTIONS = {'pool_size' : 100, 'pool_recycle' : 280}
    
    fig_font_size = 15
    
class ProductionConfig(Config):

    SECRET_KEY = os.environ.get('APP_SECRET_KEY')
    
class DevelopmentConfig(Config):

    DEBUG = True
    SECRET_KEY = 'dev'

class TestingConfig(Config):

    TESTING = True