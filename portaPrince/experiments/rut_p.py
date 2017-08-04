'''
Created on 3 Aug 2017

@author: moz
'''
import pandas
import matplotlib.pyplot as plt
import numpy

columnName = "Close"
rutdatafile = "../testData/indexes/RUT 2010-2017.csv"

def predict(data, startDate, n=100):
    result = data.set_index("Date").loc[startDate:][:n]
    
    return result.values[:,0]/result.values[0,0]*100

def create_heatmap( data ):
    id_column = 'day'
    print "data",  data.shape
    tall_pd = pandas.melt(data.reset_index(), id_vars=[id_column], value_vars=list(data), var_name='series', value_name='value')
    
    x = tall_pd[id_column].astype(float)
    y = tall_pd['value'].astype(float)
     
    heatmap, xedges, yedges = numpy.histogram2d(x, y, bins=[data.shape[0], 200])
    
    print "heatmap", heatmap.shape
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
 
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    #plt.colorbar()
     

if __name__ == "__main__":
        # read data
    pd = pandas.read_csv(rutdatafile, sep='\t', parse_dates=['Date'])
    pd[columnName].plot( grid=True)
            
    dates = []
    allResults = pandas.DataFrame(index=range(30))
    index = 0
    for i in range(2011,2016):
        for j in range(12):
            for k in range(27):
                dateStr = str(i)+'-'+str(j+1)+'-'+str(k+1)
                result = predict(pd, dateStr, 30)
                allResults['Series_'+str(index)] = result
                index=index+1

    # er der noget med takkerne i bunden?
#    allResults.plot( legend=False, grid=True, alpha=0.05 )    
    allResults.index.name="day"
#     
#     stacked = allResults.stack(new_col_name='value')
#     stacked.index.names=[u"day", u'serie']

    #print stacked
    #create_heatmap( allResults ):
    #print pandas.melt( stacked, id_vars=['day'], value_vars='value')
    
    #print stacked.pivot()
    
    create_heatmap(allResults)
    
    plt.show()
