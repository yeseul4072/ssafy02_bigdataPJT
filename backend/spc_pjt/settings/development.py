from .base import *
import os
from datetime import date


DEBUG = True

ALLOWED_HOSTS = ['*']

secret_file = os.path.join(BASE_DIR, 'secrets-dev.json')
secrets = Secrets(secret_file)

DATABASES = secrets.get_secret('DATABASES')

log_file_path = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'django-dev-log')
log_file_name = f'{date.today().isoformat()}-django.log'

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
            'filename': os.path.join(log_file_path, log_file_name),  
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