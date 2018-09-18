"""
WSGI config for miniverse project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/var/www/miniverse.dans.knaw.nl/.virtualenvs/miniverse/lib/python2.7/site-packages')
sys.path.append('/var/www/miniverse.dans.knaw.nl/.virtualenvs/miniverse')
sys.path.append('/var/www/miniverse.dans.knaw.nl/miniverse')
for k in sorted(os.environ.keys()):
    v = os.environ[k]
    print ('%-30s %s' % (k,v[:70]))
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miniverse.settings.local_settings")
#heroku_dev")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
