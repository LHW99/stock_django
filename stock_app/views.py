from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from keys import *
import requests
import pyEX as p
#api_call = p.Client(api_token=CLOUD_API_KEY, version='sandbox')

def index(request):
  symbol = 'AAPL'
  response = requests.get(f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol}&types=quote,advanced-stats&token={CLOUD_API_KEY}')
  data = response.json()

  if request.method == 'GET':
    try:
      ticker = request.GET['ticker_search']
      symbol = ticker.upper()
      response = requests.get(f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol}&types=quote,advanced-stats&token={CLOUD_API_KEY}')
      data = response.json()

      return render(request, 'index.html', {
      'companyName': data[symbol]['quote']['companyName'],
      'symbol': symbol,
      'latestPrice': data[symbol]['quote']['latestPrice'],
      'peRatio': data[symbol]['quote']['peRatio'],
      'marketCap': data[symbol]['quote']['marketCap'],
      'week52High': data[symbol]['quote']['week52High'],
      'week52Low': data[symbol]['quote']['week52Low'],
      'priceToBook': data[symbol]['advanced-stats']['priceToBook'],
      'priceToSales': data[symbol]['advanced-stats']['priceToSales'],
      #'error_message': ''
      })
    except:
      print('try again')
  
  else: 
    return HttpResponse('index')

  return render(request, 'index.html')