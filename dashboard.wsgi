#!/usr/bin/python

import sys, os, logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/dashboard/")
    
from app import create_app
application = create_app()
