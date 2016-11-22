# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:53:58 2016

@author: juan
"""

import sys
import time
import numpy as np
from TCP import client
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas)
    
#from mainwindow import Ui_MainWindow as form_class
from PyQt4 import QtCore, QtGui, uic
 
form_class = uic.loadUiType("mainwindow.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)        
        
        self.connect_button.clicked.connect(self.start_client)
        self.startbutton.clicked.connect(self.start_stop)
        self.clear_button.clicked.connect(self.remplt)
        self.temperature_dial.sliderMoved.connect(self.temperature_change_1)
        self.desired_line.editingFinished.connect(self.temperature_change_2)
        
        self.addplt()
        self.start = False
        
        self.init_time = 0
        
        self.plt_time = np.zeros(0)
        self.plt_temp = np.zeros(0)
        self.plt_error = np.zeros(0)
        
        self.client = client()
        
        self.client_label.setText(self.client.ADDRESS)        
        
        self.desired = self.desired_line.text()
 
    def addplt(self):
        self.figure, self.ax1 = plt.subplots(1,1, figsize = (8, 4.5))    
        self.figure.subplots_adjust(bottom = 0.3, left = 0.13, right = 0.87)
        self.figure.set_facecolor('none')         
        
        self.ax1.set_xlabel("Time (min)")
        self.ax1.set_ylabel("Temperature (C)", color = "r")
        self.ax1.set_xlim(0, 1)
        self.ax1.set_ylim(0, 20)
        self.ax1.grid()
        
        self.ax2 = self.ax1.twinx()
        self.ax2.set_ylabel("Error (C)", color = "grey")
        self.ax2.set_xlim(0, 1)
        self.ax2.set_ylim(0, 20)
        
        self.ax1.hold(True)
        self.ax2.hold(True)  
        
        self.ax1_temperatures = self.ax1.plot([], [], "-", color = "r")[0]
        self.ax2_errors = self.ax2.plot([], [], "-", color = "grey")[0]  
        
        self.canvas = FigureCanvas(self.figure)
        self.pltvl.addWidget(self.canvas)
        self.canvas.draw()
    
    def remplt(self):
        self.pltvl.removeWidget(self.canvas)
        self.canvas.close()
        self.plt_error = np.zeros(0)
        self.plt_temp = np.zeros(0)
        self.plt_time = np.zeros(0)
        self.figure = None
        
    def plotter(self):
        current_time = (time.time() - self.init_time)/60
        
        current_temp = float(self.client.send_data("%.1f"%self.desired))
        current_error = self.desired - current_temp
        
        self.plt_time = np.append(self.plt_time, [current_time])
        self.plt_temp = np.append(self.plt_temp, [current_temp])
        self.plt_error = np.append(self.plt_error, [current_error])
        
        minx, maxx = self.ax1.get_xlim()
        miny, maxy = self.ax1.get_ylim()
        
        if self.plt_time[-1] >= maxx:
            self.ax1.set_xlim(minx, 3*maxx/2)
        if self.plt_temp[-1] >= maxy:
            self.ax1.set_ylim(miny, 3*maxy/2)
            
        miny, maxy = self.ax2.get_ylim()
        if self.plt_error[-1] >= maxy:
            self.ax2.set_ylim(min(self.plt_error), 3*maxy/2)
        elif self.plt_error[-1] <= miny:
            self.ax2.set_ylim(min(self.plt_error), maxy)
            
        self.ax1_temperatures.set_data(self.plt_time, self.plt_temp)
        self.ax2_errors.set_data(self.plt_time, self.plt_error)
        self.canvas.draw()
        
        self.current_line.setText("%.3f"%current_temp)
        
    def start_stop(self):
        self.start = not self.start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.plotter)
        
        if self.start:
            if self.init_time == 0 or self.figure == None:
                self.init_time = time.time()
                
                pot_info = self.IC_spinBox.value(), self.UD_spinBox.value(), self.CS_spinBox.value()
                
                data = "I(%s)"%pot_info
                self.client.send_data(data)
                
            if self.figure == None:
                self.addplt()
                
            self.desired = self.desired_line.text()

            try:
                self.desired = float(self.desired)
            except Exception as e:
                print(e)
                
            self.startbutton.setStyleSheet("background-color: rgb(38, 229, 57)")
            self.timer.start(200)
        else:
            self.startbutton.setStyleSheet("background-color: rgb(229, 38, 38)")
            self.timer.stop()
            
    def temperature_change_1(self, value):
        self.desired = float(value)
        self.desired_line.setText(str(self.desired))
    
    def temperature_change_2(self):
        value = float(self.desired_line.text())
        self.desired = value
        self.desired_line.setText(str(value))
        self.temperature_dial.setValue(value)
        
    def start_client(self):
        host = self.host_line.text()
        port = self.port_line.text()
        try:
            port = int(port)
            ans = self.client.start_client(host, port)
            if ans != None:
                raise Exception(ans)
                
            else:
                self.status_label.setStyleSheet("background-color: rgb(38, 229, 57)")

        except Exception as E:
            self.showdialog(E)
            
    def showdialog(self, error):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        
        msg.setText("Something went wrong:")
        msg.setInformativeText(str(error))
        msg.setWindowTitle("TCP Error")
	
        retval = msg.exec_()     
        

app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
print("Window")
MyWindow.show()
app.exec_()
MyWindow.client.close_socket()