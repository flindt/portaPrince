'''
Created on 20 Jul 2017

@author: flindt
'''
import unittest
from predictors.historic import HistoricPredictor


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testInit(self):
        import pandas
        rutData = pandas.read_csv("../../testData/indexes/RUT 2010-2017.csv", sep='\t',parse_dates=['Date'])
        myPred = HistoricPredictor(rutData, pandas.Timestamp("2014-01-01") )
        result = myPred.predict(10)
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()