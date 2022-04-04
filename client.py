from re import S
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


print('Waiting for connection')
s.connect(('localhost', 1234))


while True:
    messg = input("client say: ")
    s.sendall(messg.encode())
    cdata = s.recv(1024)
    print("server say:" , cdata.decode())
  

s.close()