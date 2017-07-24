'''
Created on 20 Jul 2017

@author: flindt
'''
import unittest
from predictors.historic import HistoricPredictor
import pandas

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testOne(self):
        rutData = pandas.read_csv("../../testData/indexes/RUT 2010-2017.csv", sep='\t',parse_dates=['Date'])
        
        myPred = HistoricPredictor(rutData, "2014-03-01" )
        result = myPred.predict(10)
        
        pass
    
    def testMany(self):
        rutData = pandas.read_csv("../../testData/indexes/RUT 2010-2017.csv", sep='\t',parse_dates=['Date'])
        
        
        dates = []
        allResults = pandas.DataFrame()
        index = 0
        for i in range(2011,2017):
            for j in range(12):
                dateStr = str(i)+'-'+str(j+1)+'-01'
                result = HistoricPredictor(rutData, dateStr ).predict(100)
                allResults[str(index)] = result
                index=index+1
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()