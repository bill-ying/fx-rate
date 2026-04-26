from typing import Optional
from datetime import datetime

from .abstract_currency import AbstractCurrency
from .usd_to_cad import UsdToCad
from .cad_to_usd import CadToUsd
from date_options.abstract_date import AbstractDate
from date_options.month_end import MonthEnd
from date_options.single_day import SingleDay

class ExchangeRateFactory:
    @staticmethod
    def get_currency_converter(currency_code: str) -> AbstractCurrency:
        if currency_code == 'c':
            return CadToUsd()
        elif currency_code == 'u':
            return UsdToCad()
        else:
            raise ValueError("Invalid currency code. Use 'c' for CAD to USD or 'u' for USD to CAD.")

    @staticmethod
    def get_date_strategy(single_date: Optional[datetime], month_ending: Optional[datetime]) -> AbstractDate:
        if month_ending:
            return MonthEnd(month_ending)
        if single_date:
            return SingleDay(single_date)
        raise ValueError("Either single_date or annual_month_ending must be provided.")