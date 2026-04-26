import argparse
import sys
from datetime import datetime

from currencies.exchange_rate_factory import ExchangeRateFactory


def main() -> None:
    parser = argparse.ArgumentParser(description='Get CAD to USD or USD to CAD exchange rate.')
    parser.add_argument('start_currency', choices=('c', 'u'),
                        help='c: CAD to USD, u: USD to CAD')
    parser.add_argument('-m', '--annual_month_ending', nargs=1, type=lambda d: datetime.strptime(d, '%Y'),
                        help='the year for retrieving last day of 12 months (YYYY)')
    parser.add_argument('-d', '--single_date', nargs=1, type=lambda d: datetime.strptime(d, '%Y%m%d'),
                        help='the date for retrieving exchange rate (YYYYMMDD)')
    args = parser.parse_args()

    if bool(args.annual_month_ending) == bool(args.single_date):
        parser.error("One of -m or -d must be provided, but not both")

    try:
        converter = ExchangeRateFactory.get_currency_converter(args.start_currency)
        date_strategy = ExchangeRateFactory.get_date_strategy(
            args.single_date[0] if args.single_date else None,
            args.annual_month_ending[0] if args.annual_month_ending else None
        )

        # May use async calls if running as service
        date_strategy.get_exchange_rate(converter)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
