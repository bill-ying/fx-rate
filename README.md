# fx_rate

Get the exchange rate between Canadian dollar and US dollar from Bank of Canada.  The exchange rate can be retrieved in one of following ways:
- for a specific date
- for the last Bank of Canada business day of each month of a specific year

The program takes one required argument, start_currency, which can be one of following two values:
- c for CAD -> USD
- u for USD -> CAD

It also takes one of the following two optional arguments:
- -d for a specific date in yyyymmdd format
- -m for a specific year in yyyy format

This program depends on package "requests".

Examples:
- To retrieve the exchange rate from CAD to USD on 2021-03-31:
  - python fx_rate.py c -d 20210331
  
- To retrieve the exchange rates from USD to CAD for the last Bank of Canada business day of each month in 2020:
  - python fx_rate.py u -m 2020


The source code includes the necessary files to create a docker image. The docker image of this program can be pulled from docker hub:

https://hub.docker.com/r/billying/fx-rate

Example of running docker container:

 - docker run billying/fx-rate c -d 20210331
 - docker run billying/fx-rate u -m 2020