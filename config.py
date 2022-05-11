
import os

class Config:
    UPLOADED_PHOTOS_DEST = os.environ.get('UPLOADED_PHOTOS_DEST')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://","ql://",1)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'my_key'
    UPLOADED_PHOTOS_DEST='/app/static/photos'

    EMAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:qwertyip@localhost/pitch_test'


class ProdConfig(Config):
    pass

class DevConfig(Config):
DEBUG = True


    

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
}