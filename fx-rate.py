import argparse
import sys
from datetime import datetime

import requests

BOC_API_LINK = 'https://www.bankofcanada.ca/valet//observations/'

def main(*args, **kwargs):
    month_ending = kwargs['month_ending']
    single_date = kwargs['single_date']

    if args[0] == 'c':
        url = BOC_API_LINK + 'FXCADUSD'
    else:
        url = BOC_API_LINK + 'FXUSDCAD'

    exchange_response = requests.get(url).json()
    first_available_date = exchange_response['observations'][0]['d']
    first_available_year = first_available_date.split('-')[0]
    last_available_date = exchange_response['observations'][-1]['d']
    last_available_year = last_available_date.split('-')[0]

    if month_ending:
        temp_year = str(month_ending[0].year)

        if first_available_year > temp_year or last_available_year < temp_year:
            print('No month end data available for ' + temp_year)
        else:
            for i in range(1, 13):
                rates_for_months = list(filter(lambda x: x['d'].startswith(f'{temp_year}-{i:02}'),
                                         exchange_response['observations']))

                if len(rates_for_months):
                    _printRate(rates_for_months[-1])
                else:
                    break
    else:
        temp_date = single_date[0].strftime('%Y-%m-%d')
        rate_for_date = list(filter(lambda x: x['d'] == temp_date, exchange_response['observations']))

        if len(rate_for_date):
            _printRate(rate_for_date[0])
        else:
            print("No data available for " + temp_date)

def _printRate(rate_for_date):
    rate_key = list(filter(lambda x: x != 'd', rate_for_date))[0]
    print(rate_for_date['d'], rate_for_date[rate_key]['v'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description
                                     ='Get CAD to USD or USD to CAD exchange rate for a specific date and last day '
                                      'of 12 months of a year.')
    parser.add_argument('start_currency', choices=('c', 'u'),
                        help='only two options available "c" or "U".  If "c" is provided, the exchange rate will be '
                             'CAD to USD.  If "u" is provided, the exchange rate will be USD to DAD')
    parser.add_argument('-m', '--annual_month_ending', nargs=1, type=lambda d: datetime.strptime(d, '%Y'),
                        help='the year for retrieve last day of 12 months exchange rate in yyyy format')
    parser.add_argument('-d', '--single_date', nargs=1, type=lambda d: datetime.strptime(d, '%Y%m%d'),
                        help='the date for exchange rate in yyyyMMdd format')
    args = parser.parse_args()

    if not args.annual_month_ending and not args.single_date:
        parser.error("One of --annual_month_ending or --single_date must be given")

    sys.exit(main(args.start_currency, month_ending=args.annual_month_ending, single_date=args.single_date))
