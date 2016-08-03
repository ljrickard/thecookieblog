from base import *

DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}


AWS_STORAGE_BUCKET_NAME = os.environ.get("S3-BUCKET", "")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_S3_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_S3_SECRET_ACCESS_KEY", "")
AWS_HOST_REGION = os.environ.get("AWS_S3_HOST_REGION", "")
AWS_S3_CUSTOM_DOMAIN = '%s.%s' % AWS_STORAGE_BUCKET_NAME, AWS_HOST_REGION

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATICFILES_DIRS = (os.path.join(BASE_DIR, STATICFILES_LOCATION),)
