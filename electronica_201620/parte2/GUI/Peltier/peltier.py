# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:53:58 2016

@author: juan
"""

import sys
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas)
    
from PyQt4 import QtCore, QtGui, uic
 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("mainwindow.ui")[0]
 
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.startbutton.clicked.connect(self.start_stop)
        
        self.addplt()
        self.start = False
        
        self.init_time = 0
        
        self.plt_time = np.zeros(0)
        self.plt_temp = np.zeros(0)
        self.plt_error = np.zeros(0)
        
        self.desired = self.desired_line.text()
 
    def addplt(self):
        self.figure, self.ax1 = plt.subplots(1,1, figsize = (8, 4.5))    
        self.figure.subplots_adjust(bottom = 0.2, left = 0.1)
        self.figure.set_facecolor('none')         
        
        self.ax1.set_xlabel("Time (min)")
        self.ax1.set_ylabel("Temperature (C)")
        self.ax1.set_xlim(0, 1)
        self.ax1.set_ylim(0, 20)
        self.ax1.grid()
        
        self.ax2 = self.ax1.twinx()
        self.ax2.set_ylabel("Error (C)")
        self.ax2.set_xlim(0, 1)
        self.ax2.set_ylim(0, 20)
        
        self.ax1.hold(True)
        self.ax2.hold(True)  
        
        self.ax1_temperatures = self.ax1.plot([], [], "-", color = "r")[0]
        self.ax2_errors = self.ax2.plot([], [], "-", color = "g")[0]  
        
        self.canvas = FigureCanvas(self.figure)
        self.pltvl.addWidget(self.canvas)
        self.canvas.draw()
        
    def remplt(self):
        self.pltvl.removeWidget(self.canvas)
        self.canvas.close()
        
    def plotter(self):
        self.plt_time = np.append(self.plt_time, [(time.time() - self.init_time)/60])
        self.plt_temp = np.append(self.plt_temp, [np.random.rand()*20])
        self.plt_error = np.append(self.plt_error, [self.desired-self.plt_temp[-1]])
        
        minx, maxx = self.ax1.get_xlim()
        miny, maxy = self.ax1.get_ylim()
        
        if self.plt_time[-1] >= maxx:
            self.ax1.set_xlim(minx, 3*maxx/2)
        if self.plt_temp[-1] >= maxy:
            self.ax1.set_ylim(miny, 3*maxy/2)
            
        miny, maxy = self.ax2.get_ylim()
        if self.plt_error[-1] >= maxy:
            self.ax2.set_ylim(miny, 3*maxy/2)
            
        self.ax1_temperatures.set_data(self.plt_time, self.plt_temp)
        self.ax2_errors.set_data(self.plt_time, self.plt_error)
        self.canvas.draw()
        
    def start_stop(self):
        self.start = not self.start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.plotter)      
        if self.start:
            if self.init_time == 0:
                self.init_time = time.time()
                
                
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
            
app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()