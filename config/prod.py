"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 08/07/2019

"""
from .default import *
import os

SECRET_KEY = os.getenv('SECRET_KEY_ENV')

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@host:port/db_name'
