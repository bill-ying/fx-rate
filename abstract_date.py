from abc import ABC, abstractmethod
from datetime import datetime


from abstract_currency import AbstractCurrency


START_DATE = '?start_date='
END_DATE = '&end_date='
OBSERVATIONS = 'observations'


class AbstractDate(ABC):

    def __init__(self, date_to_lookup: datetime):
        self._date: datetime = date_to_lookup
        super().__init__()

    @abstractmethod
    def get_exchange_rate(self, currency: AbstractCurrency):
        pass

    @staticmethod
    def _print_rate(rate_for_date):
        rate_key = list(filter(lambda x: x != 'd', rate_for_date))[0]
        print(rate_for_date['d'], rate_for_date[rate_key]['v'])