'''
Created on 3 Aug 2017

@author: moz
'''
import pandas
import matplotlib.pyplot as plt
import numpy

columnName = "Close"
rutdatafile = "../testData/indexes/RUT 2010-2017.csv"

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
    
    print pd
    pd[columnName].plot( grid=True)
    
    # create series        
    allResults = pandas.DataFrame(index=range(no_days))
    for i in range(pd.shape[0]-no_days):
        extract = pd[columnName][i:i+no_days].reset_index(drop=True)
        allResults["Series_%04d"%(i,)] = extract/extract.values[0]*100
        
    allResults.index.name="day"

    # er der noget med takkerne i bunden?
    print allResults
    allResults.plot( legend=False, grid=True, alpha=0.05 )    
    
    # creating and shoing pmap
    plt.figure()
     
    p_matrix, yedges = create_pmap(allResults)
    print p_matrix   
    plot_pmap(p_matrix, yedges, vmax=170.0/1620 )

    plt.show()
    print "done"
