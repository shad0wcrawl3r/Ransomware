from socket import socket, gethostname

port=11111

sock = socket()

sock.connect(('192.168.213.4',port)) #two brackets because the constructor requires a tuple

sock.send(b"Testing123")

with open ("received_file",'w') as wf:
    print('Opened File')
    print('Listening for data')
    while True:
        data = sock.recv(1024)
        print(data)
        if not data:
            break
        wf.write(data)
print('write complete')

print('closing socket')

sock.close()

print('conn_closed')

