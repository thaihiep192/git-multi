import socket
import os
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))

threadCount = 0
s.listen(5)

def threaded_client(c):
    
    while True:
        data = c.recv(1024)
        print("Client "+ str(address[1]) + " say: " + data.decode())
        smessg = input("server say:")
        c.send(smessg.encode())       
    c.close()
while True:
    con,address = s.accept()
    print("connected to: " + (address[0]) + ";" + str(address[1]))
    start_new_thread(threaded_client, (con,))
    threadCount +=1
    print("thread number: " + str(threadCount))
s.close()
