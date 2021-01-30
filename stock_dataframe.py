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
  'Shares to Buy',
  'P/E Ratio',
  'P/E Percentile',
  'Price to Book Ratio',
  'PB Percentile',
  'Price to Sales Ratio',
  'PS Percentile',
  'EV/EBITDA',
  'EV/EBITDA Percentile',
  'EV/GP',
  'EV/GP Percentile',
  'RV Score',
]

for symbol_string in symbol_strings:
  batch_api_call = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=quote,advanced-stats&token={IEX_CLOUD_API_TOKEN}'
  data = requests.get(batch_api_call).json()
  for symbol in symbol_string.split(','):
      rv_dataframe = rv_dataframe.append(
      pd.Series(
        [
          symbol,
          data[symbol]['quote']['latestPrice'],
          0.0,
          data[symbol]['quote']['peRatio'],
          0.0,
          data[symbol]['advanced-stats']['priceToBook'],
          0.0,
          data[symbol]['advanced-stats']['priceToSales'],
          0.0,
          ev_to_ebitda,
          0.0,
          ev_to_gp,
          0.0,
          0.0,
        ],
        index = rv_columns
      ),
      ignore_index = True
    )