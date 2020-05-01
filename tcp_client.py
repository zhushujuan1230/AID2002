from socket import *

sockfd = socket()

server_addr=('127.0.0.1',8888)
sockfd.connect(server_addr)
f=open("time.txt","rb")
while True:
    data=f.read(100)
    if not data:
        break
    sockfd.send(data)
data=sockfd.recv(1024)
print("Server:",data.decode())

sockfd.close()
