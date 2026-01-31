#!/bin/bash
set -e

# Применяем миграции
python manage.py migrate --noinput

# Собираем статику
python manage.py collectstatic --noinput --clear

cp -r /app/site/ /static/

exec "$@"