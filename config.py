
import os

class Config:
    UPLOADED_PHOTOS_DEST = os.environ.get('UPLOADED_PHOTOS_DEST')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:qwertyip@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'my_key'



class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}