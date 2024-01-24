from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dbapphapkido',
#         'USER': 'ubeimar',
#         'PASSWORD': 'abril2022',
#         'HOST': 'localhost',
#         'PORT': '5433'
#     }
# }

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = 'static/'
