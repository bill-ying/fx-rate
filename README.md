# fx-rate

Get the exchange rate between Canadian dollar and US dollar from Bank of Canada.  The exchange rate(s) can be retrieved in one of following ways:
- for a specific date
- for the last Bank of Canada business day of each month of a specific year

The program takes one required argument, start_currency, which can be one of following two values:
- c for CAD -> USD
- u for USD -> CAD

It also takes one of the following two optional parameters:
- -d for a specific date in yyyyMMdd format
- -m for a specific year in yyyy format

This program depends on package "requests".

Examples:
- To retrieve the exchange rate from CAD to USD on 2021-03-31:
  python fx-rate.py c -d 20210331
  
- To retrieve the exchange rates from USD to CAD for the last Bank of Canada business day of each month for 2020:
  python fx-rate.py u -m 2020