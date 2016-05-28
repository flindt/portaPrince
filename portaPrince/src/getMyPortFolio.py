'''
Created on 21 May 2016

@author: flindt
'''

from pyalgotrade.tools import yahoofinance

from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from matplotlib.widgets import MultiCursor
import numpy as np
import datetime as dt
import pandas as pd
import os

myPortfolio = ['LYQ1.F','LYQ6.F','LYSX.F','L8I1.F'
                             , 'LYPX.F', 'LYM8.DE'
                             , 'SPY1.F'
                             , 'VDE', 'VGT'
                             , 'BIV', 'VGLT'
                             , 'VNR', 'VOO'
                             , 'VOOG'
                             , 'SC0D.F'
                             #, 'LYPL.F'
                             ]
                             
myPortfolio2 = ['LYQ1.F','LYQ6.F','LYSX.F','L8I1.F'
                             , 'LYPX.F', 'LYM8.DE'
                             , 'SC0D.F', 'SPY1.F'
                             , 'VDE', 'VGT'
                             ]
                             
dataDir = "data/"

def readCsvFiles(Portfolio, year):
    listOfNumbers = []
    pandaTotal = None
    for paper in Portfolio:
        fileName = paper + '-' + str(year) + '-yahoofinance.csv'
        dataFromThisFile = np.genfromtxt(dataDir+fileName, delimiter=',', names=True,dtype=None, converters={'Date': lambda x: dt.datetime.strptime(x, '%Y-%m-%d')})
        listOfNumbers.append(dataFromThisFile)
        pandaFrame = pd.read_csv(dataDir+fileName,index_col=0, parse_dates=True)
        pandaFrame.columns = pd.MultiIndex.from_product([[paper],[u'Open', u'High', u'Low', u'Close', u'Volume',u'Adj Close']])
        
        if pandaTotal is None:
            pandaTotal = pandaFrame
        else:
            print pandaFrame.head(2)
            pandaTotal = pandaTotal.join(pandaFrame, how='outer')
        
    pandaTotal = pandaTotal.fillna(method='pad', inplace=False)
    newList = {}
    for paper in pandaTotal.columns.levels[0]:
        newList[paper] = pandaTotal[paper]['Close']
        
        print newList
    return newList, pandaTotal

def plotRelative(dataToPlot, axisToPlotOn):
    plots = []
    for dataSet in dataToPlot:
        plots.append( axisToPlotOn.plot(dataToPlot[dataSet], label=dataSet) )
    
    handles, labels = axisToPlotOn.get_legend_handles_labels()
    labels = myPortfolio
    axisToPlotOn.legend(handles, labels 
                        , loc='upper left',
                        bbox_to_anchor = [1, 1],
                        shadow = True)    
    
def plot1Date(dataToPlot, axisToPlotOn):
    x = dataToPlot[0]
    for dataSet in dataToPlot[1]:
        axisToPlotOn.plot(x, dataSet, picker=5)
    
def normalize(dataToNormalize, columnToNormalize='Close', dateToUse=None):
    normalizedData = {}
    if dateToUse is None:
        index100 = 0
    for dataSet in dataToNormalize:
        firstPoint = dataToNormalize[dataSet][index100]
        normalizedData[dataSet] = dataToNormalize[dataSet]/firstPoint
        
    return normalizedData
  
def relativeData(dataToRelative):
    dataLocalList = []
    for dataSet in dataToRelative:
        dataLocalList.append(dataSet[1])
    sumVector = np.sum(dataLocalList, axis=0)
    resultVector = dataLocalList / sumVector * 8
    return [dataSet[0],resultVector]
    

def fetchMyPortfolio():
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)

    yahoofinance.build_feed(myPortfolio, 2000, 2016, dataDir,skipErrors=True)

def errorDistance(data):
    target = np.ones(len(data[0]))
    result = np.zeros(len(data[0]))
    for dataSet in data:
        result += (dataSet - target)**2
    return np.sqrt(result)


def setUpPlotRelative():
    # import constants for the days of the week
    from matplotlib.dates import SA, SU

    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, sharex=True)
    plt.style.context('fivethirtyeight')
    
    #years = mdates.YearLocator()    
    #months = mdates.MonthLocator()
    #weeks = mdates.WeekdayLocator()
    
    #weeksFmt = mdates.DateFormatter('%d')
    #ax1.xaxis.set_major_formatter(weeksFmt)
    
    #ax1.xaxis.set_major_locator(months)
    #ax1.xaxis.set_minor_locator(weeks)
    #ax1.grid(which='minor', axis='x')
    
    return (ax0, ax1, ax2)

def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    print 'onpick points:', zip(xdata[ind], ydata[ind])


def analyseRelative(year, portfolio):
    (ax0, ax1, ax2) = setUpPlotRelative()
     
    dataList, pandaFrame = readCsvFiles(portfolio, year)
    dataNormalised = normalize(dataList)
    plotRelative(dataNormalised, ax0)
    
    dataRelative = relativeData(dataNormalised)
    plot1Date(dataRelative, ax1 )
    
    error = errorDistance(dataRelative[1])
    ax2.plot(dataRelative[0], error)


if __name__ == '__main__':    
    analyseRelative(2016, myPortfolio)
    
    plt.show(block=True)
