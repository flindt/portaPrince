'''
Created on 3 Aug 2017

@author: moz
'''

from modelling_tools.autocorr import autocorr, plot_autocorr
from modelling_tools.gradients import addGradients, plot_gradient
import pandas
import matplotlib.pyplot as plt


columnName = "Close"
rutdatafile = "../testData/indexes/RUT 2010-2017.csv"

if __name__ == "__main__":
        # read data
    pd = pandas.read_csv(rutdatafile, sep='\t')
    pd[columnName].plot(grid=True)
    
    # check gradients
    addGradients(pd, columnName, relative=False)
    plot_gradient(pd, columnName)
    
    # check autocorrelations
    # "close" is not noise, v and a might be  
    pd_ac = autocorr(pd, columnName)
    plot_autocorr(pd_ac, 'autocorr')
    pd_ac_v = autocorr(pd, 'v_'+columnName)
    plot_autocorr(pd_ac_v, 'autocorr')
    pd_ac_a = autocorr(pd, 'a_'+columnName)
    plot_autocorr(pd_ac_a, 'autocorr')
    
    plt.show()
