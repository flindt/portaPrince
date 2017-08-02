class AlwaysBuy( object ):
    _predictor=None
    def __init__(self, predictor ):
        self._predictor=predictor
        pass
    
    @property
    def predictor(self):
        return self._predictor
    
    def getResult(self, params, runPeriodDays = 25):
        
        endPrice = self._predictor.getPrices( size=runPeriodDays )[runPeriodDays-1]
        
        if endPrice > params['Upper'] or endPrice < params['Lower']:
            return params['Return'] - params['Risk'] - params['Fee']
        else:
            return params['Return'] - params['Fee']