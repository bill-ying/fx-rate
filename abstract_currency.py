from abc import ABC, abstractmethod


import requests


class AbstractCurrency(ABC):

    bank_of_canada_link = 'https://www.bankofcanada.ca/valet/observations/'

    @property
    @abstractmethod
    def _bank_of_canada_series_name(self):
        pass

    def __init__(self):
        super().__init__()

    def get_bank_of_canada_response(self, date_range=''):
        url = AbstractCurrency.bank_of_canada_link + self._bank_of_canada_series_name() + date_range
        return requests.get(url).json()
