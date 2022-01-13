# myApp.wsgi
import sys
sys.path.insert(0, "/var/www/html/FlaskDir")

from myApp import app as application

# myApp above is the myApp.py file, app is the 'app' we define inside the myApp.py file
