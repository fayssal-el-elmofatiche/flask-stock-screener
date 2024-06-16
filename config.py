import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Used for example by Flask-WTF to generate CSRF tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # SQLAlchemy database URL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')