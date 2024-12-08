from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('anasayfa')

def iletisim(request):
    return HttpResponse('iletişim')

def hakkimizda(request):
    return HttpResponse('hakkımızda')

