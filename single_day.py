from datetime import datetime


from abstract_currency import AbstractCurrency
from abstract_date import AbstractDate, START_DATE, END_DATE, OBSERVATIONS


class SingleDay(AbstractDate):

    def __init__(self, date_to_lookup: datetime):
        super().__init__(date_to_lookup)

    def get_exchange_rate(self, currency: AbstractCurrency):
        temp_date = self._date.strftime('%Y-%m-%d')
        bank_of_canada_response = currency.get_bank_of_canada_response(START_DATE + temp_date + END_DATE + temp_date)
        rate_for_date = list(filter(lambda x: x['d'] == temp_date, bank_of_canada_response[OBSERVATIONS]))

        if len(rate_for_date):
            AbstractDate._print_rate(rate_for_date[0])
        else:
            print("No data available for " + temp_date)
