from pathlib import Path
from decouple import config as env


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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