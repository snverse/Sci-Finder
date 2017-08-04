#!venv/bin/python


import sys                       #here so we can insert path to our applicaiton
import logging

print sys.path

if "/var/www/ScifinderApp" not in sys.path:
    sys.path.append("/var/www/ScifinderApp")

from __init__ import s_app as application
import views


logging.basicConfig(stream=sys.stderr)
application.secret_key = 'Add your secret key'
