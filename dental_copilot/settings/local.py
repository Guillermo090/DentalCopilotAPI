from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
X_FRAME_OPTIONS = 'ALLOWALL'
XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']
WSGI_APPLICATION = 'dental_copilot.wsgi.application'
CORS_ORIGIN_ALLOW_ALL = True

#? database 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret('db_name'),
        'HOST': get_secret('db_host'),
        'PORT': get_secret('db_port'),
        'USER': get_secret('db_user'),
        'PASSWORD': get_secret('db_password'),
    }
}
