from django.shortcuts import render
import django
import requests


def app(request):
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao = cotacao.json()
    bid = cotacao['USDBRL']['bid']
    time = cotacao['USDBRL']['create_date']
    return render(request, 'home.html', {'dollar': bid, 'time': time})
