'''
Created on 21 May 2016

@author: flindt
'''

from pyalgotrade.tools import yahoofinance

from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import numpy as np
import datetime as dt

myPortfolio = ['LYQ1.F','LYQ6.F','LYSX.F','L8I1.F'
                             , 'LYPX.F', 'LYM8.DE'
                             ]

def readCsvFiles(Portfolio, year):
    listOfNumbers = []
    convertfunc = lambda x: dt.datetime.strptime(x, '%Y-%m-%d')
    for paper in Portfolio:
        fileName = paper + '-' + str(year) + '-yahoofinance.csv'
        dataFromThisFile = np.genfromtxt('/tmp/test/'+fileName, delimiter=',', names=True,dtype=None, converters={'Date': convertfunc})
        listOfNumbers.append(dataFromThisFile)
        
        print dataFromThisFile['Close']
        print fileName, len(dataFromThisFile)
        
    return listOfNumbers

def plotRelative(dataToPlot, axisToPlotOn):
    for dataSet in dataToPlot:
        axisToPlotOn.plot(dataSet[0], dataSet[1])

def plot1Date(dataToPlot, axisToPlotOn):
    x = dataToPlot[0]
    for dataSet in dataToPlot[1]:
        axisToPlotOn.plot(x, dataSet)
    
def normalize(dataToNormalize, columnToNormalize='Close'):
    normalizedData = []
    for dataSet in dataToNormalize:
        firstPoint = dataSet[columnToNormalize][-1]
        print firstPoint
        normalizedData.append([dataSet['Date'], dataSet[columnToNormalize]/firstPoint])
        
    print normalizedData
    return normalizedData
  
def relativeData(dataToRelative):
    dataLocalList = []
    for dataSet in dataToRelative:
        dataLocalList.append(dataSet[1])
    sumVector = np.sum(dataLocalList, axis=0)
    resultVector = dataLocalList / sumVector * 6
    return [dataSet[0],resultVector]
    

def fetchMyPortfolio():
    yahoofinance.build_feed(myPortfolio, 2000, 2016, '/tmp/test',skipErrors=True)

def errorDistance(data):
    target = np.ones(len(data[0]))
    result = np.zeros(len(data[0]))
    for dataSet in data:
        result += (dataSet - target)**2
    return np.sqrt(result)


def setUpPlot():
    # import constants for the days of the week
    from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, sharex=True)
    plt.style.context('fivethirtyeight')
    
    years = mdates.YearLocator()    
    months = mdates.MonthLocator()
    weeks = mdates.WeekdayLocator(byweekday=(SU, SA))
    
    weeksFmt = mdates.DateFormatter('%d')
    ax1.xaxis.set_major_formatter(weeksFmt)
    
    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_minor_locator(weeks)
    ax1.grid(which='both', axis='x')
    
    return (ax0, ax1, ax2)

if __name__ == '__main__':   
    (ax0, ax1, ax2) = setUpPlot()
     
    dataList = readCsvFiles(myPortfolio, 2016)
    dataNormalised = normalize(dataList)
    plotRelative(dataNormalised, ax0)
    
    dataRelative = relativeData(dataNormalised)
    plot1Date(dataRelative, ax1 )
    
    error = errorDistance(dataRelative[1])
    ax2.plot(dataRelative[0], error)
    
    plt.show(block=True)
    pass