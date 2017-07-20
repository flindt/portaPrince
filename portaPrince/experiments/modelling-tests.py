#
#
# links
# correlation issues: https://stackoverflow.com/questions/15854878/correlation-between-columns-in-dataframe
#
# graf: https://tomaugspurger.github.io/modern-7-timeseries.html

import pandas as pd
from pandas.tools.plotting import autocorrelation_plot
import matplotlib.pyplot as plt
import numpy as np


def df_autocorr(df, lag=1, axis=0):
    """Compute full-sample column-wise autocorrelation for a DataFrame."""
    return df.apply(lambda col: col.autocorr(lag), axis=axis)

def df_rolling_autocorr(df, window, lag=1):
    """Compute rolling column-wise autocorrelation for a DataFrame."""

    return (df.rolling(window=window)
        .corr(df.shift(lag))) # could .dropna() here

def plot_autocorr( df ):
    delta_autocorr = pd.Series( df.autocorr( lag=i) for i in range( entries_count)).fillna(0)
    delta_autocorr.plot()
    plt.show()
    plt.close()
    return delta_autocorr


rutData = pd.read_csv("../testData/indexes/RUT 2010-2017.csv", sep='\t' ,parse_dates=['Date']).filter(['Date', 'Close'])
rutData['Delta'] = rutData.Close.diff().shift(-1)
#rutData['DeltaRelative'] = rutData.Delta / rutData.Close

print(rutData['Delta'].shape)
entries_count = rutData['Delta'].shape[0]

print( rutData['Delta'] )
delta_autocorr = plot_autocorr( rutData['Delta'] )

#plt.show()
#print (rutData)

#bootstrap_plot(rutData[''], size=50, samples=500, color='grey')
#print( rutData)


# plt.figure()
# #autocorrelation_plot(rutData['Close'])
# autocorrelation_plot(rutData['Delta'])
# #plt.plot( rutData['Close'] )
# #plt.plot( rutData['Delta'] )
# #rutData['Delta'].plot()
plt.show()
plt.close()
