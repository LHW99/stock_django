from stock_django.settings.shared_settings import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
  '0.0.0.0',
  'localhost',
  'django-stocks.herokuapp.com'
]

SECRET_KEY = os.environ['SECRET_KEY']

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)