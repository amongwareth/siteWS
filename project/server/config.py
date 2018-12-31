# project/server/config.py
from env_variables import FLASK_SECRET_KEY
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    APP_NAME = 'WattStrat'
    BCRYPT_LOG_ROUNDS = 4
    DEBUG_TB_ENABLED = False
    SECRET_KEY = FLASK_SECRET_KEY
    WTF_CSRF_ENABLED = False

class ProductionConfig(BaseConfig):
    """Production configuration."""
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
