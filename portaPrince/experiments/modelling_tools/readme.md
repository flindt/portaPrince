modelling tools
===================

Der er lidt test data til snaity check

* linear_test_data.csv

    20 punkters linie.
    
 * random_normal.csv:
 
    1000 punkter normal fordelt tilfældige tal
     
 * sine_wave.csv:
 
 	1000 punkter perfekt sinus med masser af perioder

I hver .py fil er der mindst to funktioner, en til datamanipulation og en til at plotte.

autocorr
-------------

Standard autokorrelering.

Fra kommando linien: `python autocorr.py <csv fil> <kolonenavn>`

e.g.
* `python autocorr.py linear_test_data.csv`
	
    viser at der er struktur, men ikke perioder
    
* `python autocorr.py random_normal.csv`

    viser at der ikke er struktur
    
* `python autocorr.py sine_wave.csv`

    viser struktur og at periode tiden er ca 6 (dvs. 2*pi)


gradients
---------------

tilføjer gradient kolonner, dvs. 1. og 2. afledte

Fra kommando linien: `python gradients.py <csv fil> <kolonenavn>`

e.g.
* `python gradients.py linear_test_data.csv`
	
    viser at der er struktur, men ikke perioder
    
* `python gradients.py random_normal.csv`

    viser at der ikke er struktur
    
* `python gradients.py sine_wave.csv`

    viser struktur og at periode tiden er ca 6 (dvs. 2*pi)

  
Internt er der også mulighed for at lave v og a kolonerne relative, dvs. 1/y*dy/dx istedet for dy/dx