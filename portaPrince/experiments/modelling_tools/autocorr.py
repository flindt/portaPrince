'''
Created on 3 Aug 2017

@author: moz
'''
import sys
import pandas
import numpy

testDataFile = "linear_test_data.csv"
defaultColumnName = "model"

def autocorr( pd, column ):
    autocorr = numpy.correlate( pd[column], pd[column], 'full')
    acorr_pd = pandas.DataFrame( data={'autocorr': autocorr}, index=range(-1*len(autocorr)//2+1, len(autocorr)//2+1))
    acorr_pd.index.name = 'lag'
    return acorr_pd



if __name__ == '__main__':
    if len(sys.argv) > 1:
        datafile = sys.argv[1] 
    else:
        datafile = testDataFile           
    print "Reading data from", datafile

    if len(sys.argv) > 2:
        columnName = sys.argv[2] 
    else:
        columnName = defaultColumnName           
    print "- column: ", columnName

    pd = pandas.read_csv(datafile, sep='\t')
    pd_ac = autocorr(pd, columnName)
    
    print pd_ac
    
    
