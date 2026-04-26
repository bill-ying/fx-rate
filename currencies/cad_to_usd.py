from .abstract_currency import AbstractCurrency


class CadToUsd(AbstractCurrency):

    @property
    def _bank_of_canada_series_name(self) -> str:
        return 'FXCADUSD'
