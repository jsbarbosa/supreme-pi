"""
Created on Sun Nov 13 18:09:13 2016

@author: juan
"""

import socket
import numpy as np

host = "10.42.0.207"        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(host , port)

s.listen(1)
conn, addr = s.accept()

while True:
    try:
        data = conn.recv(1024).decode(encoding='UTF-8')
        if data == "":
            s.listen(1)
            conn, addr = s.accept()

        elif data == "close":
            break
        
        if data:
            answer = ("%.6f"%np.random.rand()).encode(encoding='UTF-8')
            conn.sendall(answer)
    except socket.error:
        print("Error Occured.")
        break
    
conn.close()
