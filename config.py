import os

class Config:
    # Used for example by Flask-WTF to generate CSRF tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'