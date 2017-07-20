'''
Created on 21 Jun 2017

@author: flindt
'''

import pyqtgraph
#from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QApplication
from PyQt4.QtGui import QMainWindow, QVBoxLayout, QApplication
from PyQt4.QtCore import pyqtSlot
import sys

import numpy as np

import random 

def coin_flip(flip_count):
    """Returns how mains tails, 1, out flip_count coin flips"""
    return sum(random.randint(0, 1) for _ in xrange(int(flip_count)))
#np.vectorize(coin_flip)(np.ones(100)*100)

class Example(QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        self.addPlots()

        
        
    def initUI(self):   
        
        grid = QVBoxLayout()
                
        self.myGraph = pyqtgraph.PlotWidget() 
        self.myGraph.fitInView(1,250,1,500)
        self.setCentralWidget(self.myGraph)
        self.showNormal()
        
        grid.addWidget(self.myGraph)    
        
        self.statusBar().showMessage('Ready')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Fitting Data to exponential curve')    
        self.show()
       
    @pyqtSlot(object)
    def update(self, *plotInput, **plotInputKV):
        
        self.myGraph.plot(*plotInput, **plotInputKV)
        
    def addPlots(self):
        import pandas
        rutData = pandas.read_csv("../testData/indexes/RUT 2010-2017.csv", sep='\t')
        rutData['Delta'] = rutData.Close.diff().shift(-1)
        rutData['DeltaRelative'] = rutData.Delta / rutData.Close
        
        self.update(y=rutData.DeltaRelative.values)
        

def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()