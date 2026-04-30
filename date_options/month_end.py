from datetime import datetime


from currencies.abstract_currency import AbstractCurrency
from .abstract_date import AbstractDate, START_DATE, END_DATE, OBSERVATIONS


class MonthEnd(AbstractDate):

    def __init__(self, date_to_lookup: datetime) -> None:
        super().__init__(date_to_lookup)

    def get_exchange_rate(self, currency: AbstractCurrency) -> None:
        year = str(self._date.year)
        bank_of_canada_response = currency.get_bank_of_canada_response(START_DATE + year + '-01-01' + END_DATE +
                                                                       year + '-12-31')
        observations = bank_of_canada_response.get(OBSERVATIONS, [])

        if not observations:
            print('No month end data available for ' + year)
        else:
            for i in range(1, 13):
                rates_for_months = list(filter(lambda x: x['d'].startswith(f'{year}-{i:02}'),
                                               observations))

                if len(rates_for_months):
                    AbstractDate._print_rate(rates_for_months[-1])
                else:
                    break
