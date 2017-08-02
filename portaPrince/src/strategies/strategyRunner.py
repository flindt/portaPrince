'''
Created on 2 Aug 2017

@author: flindt
'''
import pandas
from predictors.historic import HistoricPredictor
from strategies.AlwaysBuy import AlwaysBuy

class runOneStrategy(object):
    '''
    Runs a given strategy on a set of prices
    '''


    def __init__(self, strategy, priceSet):
        '''
        Constructor
        '''
        pass
    
    def run(self):
        return None
    
    
class varitateAlwaysBuy():
    
    def __init__(self):
        pass
    
    def fillData(self):
        rutData = pandas.read_csv("../../testData/indexes/RUT 2010-2017.csv", sep='\t',parse_dates=['Date'])
         
        dates = []
        allResults = []
        index = 0
        for i in range(2011,2017):
            for j in range(12):
                for k in range(1):
                    dateStr = str(i)+'-'+str(j+1)+'-'+str(k+1)
                    
                    myStrategy = AlwaysBuy(HistoricPredictor(rutData, dateStr ))
                    
                    params = { 'Upper' : 110,
                               'Lower' : 90,
                               'Risk' : 1000,
                               'Fee' : 35,
                               'Return' : 205                               
                               }
                    
                    allResults.append( myStrategy.getResult(params, 28) )
                    index=index+1
                    
        return allResults           
    
    


if __name__ == '__main__':
    alwaysBuyVariation = varitateAlwaysBuy()
    result = pandas.DataFrame( alwaysBuyVariation.fillData() )
    
    pass
