import os

class Config:
 
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Samfan01@localhost/blog'

class ProdConfig(Config):
    
    pass
class DevConfig(Config):
    DEBUG = True
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}