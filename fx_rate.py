import argparse
import sys
from datetime import datetime


from Usd import Usd
from cad import Cad
from month_end import MonthEnd
from single_day import SingleDay


BOC_API_LINK = 'https://www.bankofcanada.ca/valet//observations/'


def main(currency, **kwargs):
    to_convert = Cad() if currency == 'c' else Usd()
    month_ending = kwargs['month_ending']
    lookup_date = MonthEnd(month_ending[0]) if month_ending else SingleDay(kwargs['single_date'][0])
    lookup_date.get_exchange_rate(to_convert)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get CAD to USD or USD to CAD exchange rate for a specific date '
                                                 'and last day of 12 months of a year.')
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
