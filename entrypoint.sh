#!/bin/sh
set -e

echo "Esperando a la base de datos..."
until python manage.py dbshell >/dev/null 2>&1; do
  sleep 2
done

echo "Aplicando migraciones..."
python manage.py migrate --noinput

exec "$@"
