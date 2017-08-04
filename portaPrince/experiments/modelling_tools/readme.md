modelling tools
===================

Der er lidt test data til snaity check

* linear_test_data.csv

    20 punkters linie.
    
 * random_normal.csv:
 
    1000 punkter normal fordelt tilfældige tal
     
 * sine_wave.csv:
 
 	1000 punkter perfekt sinus med masser af perioder

autocorr
-------------

Standard autokorrelering.

brug: `python autocorr.py <csv fil> <kolonenavn>`

e.g.
* `python autocorr.py linear_test_data.csv`
* `python autocorr.py random_normal.csv`
* `python autocorr.py sine_wave.csv`
