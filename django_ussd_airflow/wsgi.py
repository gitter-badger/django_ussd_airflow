"""
WSGI config for django_ussd_airflow project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django_ussd_airflow import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_ussd_airflow.settings")

application = get_wsgi_application()
