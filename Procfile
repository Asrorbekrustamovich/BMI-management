web: python manage.py migrate && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT && python manage.py collectstatic --noinput



