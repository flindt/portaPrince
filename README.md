# portaPrince

We use [pyAlgoTrade](http://gbeced.github.io/pyalgotrade/) for this project, and it has [nice documentation](http://gbeced.github.io/pyalgotrade/docs/v0.17/html/).

To run use
----------

Update/download the data

    `python downloadPortfolio.py`

Run the "main" program

    `python getMyPortFolio.py`
  

Troubleshooting
------------------

### pyalgotrade missing

You get the error

    `ImportError: No module named pyalgotrade.tools` when running the program:
  
solution

    install the module (as root): `pip install pyalgotrade`

### missing data

When running the main program your get

    `IOError: data/<somefile>.csv not found.`

solution

    run the download script: `python downloadPortfolio.py`
