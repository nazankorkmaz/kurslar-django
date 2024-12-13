from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'pages/index2.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def home(request):
    return HttpResponse('anasayfa')

def iletisim(request):
    return HttpResponse('iletişim')

def hakkimizda(request):
    return HttpResponse('hakkımızda')

