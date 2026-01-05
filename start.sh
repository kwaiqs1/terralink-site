#!/usr/bin/env bash
set -o errexit
set -o pipefail

echo "PORT is: ${PORT}"

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn terralink_site.wsgi:application \
  --bind 0.0.0.0:${PORT:-8000} \
  --access-logfile - \
  --error-logfile - \
  --log-level info
