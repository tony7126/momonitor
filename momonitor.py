import os
import sys
import site

sys.path.insert(0, "/home/ubuntu/momo/momonitor")
sys.path.insert(1, "/home/ubuntu/momo/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
