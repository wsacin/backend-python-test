DATABASE = '/tmp/alayatodo.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
PASSWORD_HASH_METHOD = 'pbkdf2:sha1'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
