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
      response = requests.get(f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol}&types=quote,advanced-stats&token={CLOUD_API_KEY}')
      data = response.json()

      return render(request, 'index.html', {
      'companyName': data[symbol]['quote']['companyName'],
      'symbol': f'({symbol})',
      'latestPrice': f"${data[symbol]['quote']['latestPrice']}",
      'peRatio': data[symbol]['quote']['peRatio'],
      'marketCap': f"{data[symbol]['quote']['marketCap']/1000000000}",
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

def top50(request):
  return render(request, 'top50.html')