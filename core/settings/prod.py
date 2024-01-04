from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_USER_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}

# 'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'NEW_YEAR',
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_USER_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT')
#     }