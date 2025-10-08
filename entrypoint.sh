#!/bin/bash

echo "Running migrations..."
poetry run python manage.py migrate
echo "Migration complete."

echo "Starting Django development server..."
exec poetry run python manage.py runserver 0.0.0.0:8000
