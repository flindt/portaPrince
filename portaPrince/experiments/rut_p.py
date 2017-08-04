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

def create_pmap( data, bins=200 ):
    ''' using numpy, takes the series, bins them and returns a matrix with the
        probability of a series being in that box
    '''
    id_column = 'day'
    tall_pd = pandas.melt(data.reset_index(), id_vars=[id_column], value_vars=list(data), var_name='series', value_name='value')
    
    x = tall_pd[id_column]
    y = tall_pd['value'].astype(float)
     
    heatmap, xedges, yedges = numpy.histogram2d(x, y, bins=[data.shape[0], bins])
 
    pd_hm = pandas.DataFrame( heatmap/data.shape[1] )
    pd_hm.columns=yedges[:-1]
    return pd_hm, yedges

def plot_pmap(df_heatmap, ysections, vmax=None ):
    extent = [0, df_heatmap.shape[0], ysections[0], ysections[-1]]
    df_reversed_col = df_heatmap[df_heatmap.columns[::-1]]
    
    plt.imshow(df_reversed_col.transpose(), aspect='auto', 
               cmap='jet', vmax=vmax, vmin=0,
               extent=extent )
    plt.colorbar()
    

if __name__ == "__main__":
    no_days = 30
        # read data
    pd = pandas.read_csv(rutdatafile, sep='\t', parse_dates=['Date'])
    #plt.figure()
    #pd[columnName].plot( grid=True)
            
    dates = []
    allResults = pandas.DataFrame(index=range(no_days))
    index = 0
    for i in range(2011,2016):
        for j in range(12):
            for k in range(27):
                dateStr = str(i)+'-'+str(j+1)+'-'+str(k+1)
                result = predict(pd, dateStr, no_days)
                allResults['Series_'+str(index)] = result
                index=index+1

    allResults.index.name="day"
    # er der noget med takkerne i bunden?
    #plt.figure()
    #allResults.plot( legend=False, grid=True, alpha=0.05 )    
#     
#     stacked = allResults.stack(new_col_name='value')
#     stacked.index.names=[u"day", u'serie']

    #print stacked
    #create_heatmap( allResults ):
    #print pandas.melt( stacked, id_vars=['day'], value_vars='value')
    
    #print stacked.pivot()
    #plt.figure()
    
    p_matrix, yedges = create_pmap(allResults)
    print p_matrix
    print p_matrix.transpose().describe()
    
    plot_pmap(p_matrix, yedges, vmax=170.0/1620 )

    plt.show()
    print "done"
