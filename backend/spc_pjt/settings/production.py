from .base import *
import os
from datetime import date
import logging
import requests


DEBUG = False

ALLOWED_HOSTS = ['*']

secret_file = os.path.join(BASE_DIR, 'secrets-prod.json')
secrets = Secrets(secret_file)

DATABASES = secrets.get_secret('DATABASES')

class MattermostRequestsHandler(logging.Handler):
        
    def emit(self, record):
        log_entry = self.format(record)
        return requests.post(
            url=secrets.get_secret('MATTERMOST_URL'),
            data=log_entry.encode('utf-8'),
            headers={'Content-type': 'application/json'}
        )

log_file_path = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'django-prod-log')
log_file_name = f'django-prod.log.{date.today().isoformat()}'

LOGGING['handlers'] = {
        'file': {  
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(log_file_path, log_file_name),
            'when': 'midnight',
            'backupCount': 100,
            'formatter': 'standard',
        },
        'http': {
            'class': 'spc_pjt.settings.production.MattermostRequestsHandler',
            'formatter': 'json'
        }
    }