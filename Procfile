

web: gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
#or works good with external database
web: python manage.py migrate && gunicorn core.wsgi