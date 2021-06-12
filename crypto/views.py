from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,CHZ,BNB,XRP,ADA,DOGE,DOT,LTC,BUSD&tsyms=USD'
coins_list = ['Bitcoin','Ethereum','Chilliz','Binance Coin','XRP','Cardano','Dogecoin','Polkadot','Litecoin','BUSD']

def home(request):
    data = requests.get(url)
    data = json.loads(data.text)
    for i,(coin,val) in enumerate(data['DISPLAY'].items()):
        val['USD']['NAME'] = coins_list[i]
        val['USD']['IMAGEURL'] = 'https://www.cryptocompare.com'+val['USD']['IMAGEURL']
    context = {'coins':data['DISPLAY']}
    return render(request, 'crypto/index.html',context)
    #return HttpResponse("Hello World from kryptex")
