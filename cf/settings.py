# -*- coding: utf-8 -*-
import os
import dj_database_url
from geoshape.settings import *

if 'DEBUG' in os.environ:
    DEBUG = os.environ.get('DEBUG')

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ.get('SECRET_KEY')

USE_AWS_S3_STATIC = os.environ.get('USE_AWS_S3_STATIC')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
AWS_S3_DOMAIN = AWS_S3_CUSTOM_DOMAIN if AWS_S3_CUSTOM_DOMAIN else 's3.amazonaws.com'
AWS_S3_BUCKET_DOMAIN = '%s.%s' % (AWS_STORAGE_BUCKET_NAME, AWS_S3_DOMAIN)

SITENAME = 'Exchange'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_BUCKET_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'cf.s3utils.MediaStorage'

if USE_AWS_S3_STATIC > 0:
    STATICFILES_STORAGE = 'cf.s3utils.StaticStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_BUCKET_DOMAIN, STATICFILES_LOCATION)
else:
    STATICFILES_STORAGE = 'cf.s3utils.StaticStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_BUCKET_DOMAIN, STATICFILES_LOCATION)
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, STATICFILES_LOCATION)
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

POSTGIS = os.environ.get('POSTGIS_URL')
DATABASES = {
    'default': dj_database_url.config(conn_max_age=500),
    'datastore': dj_database_url.parse(POSTGIS, conn_max_age=500)
}

GS_URL = os.environ.get('GS_URL')
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': GS_URL,
        'PUBLIC_LOCATION': GS_URL,
        'USER': os.environ.get('GS_USER'),
        'PASSWORD': os.environ.get('GS_PASSWORD'),
        'MAPFISH_PRINT_ENABLED': True,
        'PRINT_NG_ENABLED': True,
        'GEONODE_SECURITY_ENABLED': True,
        'GEOGIG_ENABLED': True,
        'WMST_ENABLED': False,
        'DATASTORE': 'datastore',
        'GEOGIG_DATASTORE_DIR': '/var/lib/geoserver_data/geogig',
    }
}

GEOGIG_DATASTORE_NAME = 'geogig-repo'
UPLOADER = {
    'BACKEND': 'geonode.importer',
    'OPTIONS': {
        'TIME_ENABLED': True,
        'GEOGIG_ENABLED': True,
    }
}

ES_ENGINE = 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': ES_ENGINE,
        'URL': os.environ.get('ES_URL'),
        'INDEX_NAME': os.environ.get('ES_INDEX', 'exchange'),
    },
}

BROKER_URL = os.environ.get('RABBITMQ_URL')
CELERY_ALWAYS_EAGER = False
NOTIFICATION_QUEUE_ALL = not CELERY_ALWAYS_EAGER

INSTALLED_APPS += (
    'storages',
    'haystack',
)
