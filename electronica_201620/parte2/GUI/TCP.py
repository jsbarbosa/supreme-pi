"""
Created on Sun Nov 13 18:09:13 2016

@author: juan
"""

import socket
from controller import controller



class client:
    def __init__(self, TCP_IP, TCP_PORT, BUFFER_SIZE = 1024):
        self.TCP_IP = TCP_IP
        self.TCP_PORT = TCP_PORT
        self.BUFFER_SIZE = BUFFER_SIZE
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.TCP_IP, self.TCP_PORT))
        
    def send_data(self, message):
        message = message.encode(encoding='UTF-8')
        self.socket.sendall(message)
        data = self.socket.recv(self.BUFFER_SIZE).decode(encoding='UTF-8')        
        return data
        
    def close_socket(self):
        self.send_data("close")
        self.socket.close()



class server:
    def __init__(self, host = "10.42.0.207", port = 12345):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bing((self.host, self.port))
        print(host , port)

        self.socket.listen(1)
        self.conn, addr = self.socket.accept()

        self.controller = controller(0,0,0,0)

    def attention(self):
        while True:
            try:
                data = self.conn.recv(1024).decode(encoding='UTF-8')
                    
                if data == "":
                    self.socket.listen(1)
                    self.conn, addr = s.accept()

                elif data == "close":
                    break
                
                if data:
                    temp = self.controller.read()
                    answer = ("%.6f"%temp).encode(encoding='UTF-8')
                    conn.sendall(answer)
            except socket.error:
                print("Error Occured.")
                break
        self.conn.close()
