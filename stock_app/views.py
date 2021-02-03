from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from keys import *
import requests
from stock_dataframe import rv_dataframe

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
      })
    except:
      return render(request, 'index.html')
  
  else: 
    return HttpResponse('index')

  return render(request, 'index.html')

def top50(request):
  df = rv_dataframe.to_html()
  
  return render(request, 'top50.html', {'df': df})

def watchlist(request):
  return render(request, 'watchlist.html')