from django.shortcuts import render
from keys import *
import requests
import pyEX as p
#api_call = p.Client(api_token=CLOUD_API_KEY, version='sandbox')

# Create your views here.
def index(request):
  symbol = 'AAPL'
  response = requests.get(f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={CLOUD_API_KEY}')
  data = response.json()

  if request.method == 'GET':
    ticker = request.GET['ticker_search']
    symbol = ticker.upper()
    response = requests.get(f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={CLOUD_API_KEY}')
    data = response.json()
    print(data)
    #return render(request, 'index.html', {
    #'symbol': data['symbol'],
    #'latestPrice': data['latestPrice']
    #})

  else:
    return HttpResponse('index')

  return render(request, 'index.html')

#  def get_queryset(self):
#    search = requests.GET['search']
#    symbol = search.upper()
#    if 'search' in request.GET:
#      return render(request, 'index.html', {
#        'symbol': data['symbol'],
#        'latestPrice': data['latestPrice']
#        })
#    else:
#      return render(request, 'index.html')
#    return render(request, 'index.html')