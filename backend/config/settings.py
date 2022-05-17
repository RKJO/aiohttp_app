import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
PACKAGE_NAME = 'aiohttpdemo_blog'

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DATABASE_URL = os.environ.get('DATABASE_URL')