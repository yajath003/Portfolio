import os

 # Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SITE_NAME = 'Portfolio'
IMAGES_PATH = os.path.join(basedir, 'static/images/uploads')
CREATOR_HASHED_PASSWORD = 'pbkdf2:sha256:260000$OQx8p0tyvanfpBn9$d05d320c4cb39e458556ca7c568b10ee4464a406683da95750c958de28c293c9'
SECRET_KEY = 'you-will-never-guess'

