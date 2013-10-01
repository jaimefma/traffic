#! /usr/bin/python

import time, os, sys

if len(sys.argv) == 3:
    dest = sys.argv[2]
    if not os.path.exists(dest):
        os.mkdir(dest)
    print "Storing data in: {0}".format(sys.argv[2])
    os.chdir(sys.argv[2])
    url = sys.argv[1]
else:
    usage = "usage: {0} <url> <path_to_store_data>".format(sys.argv[0])
    exit( usage );

print "Connecting to host {0}".format(url)
os.system('wget -k -H -p {0}'.format(url))

# Renombrar cosas
tNow = time.ctime().replace(':','').split()

newPre = '{0}{1}_{2}/'.format(tNow[0], tNow[2], tNow[3])
os.mkdir(newPre)
hostName = url.split('/')[0]
os.rename(hostName, newPre+hostName)
os.rename('www.dgt.es', newPre+'www.dgt.es')
          
