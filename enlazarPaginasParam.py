# usage: enlazarPaginas.py path_a_los_ficheros/prefijo_directorios_comunes*
# PRE: solo debe existir un .html por cada uno de los subarboles que se le pasan 
import sys, os
import os, fnmatch

#prefix = './'
#if len(sys.argv) == 2:
#    prefix = sys.argv[1]

def insertAfer(txt, ref, fileName):
    '''Buscar `ref` (sin distinguir mayus de minus).en el fichero
    `fileName` e introduce `txt` justo despues sin eliminar el
    contenido que puediera haber.'''
    index = None
    ref = ref.lower()
    fd = open(fileName, 'r')

    lines = fd.readlines()
    fd.close()
    for i, line in enumerate(lines):
        if line.lower().find( ref ) != -1:
            lines.insert( i+1, txt)#index = fd.tell()
            index = i
            #txtToAppend = fd.readline()
            break
        #line = fd.readline()

    if not index:
        return -1

    fd = open(fileName, 'w')
    fd.writelines( lines )
    fd.close()
    return 0

def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below
    supplied root directory.'''
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

if __name__ == '__main__':
    dirs = sys.argv[1:] #glob.glob(prefix).sort()
    dirs.sort()
    size = len(dirs)
    if size <= 0:
        exit("Need a bash pattern with all the directories to process Wed29_*") 
        
    # locate the .html file
    
    url = locate("*.html", dirs[0]).next().split(dirs[0])[1]
    print url
    #exit()
    for index, dirName in enumerate(dirs):

        previous_path = 'href="../../{0}{1}"'.format( os.path.basename( dirs[index-1] ), url) if index > 0 else ""
        next_path = 'href="../../{0}{1}"'.format( os.path.basename( dirs[ index+1] ), url) if index < size-1 else ""

        txt = '<p><a {0}>Anterior</a>  <a {1}>Siguiente</a></p>\n'.format(previous_path, next_path)

        dirName +=  url
        if insertAfer( txt, 'body', dirName ) == -1:
            print "Warning: 'body' not found in {0}".format(dirName)
        

        #fd.write("<table borde=0 width=1000>"
    
    
