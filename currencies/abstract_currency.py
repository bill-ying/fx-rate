
import httpx
from abc import ABC, abstractmethod

class AbstractCurrency(ABC):
    bank_of_canada_link = 'https://www.bankofcanada.ca/valet/observations/'

    @property
    @abstractmethod
    def _bank_of_canada_series_name(self) -> str:
        pass

    def get_bank_of_canada_response(self, date_range: str = '') -> dict:
        with httpx.Client() as client:
            url = f"{self.bank_of_canada_link}{self._bank_of_canada_series_name()}{date_range}"
            response = client.get(url)
            response.raise_for_status()
            return response.json()
