import argparse
import sys
from datetime import datetime

import requests

BOC_API_LINK = 'https://www.bankofcanada.ca/valet//observations/'


def main(*args, **kwargs):
    url = BOC_API_LINK + ('FXCADUSD' if args[0] == 'c' else 'FXUSDCAD')
    bank_of_canada_response = requests.get(url).json()
    month_ending = kwargs['month_ending']

    if month_ending:
        _last_day_of_month_rates(month_ending, bank_of_canada_response)
    else:
        _specific_day_rate(kwargs['single_date'], bank_of_canada_response)


def _specific_day_rate(input_date, bank_of_canada_response):
    temp_date = input_date[0].strftime('%Y-%m-%d')
    rate_for_date = list(filter(lambda x: x['d'] == temp_date, bank_of_canada_response['observations']))

    if len(rate_for_date):
        _print_rate(rate_for_date[0])
    else:
        print("No data available for " + temp_date)


def _last_day_of_month_rates(month_ending, bank_of_canada_response):
    year = str(month_ending[0].year)
    first_available_year = bank_of_canada_response['observations'][0]['d'].split('-')[0]
    last_available_year = bank_of_canada_response['observations'][-1]['d'].split('-')[0]

    if first_available_year > year or last_available_year < year:
        print('No month end data available for ' + year)
    else:
        for i in range(1, 13):
            rates_for_months = list(filter(lambda x: x['d'].startswith(f'{year}-{i:02}'),
                                           bank_of_canada_response['observations']))

            if len(rates_for_months):
                _print_rate(rates_for_months[-1])
            else:
                break


def _print_rate(rate_for_date):
    rate_key = list(filter(lambda x: x != 'd', rate_for_date))[0]
    print(rate_for_date['d'], rate_for_date[rate_key]['v'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description
                                     ='Get CAD to USD or USD to CAD exchange rate for a specific date and last day '
                                      'of 12 months of a year.')
    parser.add_argument('start_currency', choices=('c', 'u'),
                        help='only two options available "c" or "u".  If "c" is provided, the exchange rate will be '
                             'CAD to USD.  If "u" is provided, the exchange rate will be USD to DAD')
    parser.add_argument('-m', '--annual_month_ending', nargs=1, type=lambda d: datetime.strptime(d, '%Y'),
                        help='the year for retrieving last day of 12 months exchange rate in yyyy format')
    parser.add_argument('-d', '--single_date', nargs=1, type=lambda d: datetime.strptime(d, '%Y%m%d'),
                        help='the date for retrieving exchange rate in yyyyMMdd format')
    input_args = parser.parse_args()

    if not input_args.annual_month_ending and not input_args.single_date:
        parser.error("One of -m or -d must be provided")

    sys.exit(main(input_args.start_currency, month_ending=input_args.annual_month_ending,
                  single_date=input_args.single_date))
