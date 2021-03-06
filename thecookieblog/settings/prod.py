from base import *
import dj_database_url

DEBUG = os.environ.get("DEBUG", False)

ALLOWED_HOSTS = ['the-cookie-blog.herokuapp.com']


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}

CLEAR_DB_URL = os.environ.get('CLEARDB_DATABASE_URL', '')
DATABASES['default'] = dj_database_url.parse(CLEAR_DB_URL)


AWS_STORAGE_BUCKET_NAME = os.environ.get("S3-BUCKET", "")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY", "")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATICFILES_DIRS = (os.path.join(BASE_DIR, STATICFILES_LOCATION),)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '')

AWS_S3_FILE_OVERWRITE = False
