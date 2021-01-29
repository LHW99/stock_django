from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from keys import *
import requests
import pyEX as p
#api_call = p.Client(api_token=CLOUD_API_KEY, version='sandbox')

def index(request):
  if request.method == 'GET':
    try:
      ticker = request.GET['ticker_search']
      symbol = ticker.upper()
      response = requests.get(f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol}&types=quote,news,chart&token={CLOUD_API_KEY}')
      #response = requests.get(f'https://sandbox.iexapis.com/stable/stock/{symbol}/batch?types=quote&token={CLOUD_API_KEY}')
      #response = requests.get(f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={CLOUD_API_KEY}')
      data = response.json()

      return render(request, 'index.html', {
      'symbol': symbol,
      'latestPrice': data[symbol]['quote']['latestPrice'],
      'error_message': ''
      })
    except:
      print('try again')
  
  else: 
    return HttpResponse('index')

  return render(request, 'index.html')