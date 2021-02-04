import pandas as pd
import requests
from keys import *

stocks = pd.read_csv('sp_500_stocks.csv')

def chunks(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

symbol_groups = list(chunks(stocks['Ticker'], 100))
symbol_strings = []
for i in range(0, len(symbol_groups)):
  symbol_strings.append(','.join(symbol_groups[i]))

rv_columns = [
  'Ticker',
  'Price',
  'P/E Ratio',
  'Price to Book Ratio',
  'Price to Sales Ratio',
  'Percentage Change (1-Month)',
  'Percentage Change (3-Month)',
  'Percentage Change (6-Month)',
  'Percentage Change (1-Year)',
  'Percentage Change (5-Years)',
  'Percentage Change (Max)',
]

rv_dataframe = pd.DataFrame(columns = rv_columns)

for symbol_string in symbol_strings:
  batch_api_call = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=quote,stats,advanced-stats&token={CLOUD_API_KEY}'
  data = requests.get(batch_api_call).json()
  for symbol in symbol_string.split(','):
      rv_dataframe = rv_dataframe.append(
      pd.Series(
        [
          symbol,
          data[symbol]['quote']['latestPrice'],
          data[symbol]['quote']['peRatio'],
          data[symbol]['advanced-stats']['priceToBook'],
          data[symbol]['advanced-stats']['priceToSales'],
          data[symbol]['stats']['month1ChangePercent'],
          data[symbol]['stats']['month3ChangePercent'],
          data[symbol]['stats']['month6ChangePercent'],
          data[symbol]['stats']['year1ChangePercent'],          
          data[symbol]['stats']['year5ChangePercent'],
          data[symbol]['stats']['maxChangePercent'],
        ],
        index = rv_columns
      ),
      ignore_index = True
    )
