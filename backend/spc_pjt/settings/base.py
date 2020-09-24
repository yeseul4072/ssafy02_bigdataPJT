import os, json
from django.core.exceptions import ImproperlyConfigured


class Secrets:
    def __init__(self, secret_file):
        with open(secret_file) as f:
            self.secrets = json.loads(f.read())
    
    def get_secret(self, setting):
        try:
            return self.secrets.get(setting)
        except:
            error_msg = f'Set the {setting} environment variable'
            raise ImproperlyConfigured(error_msg)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

secret_file = os.path.join(BASE_DIR, 'secrets-base.json')
secrets = Secrets(secret_file)

SECRET_KEY = secrets.get_secret('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # registration

    # DRF
    'rest_framework',
    'rest_framework.authtoken',

    # rest-auth & allauth
    'rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount', # to fix deleting user issue
    'rest_auth.registration',

    # CORS
    'corsheaders',

    # swagger
    'drf_yasg',

    # my apps
    'accounts',
    'community',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spc_pjt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'spc_pjt.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'accounts.User'

SITE_ID = 1

CORS_ORIGIN_ALLOW_ALL = True
# 배포시 CORS_ORIGIN_WHITELIST 사용하기.

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly', 
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
        'json': {
            'format': '{"text": "#### %(asctime)s %(name)s %(levelname)s \n##### %(message)s"}'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'http'],  
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
            'propagate': False
        },
    },
}