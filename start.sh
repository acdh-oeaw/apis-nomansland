#!/bin/bash
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
#FIXME: remove that
#sed -i '65 s/value.id = value.text;/value.id = value.id;/' /app/.heroku/python/lib/python3.8/site-packages/dal_select2/static/autocomplete_light/select2.js
python manage.py collectstatic --noinput --settings=apis.settings.dev
python manage.py migrate --settings=apis.settings.dev
gunicorn apis.wsgi -b 0.0.0.0:5000 --timeout 120 --workers=3 --threads=3 --worker-connections=1000
