
# server.py
import socket
import time

#create a socket object
serversocket = socket.socket(
               socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 1099

#bind to the port
serversocket.bind((host, port))

# listen to 5 requests
serversocket.listen(5)

while True:
    # estrablish a connection
    clientsocket,addr = serversocket.accept()

    print ("Got a connection from %s" %  str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
