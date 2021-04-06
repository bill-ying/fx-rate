from datetime import datetime


from abstract_currency import AbstractCurrency
from abstract_date import AbstractDate, START_DATE, END_DATE, OBSERVATIONS


class MonthEnd(AbstractDate):

    def __init__(self, date_to_lookup: datetime):
        super().__init__(date_to_lookup)

    def get_exchange_rate(self, currency: AbstractCurrency):
        year = str(self._date.year)
        bank_of_canada_response = currency.get_bank_of_canada_response(START_DATE + year + '-01-01' + END_DATE +
                                                                       year + '-12-31')
        first_available_year = bank_of_canada_response[OBSERVATIONS][0]['d'].split('-')[0]
        last_available_year = bank_of_canada_response[OBSERVATIONS][-1]['d'].split('-')[0]

        if first_available_year > year or last_available_year < year:
            print('No month end data available for ' + year)
        else:
            for i in range(1, 13):
                rates_for_months = list(filter(lambda x: x['d'].startswith(f'{year}-{i:02}'),
                                               bank_of_canada_response[OBSERVATIONS]))

                if len(rates_for_months):
                    AbstractDate._print_rate(rates_for_months[-1])
                else:
                    break
