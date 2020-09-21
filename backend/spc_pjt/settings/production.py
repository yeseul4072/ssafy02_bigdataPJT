from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

secret_file = os.path.join(BASE_DIR, 'secrets-prod.json')
secrets = Secrets(secret_file)

DATABASES = secrets.get_secret('DATABASES')