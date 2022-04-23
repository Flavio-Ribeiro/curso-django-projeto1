from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('home2')


def contato(request):
    return HttpResponse('contato2')


def sobre(request):
    return HttpResponse('sobre2')
