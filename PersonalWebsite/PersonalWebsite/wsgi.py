"""
WSGI config for PersonalWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'PersonalWebsite')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PersonalWebsite.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

