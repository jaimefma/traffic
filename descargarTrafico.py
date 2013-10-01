#! /usr/bin/python
# usage: descargarTrafico.py [path_to_store_data]

import time, os, sys

if len(sys.argv) == 2:
    os.chdir(sys.argv[1])

os.system('wget -k -H -p bb11.cesvima.upm.es/trafico_getafe.html')

# Renombrar cosas
tNow = time.ctime().replace(':','').split()

newPre = '{0}{1}_{2}/'.format(tNow[0], tNow[2], tNow[3])
os.mkdir(newPre)
os.rename('bb11.cesvima.upm.es', newPre+'bb11.cesvima.upm.es')
os.rename('www.dgt.es', newPre+'www.dgt.es')
          
