#!/bin/bash


python manage.py makemigrations --noinput
python manage.py migrate




if [ "$ENVIRONMENT" = "development" ]; then
    echo "Running Django development server..."
    python manage.py runserver 0.0.0.0:$DJANGO_PORT
elif [ "$ENVIRONMENT" = "production" ]; then
    python manage.py collectstatic --noinput
    echo "Running Django production server..."
    gunicorn ai_trace_poll.wsgi:application --bind 0.0.0.0:$DJANGO_PORT
else
    echo "Unknown environment: $ENVIRONMENT"
    exit 1
fi
