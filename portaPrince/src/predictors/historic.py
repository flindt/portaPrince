'''
Created on 20 Jul 2017

@author: flindt
'''


class HistoricPredictor(object):
    '''
    classdocs
    '''


    def __init__(self, pdHistoricValues, startDate):
        self.historicValues = pdHistoricValues
        self.startDate = startDate
        
    def predict(self, n=100):
        result = self.historicValues.set_index("Date").loc[self.startDate:][:n]
        
        return result.values[:,0]/result.values[0,0]*100
    
    def getPrices(self, size= 100):
        return self.predict(size)