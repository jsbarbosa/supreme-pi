"""
Created on Sun Nov 13 18:09:13 2016

@author: juan
"""

import socket

class client:
    def __init__(self, TCP_IP, TCP_PORT, BUFFER_SIZE = 1024):
        self.TCP_IP = TCP_IP
        self.TCP_PORT = TCP_PORT
        self.BUFFER_SIZE = BUFFER_SIZE
        self.ADDRESS = socket.gethostname()
        
    def start_client(self, TCP_IP, TCP_PORT):
        self.TCP_IP = TCP_IP
        self.TCP_PORT = TCP_PORT
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.TCP_IP, self.TCP_PORT))
        except Exception as e:
            return e
            
    def send_data(self, message):
        message = message.encode(encoding='UTF-8')
        self.socket.sendall(message)
        data = self.socket.recv(self.BUFFER_SIZE).decode(encoding='UTF-8')        
        return data
        
    def close_socket(self):
        self.socket.close()

class server:
    def __init__(self, host, port):
        from controller import controller
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
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
                    self.conn, addr = self.socket.accept()

                elif data == "close":
                    break
                
                if data:
                    temp = self.controller.read()
                    answer = ("%.6f"%temp).encode(encoding='UTF-8')
                    self.conn.sendall(answer)
            except socket.error:
                print("Error Occured.")
                break
        self.conn.close()
