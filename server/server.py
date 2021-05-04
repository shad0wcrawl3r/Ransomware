from socket import socket, gethostname
from subprocess import Popen
from sys import executable

port=11111
host=''
sock = socket()

sock.bind((host,port)) #two brackets because the method requires a tuple

sock.listen(1)
print('Listening on %s:%i'%(host,port))
con,addr = sock.accept()
count=0
backlog=[]
while True:
    data_recv=con.recv(1024).decode('utf-8')
    if data_recv=='END':
        break
    # with open('testf','w') as f:
    #     f.write(data_recv)
    if len(backlog)>20:
        del backlog[0]
    backlog.append(data_recv)
    if len(set(backlog))==1 and "" in backlog:
        print("Too many blank lines detected, exiting")
        break
    file_name=str(addr[0])
    
    with open(file_name,"a") as f:
        f.write(data_recv)


con.close()
sock.close()

#relaunch the server and exit the present instance
Popen([executable, __file__])
exit()

