from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse('anasayfa')

def kurslar(request):
    return HttpResponse('kurs listesi..')