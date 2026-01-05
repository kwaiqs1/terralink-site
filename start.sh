#!/usr/bin/env bash
set -euo pipefail

cd /app

echo "PORT is: ${PORT:-8000}"

python manage.py migrate --noinput
python manage.py collectstatic --noinput

# ✅ Create superuser from Railway Variables (safe to run every deploy)
python manage.py ensure_superuser

exec gunicorn terralink_site.wsgi:application \
  --bind "0.0.0.0:${PORT:-8000}" \
  --access-logfile - \
  --error-logfile - \
  --log-level info
