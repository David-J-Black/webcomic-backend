source "venv/bin/activate"
cd src
gunicorn --bind 127.0.0.1:6900 --workers=2 --access-logfile access.log --error-logfile error.log wsgi:app
deactivate
