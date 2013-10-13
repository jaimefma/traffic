#! /usr/bin/python


"""
Templates should only contains image dgt url cameras to 'dgt.es/...'

The
"""

import time, os, sys, re
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
_log = logging.getLogger(__name__)

if len(sys.argv) == 3:
    dest = sys.argv[2]
    if not os.path.exists(dest):
        os.mkdir(dest)
    print "Storing data in: {0}".format(sys.argv[2])
    os.chdir(sys.argv[2])
    url = sys.argv[1]
    match = re.match(r'http.*://(?P<url>.*)', url)
    if match:
        url = match.group('url')
else:
    usage = "usage: {0} <url> <path_to_store_data>".format(sys.argv[0])
    exit( usage );

print "Connecting to host {0}".format(url)
os.system('wget -k -H -p {0}'.format(url))

_log.info("URL '%s'" % url)
# Renombrar cosas
tNow = time.ctime().replace(':','').split()

newPre = '{0}{1}_{2}/'.format(tNow[0], tNow[2], tNow[3])
os.mkdir(newPre)
_log.info("%s folder created" % newPre)
hostName = url.split('/')[0]
new_name = newPre+hostName
_log.info("Renamed folder %s by %s" % (hostName, new_name))
os.rename(hostName, new_name)
os.rename('dgt.es', newPre+'dgt.es')

          
