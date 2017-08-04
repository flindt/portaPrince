'''
Created on 3 Aug 2017

@author: moz
'''
import pandas
import matplotlib.pyplot as plt
import numpy
import matplotlib.colors as colors

columnName = "Close"
rutdatafile = "../testData/indexes/RUT 2010-2017.csv"

def predict(data, startDate, n=100):
    result = data.set_index("Date").loc[startDate:][:n]
    
    return result.values[:,0]/result.values[0,0]*100

def create_heatmap( data, bins=200 ):
    ''' using numpy, takes the series, bins them and returns a matrix with the
        probability of a series being in that box
    '''
    id_column = 'day'
    tall_pd = pandas.melt(data.reset_index(), id_vars=[id_column], value_vars=list(data), var_name='series', value_name='value')
    
    x = tall_pd[id_column]
    y = tall_pd['value'].astype(float)
     
    heatmap, xedges, yedges = numpy.histogram2d(x, y, bins=[data.shape[0], bins])
 
    pd_hm = pandas.DataFrame( heatmap/data.shape[1] )
    pd_hm.columns=["%.1f"%(x,) for x in yedges[:-1]]
    return pd_hm, yedges

def plot_heatmap(df_heatmap ):
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    plt.imshow(df_heatmap, interpolation='none', 
               cmap='jet', vmax=170.0/1620)
    #plt.xlim=(xedges[0], xedges[-1])
    plt.colorbar()
    

if __name__ == "__main__":
        # read data
    pd = pandas.read_csv(rutdatafile, sep='\t', parse_dates=['Date'])
    plt.figure()
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
    plt.figure()
    allResults.plot( legend=False, grid=True, alpha=0.05 )    
    allResults.index.name="day"
#     
#     stacked = allResults.stack(new_col_name='value')
#     stacked.index.names=[u"day", u'serie']

    #print stacked
    #create_heatmap( allResults ):
    #print pandas.melt( stacked, id_vars=['day'], value_vars='value')
    
    #print stacked.pivot()
    #plt.figure()
    
    p_matrix, yedges = create_heatmap(allResults)
    print p_matrix
    
    plt.show()
