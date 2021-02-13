from stock_django.settings.shared_settings import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
  '0.0.0.0',
  'localhost',
]

SECRET_KEY = os.environ['SECRET_KEY']