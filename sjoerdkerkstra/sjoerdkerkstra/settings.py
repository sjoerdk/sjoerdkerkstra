import os
import glob 
from django.core.exceptions import ImproperlyConfigured

# Scheme for using different settings wihout having everything in git:
# Get settings/*.conf and execute these in alphabetic order. 
# later values overwrite previous settings.  

path = os.path.join(os.path.dirname(__file__), 'settings', '*.conf')
conffiles = glob.glob(path)

if(len(conffiles) == 0):
    msg = "Could not find any files matching '" + path + "'. There should be at least one configuration file containing django settings at that location."
    raise ImproperlyConfigured(msg) 

conffiles.sort()
for f in conffiles:
    execfile(os.path.abspath(f))

