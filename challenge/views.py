from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'challenge/home.html', context={
        'user': 'Julia'
    })


def desafio(request):
    return HttpResponse("Estamos na página desafio.")
