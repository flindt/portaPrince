'''
Created on 20 Jul 2017

@author: flindt
'''
import unittest
from predictors.normal import NormalPredictor

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testNormalPredictor(self):
        myPredictor = NormalPredictor()
        
        result = myPredictor.predict(10)
        self.assertEqual(len(result), 10, "Wrong length of results returned...")
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNormalPredictor']
    unittest.main()