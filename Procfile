release: python manage.py migrate
web: gunicorn smartglasses.wsgi:application --bind 0.0.0.0:$PORT
