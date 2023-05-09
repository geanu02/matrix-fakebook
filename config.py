import os 

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.environ.get('ELEPHANT_URL')