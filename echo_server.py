
#echo_server.py

import socket

host =''       #symblic name meaning all available interfaces
port = 12345   #arbitrary non_privileged port

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()
print("connceted by ", addr)


while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)

conn.close()

