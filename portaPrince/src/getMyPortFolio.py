'''
Created on 21 May 2016

@author: flindt
'''

from pyalgotrade.tools import yahoofinance

from matplotlib import pyplot as plt
import numpy as np

myPortfolio = ['LYQ1.F','LYQ6.F','LYSX.F','L8I1.F'
                             , 'LYPX.F', 'LYM8.DE'
                             ]

def readCsvFiles(Portfolio, year):
    listOfNumbers = []
    for paper in Portfolio:
        fileName = paper + '-' + str(year) + '-yahoofinance.csv'
        dataFromThisFile = np.genfromtxt('/tmp/test/'+fileName, delimiter=',',skip_header=True)
        listOfNumbers.append(dataFromThisFile)
        
        print fileName, len(dataFromThisFile)
        print dataFromThisFile
        
    return listOfNumbers

def plotRelative(dataToPlot, axisToPlotOn):
    for dataSet in dataToPlot:
        x = np.arange(len(dataSet))
        axisToPlotOn.plot(x, dataSet)

    
    
def normalize(dataToNormalize, columnToNormalize=4):
    normalizedData = []
    for dataSet in dataToNormalize:
        firstPoint = dataSet[0,columnToNormalize]
        print firstPoint
        normalizedData.append(dataSet[:,columnToNormalize]/firstPoint)
        
    print normalizedData
    return normalizedData
  
def relativeData(dataToRelative):
    
    sumVector = np.sum(dataToRelative, axis=0)
    return dataToRelative / sumVector * 6
    

def fetchMyPortfolio():
    yahoofinance.build_feed(myPortfolio, 2000, 2016, '/tmp/test',skipErrors=True)

def errorDistance(data):
    target = np.ones(len(data[0]))
    result = np.zeros(len(data[0]))
    for set in data:
        result += (set - target)**2
    return np.sqrt(result)


if __name__ == '__main__':   
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
    plt.style.context('fivethirtyeight')
     
    dataList = readCsvFiles(myPortfolio, 2016)
    dataNormalised = normalize(dataList)
    plotRelative(dataNormalised, ax0)
    
    dataRelative = relativeData(dataNormalised)
    plotRelative( dataRelative, ax1 )
    
    error = errorDistance(dataRelative)
    x = np.arange(len(error))
    ax2.plot(x, error)
    
    plt.show()
    pass