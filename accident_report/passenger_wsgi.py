import os
import sys

# This is where manage.py is located
sys.path.insert(0, "/home/arnaqueh/home/accident_report/accident_report")

# Point to the settings inside the inner accident_report
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "accident_report.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
