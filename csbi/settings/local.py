from .base import (
    os,
    BASE_DIR,
)

DEBUG = True
<<<<<<< HEAD
ALLOWED_HOSTS = ['*']
=======
ALLOWED_HOSTS = []
>>>>>>> 739ecddfbb22467edc2b53dfa37064a806d76edc

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
