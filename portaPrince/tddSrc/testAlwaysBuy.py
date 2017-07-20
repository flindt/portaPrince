'''
Created on 20 Jul 2017

@author: moozer
'''
import unittest
import pandas
from strategies.AlwaysBuy import AlwaysBuy

TestpriceFileA = "data/price_data_A.csv"
TestParamA = {'Return': 100, 'Upper': 120, 'Lower': 80, "Risk": 1000, 'Fee': 20}
TestResultA = {'Result': 80}


class MockPredictor( object):
    _result = None
    def setResult( self, result ):
        self._result = result

    def getPrices( self, size ):
        return self._result

class Test(unittest.TestCase):

    def setUp(self):
        self.p = MockPredictor()
        pass

    def tearDown(self):
        pass

    def testInit(self):
        s = AlwaysBuy( predictor = self.p )
        self.assertEqual(s.predictor, self.p)
        pass

    def testResult(self):
        s = AlwaysBuy(  predictor = self.p )
        priceData = pandas.read_csv(TestpriceFileA, sep='\t')
        self.p.setResult( priceData )
        result = s.getResult( TestParamA )
        self.assertEqual(result, TestResultA['Result'] )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
