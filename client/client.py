from socket import socket, gethostname

port=11111


sock=socket()
sock.bind(('192.168.213.4', port)) #again, this requires a tuple

sock.listen(5) #lsiten for bad connection 
                #dont understand why the original code wrote this line, need to research

while True:
    conn,addr= sock.accept()  #this is to establish a connection

    data_recv=conn.recv(1024)

    print(data_recv)

    with open('testfile','r') as sf:
        data = sf.read(1024)    #reading 1024 bytes at a time
        while data:
            conn.send(data)

            data=sf.read(1024)  #reading another 1024 bytes of data

        #the while loop will continue until the file reaches EOF

    print("Sending complete")

    conn.close()
    break

sock.shutdown(1)

sock.close()

        






