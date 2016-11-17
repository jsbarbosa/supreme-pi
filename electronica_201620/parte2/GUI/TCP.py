"""
Created on Sun Nov 13 18:09:13 2016

@author: juan
"""

import socket
from controller import controller

class client:
    def __init__(self, TCP_IP = "127.0.0.1", TCP_PORT = 12345, BUFFER_SIZE = 1024):
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
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        print(host , port)

        self.socket.listen(1)
        self.conn, addr = self.socket.accept()        

    def attention(self):
        while True:
            try:
                data = self.conn.recv(1024).decode(encoding='UTF-8')
                
                if data:
                    try:
                        data = float(data)
                        
                        temp = self.controller.read()
                        self.controller.desired_temperature = data
                        answer = ("%.6f"%temp).encode(encoding='UTF-8')
                        self.conn.sendall(answer)
                    except ValueError:    
                        if data[0] == "I":
                            self.conn.sendall("Fine".encode(encoding='UTF-8'))
                            kp_info, ki_info, kd_info, vals = eval(data[1:])                    
                            self.controller = controller(kp_info, ki_info, kd_info, vals)
                    
                        elif data == "close":
                            break
                    
                else:
                    self.socket.listen(1)
                    self.conn, addr = self.socket.accept()
                    
            except socket.error:
                print("Error Occured.")
                break
        self.conn.close()
