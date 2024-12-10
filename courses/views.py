from django.shortcuts import render ,redirect
from django.urls import reverse
# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

data ={
     "programlama": "programlama kategorisine ait kurslar",
    "web-gelistrime":" web gelistrime kategorisine ait kurslar",
    "mobil": "mobil kategorisine ait kurslar"   
       }

def kurslar(request):
    #return HttpResponse('kurs listesi..')
    list_items=""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url = reverse('courses_by_category', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"
    
    html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"
    return HttpResponse(html)

def details(request,kurs):
    return HttpResponse(f"{kurs} detay sayfası")


def mobilUygulama(request):
    return HttpResponse("mobil uygulamalar kurs listesi")

def getCoursesByCategory(request,category_name):
   
    
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponse(f"{category_name} kategorisine ait kurslar listesi string")

def getCoursesByCategoryId(request,category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi yapıldı.")
    
    category_name = category_list[category_id - 1]
    redirect_url = reverse('courses_by_category', args=[category_name])
    return redirect(redirect_url)

    """
    redirect_text = category_list[category_id - 1]
    #return redirect('/kurs/kategori/'+ redirect_text)
    return HttpResponseRedirect('/kurs/kategori/'+redirect_text)
#    return HttpResponse(f"{category_id} kategorisine ait kurslar listesi int")

"""