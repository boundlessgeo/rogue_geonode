#!/bin/sh
echo "------ Create database tables ------"
python manage.py syncdb --noinput

echo "------ create default admin user ------"
echo "from geonode.people.models import Profile; Profile.objects.create_superuser('admin', 'admin@boundlessgeo.com', 'admin')" | python manage.py shell

echo "------ starting gunicorn  ------"
gunicorn geoshape.wsgi --workers 2