# usage: enlazarPaginas.py path_a_los_ficheros/prefijo_directorios_comunes*
import sys, os

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
        


if __name__ == '__main__':
    dirs = sys.argv[1:] #glob.glob(prefix).sort()
    dirs.sort()

    size = len(dirs)
    
    for index, dirName in enumerate(dirs):

        previous_path = 'href="../../{0}/bb11.cesvima.upm.es/trafico_madrid.html"'.format( os.path.basename( dirs[index-1] )) if index > 0 else ""
        next_path = 'href="../../{0}/bb11.cesvima.upm.es/trafico_madrid.html"'.format( os.path.basename( dirs[ index+1] )) if index < size-1 else ""

        txt = '<p><a {0}>Anterior</a>  <a {1}>Siguiente</a></p>\n'.format(previous_path, next_path)

        dirName +=  '/bb11.cesvima.upm.es/trafico_madrid.html'
        if insertAfer( txt, 'body', dirName ) == -1:
            print "Warning: 'body' not found in {0}".format(dirName)
        

        #fd.write("<table borde=0 width=1000>"
    
    
