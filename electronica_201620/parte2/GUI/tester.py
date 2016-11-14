# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:57:10 2016

@author: juan
"""

from client_TCP import client

cliente = client("10.42.0.207", 12345)

message = "Potato"
cliente.send_data(message)