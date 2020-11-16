"""
use a class to store configuration variables
"""

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # Secret key configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Flask-SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    # Email configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    POSTS_PER_PAGE = 25

    GOOGLE_LOGIN_CLIENT_ID = "377880173751-ohc3i3v3or0qf3n2d0a9kr19jdh5gqqc.apps.googleusercontent.com"
    GOOGLE_LOGIN_CLIENT_SECRET = "dDzSWX_PokdRDYCUMQ8tWj_V"
    GOOGLE_API_SCOPE = 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email'
    GOOGLE_OAUTH2_URL = 'https://accounts.google.com/o/oauth2/'
    GOOGLE_API_URL = 'https://www.googleapis.com/oauth2/v1/'
    GOOGLE_REDIRECT_URI = 'https://localhost:5000/gCallback'
    GOOGLE_USERINFO_ENDPOINT = 'https://openidconnect.googleapis.com/v1/userinfo'

    OAUTH_CREDENTIALS={
            'google': {
                'id': GOOGLE_LOGIN_CLIENT_ID,
                'secret': GOOGLE_LOGIN_CLIENT_SECRET
            },

            'facebook': {
                'id': '1021466161623333',
                'secret': '425f7caab42c674af2a2e2a05ef67559'
            }
    }
