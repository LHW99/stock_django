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
      'week52High': f"${data[symbol]['quote']['week52High']}",
      'week52Low': f"${data[symbol]['quote']['week52Low']}",
      'priceToBook': data[symbol]['advanced-stats']['priceToBook'],
      'priceToSales': data[symbol]['advanced-stats']['priceToSales'],
      })
    except:
      return render(request, 'index.html')
  
  else: 
    return HttpResponse('index')

  return render(request, 'index.html')

def top50gain(request):
  if request.method == 'GET':
    try:
      time = request.GET.get('timer')
      df = rv_dataframe
      df.sort_values(f"Percentage Change ({time})", ascending = False, inplace = True)
      df = df[:50]
      df.reset_index(drop = True, inplace = True)
      df = df.to_html()
      return render(request, 'top50gain.html', {'df': df})
    except:
      df = rv_dataframe
      df.sort_values('Percentage Change (5-Years)', ascending = False, inplace = True)
      df = df[:50]
      df.reset_index(drop = True, inplace = True)
      df = df.to_html()
      return render(request, 'top50gain.html', {'df': df})

  return render(request, 'top50gain.html', {'df': df})

def top50loss(request):
  if request.method == 'GET':
    try:
      time = request.GET.get('timer')
      df = rv_dataframe
      df.sort_values(f"Percentage Change ({time})", ascending = True, inplace = True)
      df = df[:50]
      df.reset_index(drop = True, inplace = True)
      df = df.to_html()
      return render(request, 'top50loss.html', {'df': df})
    except:
      df = rv_dataframe
      df.sort_values('Percentage Change (5-Years)', ascending = True, inplace = True)
      df = df[:50]
      df.reset_index(drop = True, inplace = True)
      df = df.to_html()
      return render(request, 'top50loss.html', {'df': df})

  return render(request, 'top50loss.html', {'df': df})

def top50pe(request):
  df = rv_dataframe
  df.sort_values('P/E Ratio', ascending = False, inplace = True)
  df = df[:50]
  df.reset_index(drop = True, inplace = True)
  df = df.to_html()

  return render(request, 'top50pe.html', {'df': df})

def all(request):
  df = rv_dataframe.to_html()

  return render(request, 'all.html', {'df': df})
