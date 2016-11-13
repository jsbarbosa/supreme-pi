# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:04:06 2016

@author: juan
"""

import socket

TCP_IP = 'Lenovo-U410'#'10.42.0.207'

TCP_PORT = 12344
BUFFER_SIZE = 1024
MESSAGE = b"Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
data = data.decode(encoding='UTF-8')
print ("received data:", data)