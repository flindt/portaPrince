'''
Created on 20 Jul 2017

@author: moozer
'''
import unittest
from strategies.AlwaysBuy import AlwaysBuy

simpleTestpriceFile = "date/price_simple.csv"


class MockPredictor( object):
    _result = None
    def setResult( self, result ):
        self._result = result

    def getPrices( self, size ):
        return self._result


class Test(unittest.TestCase):

    def setUp(self):
        self.p = MockPredictor()
        #p.setResult( testResult )
        pass


    def tearDown(self):
        pass


    def testInit(self):
        s = AlwaysBuy( predictor = self.p )
        self.assertEqual(s.predictor, self.p)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
