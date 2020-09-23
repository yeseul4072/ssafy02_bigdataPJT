from .base import *


DEBUG = True

ALLOWED_HOSTS = []

secret_file = os.path.join(BASE_DIR, 'secrets-local.json')
secrets = Secrets(secret_file)

DATABASES = secrets.get_secret('DATABASES')