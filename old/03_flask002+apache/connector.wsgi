# coding: utf-8
import sys
sys.path.insert(0, '/var/www/html')

from app-c import app as application
application = create_app()