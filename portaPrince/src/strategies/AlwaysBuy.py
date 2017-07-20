class AlwaysBuy( object ):
    _predictor=None
    def __init__(self, predictor ):
        self._predictor=predictor
        pass
    
    @property
    def predictor(self):
        return self._predictor