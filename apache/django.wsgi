import os
import sys
sys.stdout = sys.stderr

# Add the virtual Python environment site-packages directory to the path
# See http://code.google.com/p/modwsgi/wiki/VirtualEnvironments
import site
site.addsitedir('/var/www/founderdating/lib/python2.6/site-packages')


#If your project is not on your PYTHONPATH by default you can add the following
sys.path.append('/var/www/founderdating')
os.environ['DJANGO_SETTINGS_MODULE'] = 'fd.settings'
os.environ['FD_ENVIRONMENT'] = 'prod'

sys.path.append('/var/www/founderdating/fd')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
