from abstract_currency import AbstractCurrency


class CadToUsd(AbstractCurrency):

    def __init__(self):
        super().__init__()

    def _bank_of_canada_series_name(self):
        return 'FXCADUSD'
