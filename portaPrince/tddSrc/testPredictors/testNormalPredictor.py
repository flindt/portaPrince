'''
Created on 20 Jul 2017

@author: flindt
'''
import unittest
from predictors.normal import NormalPredictor

import pandas

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testNormalPredictor(self):
        myPredictor = NormalPredictor()
        
        result = myPredictor.predict(10)
        self.assertEqual(len(result), 10, "Wrong length of results returned...")
        
    def testNormalMany(self):
        myPredictor = NormalPredictor()
        
        allResults = pandas.DataFrame()
        for i in range(11):
            result = myPredictor.predict(100)
            allResults[str(i)] = result
            
        pass
            
    def testDumpToCSV(self):
        myPredictor = NormalPredictor()
        
        for i in range(10):
            result = myPredictor.predict(100)
            result.to_csv("../../tddSrc/data/random/normal_"+str(i)+".csv", sep="\t")
        
        pass 
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNormalPredictor']
    unittest.main()