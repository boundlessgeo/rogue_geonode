# -*- coding: utf-8 -*-
import os
from geoshape.settings import *

SITENAME = 'Boundless Exchange'

LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

WSGI_APPLICATION = "geoshape.wsgi.application"

STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

ROOT_URLCONF = 'geoshape.urls'

LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

if 'DEBUG' in os.environ:
    DEBUG = os.environ.get('DEBUG')

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ.get('SECRET_KEY')

if 'DATABASE_URL' and 'POSTGIS_URL' in os.environ:
    import dj_database_url
    POSTGIS = os.environ.get('POSTGIS_URL')
    DATABASES = {'default': dj_database_url.config(conn_max_age=500),
                 'datastore': dj_database_url.parse(POSTGIS, conn_max_age=500)
                 }

if 'GS_URL' and 'GS_USER' and 'GS_PASSWORD' in os.environ:
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

if 'ES_URL' in os.environ:
    ES_ENGINE = 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine'
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': ES_ENGINE,
            'URL': os.environ.get('ES_URL'),
            'INDEX_NAME': os.environ.get('ES_INDEX', 'storyscapes'),
            },
    }
    INSTALLED_APPS += (
        'haystack',
    )

if 'RABBITMQ_URL' in os.environ:
    BROKER_URL = os.environ.get('RABBITMQ_URL')
    CELERY_ALWAYS_EAGER = False
    NOTIFICATION_QUEUE_ALL = not CELERY_ALWAYS_EAGER