"""
Created on Sun Nov 13 18:09:13 2016

@author: juan
"""

import socket

host = socket.gethostname()        # Symbolic name meaning all available interfaces
port = 12344     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(host , port)

while True:
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    try:
        data = conn.recv(1024).decode(encoding='UTF-8')
        if data == "close":
            break
        
        if data:
            print("Client Says: " + data)
            conn.sendall(b"Server Says: hi")

    except socket.error:
        print("Error Occured.")
        break
    
    conn.close()
