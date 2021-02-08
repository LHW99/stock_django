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
      response = requests.get(f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol}&types=quote,stats,advanced-stats&token={CLOUD_API_KEY}')
      data = response.json()

      return render(request, 'index.html', {
      'companyName': data[symbol]['quote']['companyName'],
      'symbol': f'({symbol})',
      'latestPrice': f"${data[symbol]['quote']['latestPrice']}",
      'marketCap': f"Market Cap (Billions): {data[symbol]['quote']['marketCap']/1000000000:.2f}",
      'month1ChangePercent': f"1-Month Percentage Change: {data[symbol]['stats']['month1ChangePercent']*100:.2f}%",
      'month3ChangePercent': f"3-Month Percentage Change: {data[symbol]['stats']['month3ChangePercent']*100:.2f}%",
      'month6ChangePercent': f"6-Month Percentage Change: {data[symbol]['stats']['month6ChangePercent']*100:.2f}%",
      'year1ChangePercent': f"1-Year Percentage Change: {data[symbol]['stats']['year1ChangePercent']*100:.2f}%",  
      'week52High': f"52-Week High: ${data[symbol]['quote']['week52High']}",
      'week52Low': f"52-Week Low: ${data[symbol]['quote']['week52Low']}",
      'peRatio': f"Price-to-Earnings Ratio: {data[symbol]['quote']['peRatio']}",
      'priceToBook': f"Price-to-Book Ratio: {data[symbol]['advanced-stats']['priceToBook']}",
      'priceToSales': f"Price-to-Sales Ratio: {data[symbol]['advanced-stats']['priceToSales']}",
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
      df = df.to_html(index=False)
      return render(request, 'top50gain.html', {'df': df})
    except:
      df = rv_dataframe
      df.sort_values('Percentage Change (5-Years)', ascending = False, inplace = True)
      df = df[:50]
      df.reset_index(drop = True, inplace = True)
      df = df.to_html(index=False)
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
      df = df.to_html(index=False)
      return render(request, 'top50loss.html', {'df': df})
    except:
      df = rv_dataframe
      df.sort_values('Percentage Change (5-Years)', ascending = True, inplace = True)
      df = df[:50]
      df.reset_index(drop = True, inplace = True)
      df = df.to_html(index=False)
      return render(request, 'top50loss.html', {'df': df})

  return render(request, 'top50loss.html', {'df': df})

def top50pe(request):
  df = rv_dataframe
  df.sort_values('P/E Ratio', ascending = False, inplace = True)
  df = df[:50]
  df.reset_index(drop = True, inplace = True)
  df = df.to_html(index=False)

  return render(request, 'top50pe.html', {'df': df})

def all(request):
  df = rv_dataframe.to_html(index=False)

  return render(request, 'all.html', {'df': df})
