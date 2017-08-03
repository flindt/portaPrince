'''
Created on 20 Jul 2017

@author: flindt
'''

import numpy.random
import pandas

class NormalPredictor(object):

    def __init__(self, stdev=0.1):
        self.stdev=stdev
        pass
    
    def predict(self, n=100):
        self.values = pandas.DataFrame({'price':[100]}).reindex(range(n))
        
        changes = numpy.random.normal(0, self.stdev, n)
        for i in range(n-1):
            self.values.price.iloc[i+1] = (1+changes[i])*self.values.price.iloc[i]
            
        return self.values
        