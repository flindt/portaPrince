'''
Created on 3 Aug 2017

@author: moz
'''
import pandas
import matplotlib.pyplot as plt
import numpy

columnName = "Close"
rutdatafile = "../testData/indexes/RUT 2010-2017.csv"
outputfilename = "pmap_RUT 2010-2017"

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
    
def generate_series( data, no_days=30 ):
    result = pandas.DataFrame(index=range(no_days))

    for i in range(data.shape[0]-no_days):
        extract = data[columnName][i:i+no_days].reset_index(drop=True)
        result["Series_%04d"%(i,)] = extract/extract.values[0]*100
        
    result.index.name="day"
    return result

if __name__ == "__main__":
    periods = [30, 60, 90, 120, 180, 360]
    
    # read data
    pd = pandas.read_csv(rutdatafile, sep='\t', parse_dates=['Date'])
    
    print pd
    pd[columnName].plot( grid=True)

    for no_days in periods:
        # create series        
        allResults = generate_series( pd, no_days )
        
        # er der noget med takkerne i bunden?
        print allResults
        allResults.plot( legend=False, grid=True, alpha=0.05 )    
        
        # creating and shoing pmap
        plt.figure()
         
        p_matrix, yedges = create_pmap(allResults)
        print p_matrix   
        plot_pmap(p_matrix, yedges, vmax=170.0/1620 )
    
        p_matrix.to_csv( outputfilename+"_%03d_days.csv"%(no_days), sep='\t')
    
    plt.show()
    print "done"
