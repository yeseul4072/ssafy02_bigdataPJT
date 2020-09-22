from .base import *
import os
from datetime import date


DEBUG = True

ALLOWED_HOSTS = ['*']

secret_file = os.path.join(BASE_DIR, 'secrets-dev.json')
secrets = Secrets(secret_file)

DATABASES = secrets.get_secret('DATABASES')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
    },
    'handlers': {
        'file': {  
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.join(os.path.dirname(BASE_DIR), 'django-dev-log'), f'{date.today().isoformat()}-django.log'),  
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],  
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}