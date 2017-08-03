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

def autocorr( pd, columnName ):
    autocorr = numpy.correlate( pd[columnName], pd[columnName], 'full')
    acorr_pd = pandas.DataFrame( data={'autocorr': autocorr}, index=range(-1*len(autocorr)//2+1, len(autocorr)//2+1))
    acorr_pd.index.name = 'lag'
    return acorr_pd

def plot_autocorr( pd, columnName ):
    ''' this will plot index vs. ColumnName, but is intended for autocorrelations.
    '''
    ax = pd.plot( y=columnName, lw=2,colormap='jet', legend=False, grid=True)
    ax.set_ylabel('autocorrelation')


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
    pd[columnName].plot(grid=True)

    # autocorrelate
    pd_ac = autocorr(pd, columnName)
    print pd_ac
    
    # and plot it    
    plot_autocorr( pd_ac, 'autocorr')
    plt.show()
    
