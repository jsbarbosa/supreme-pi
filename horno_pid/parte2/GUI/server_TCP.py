# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:04:06 2016

@author: juan
"""

from TCP import server

my_server = server("10.42.0.207", 12345)
my_server.attention()
