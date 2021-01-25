from django.shortcuts import render
from keys import *
import requests
import pyEX as p
#api_call = p.Client(api_token=CLOUD_API_KEY, version='sandbox')

# Create your views here.
def index(request):
  response = requests.get(f'https://sandbox.iexapis.com/stable/stock/AAPL/quote?token={CLOUD_API_KEY}')
  data = response.json()
  return render(request, 'index.html', {
    'symbol': data['symbol'],
    'latestPrice': data['latestPrice']
  })