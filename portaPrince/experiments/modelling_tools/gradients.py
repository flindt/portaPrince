'''
Created on 3 Aug 2017

@author: moz
'''

import sys
import pandas
import numpy
import matplotlib.pyplot as plt

testDataFile = "linear_test_data.csv"
defaultColumnName = "model"

def addGradients( pd, columnName ):
    ''' adds velocity and acceleration columns
        v_columnname and a_columnname
    '''
    pd['v_'+columnName] = numpy.gradient(pd[columnName])
    pd['a_'+columnName] = numpy.gradient(pd['v_'+columnName])

def plot_gradient( pd, columnName):
    columns = [columnName, 'v_'+columnName, 'a_'+columnName]
    pd[columns].plot( subplots=True, legend=False)

if __name__ == '__main__':
    ### some usability :-)
    if len(sys.argv) > 1:
        datafile = sys.argv[1] 
    else:
        datafile = testDataFile
        print "info: you could do"
        print "  %s other.csv columnB"%(sys.argv[0],)
    print "Reading data from", datafile

    if len(sys.argv) > 2:
        columnName = sys.argv[2] 
    else:
        columnName = defaultColumnName           
    print "- column: ", columnName

    # read data
    pd = pandas.read_csv(datafile, sep='\t')

    # add gradients
    addGradients(pd, columnName)
    print pd
#     
#     # and plot it    
    plot_gradient( pd, columnName)
    plt.show()
    
    