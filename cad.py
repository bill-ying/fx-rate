from abstract_currency import AbstractCurrency


class Cad(AbstractCurrency):

    def __init__(self):
        super().__init__()

    def _bank_of_canada_series_name(self):
        return 'FXCADUSD'
