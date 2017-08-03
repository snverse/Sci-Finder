#!venv/bin/python


import sys                       #here so we can insert path to our applicaiton
import logging

print "Hello world!"
print sys.path

sys.path.append("/var/www/ScifinderApp/ScifinderApp")

from __init__ import s_app as application

logging.basicConfig(stream=sys.stderr)
application.secret_key = 'Add your secret key'
