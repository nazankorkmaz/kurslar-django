from django.shortcuts import render ,redirect
from django.urls import reverse
from datetime import date
# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

data ={
     "programlama": "programlama kategorisine ait kurslar",
    "web-gelistrime":" web gelistrime kategorisine ait kurslar",
    "mobil": "mobil kategorisine ait kurslar"   
       }


db ={
    "courses" : [
        {
            "title":"javascript kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUIBJNkSlQuS47lGQ7_X7AHayZaNUQviEvbQ&s",
            "slug":"javascript-kursu",
            "date":date(2024,12,14),
            "isActive":True,
            "isUpdated":True

        },
        {
            "title":"python kursu",
            "description":"python kurs açıklaması",
            "imageUrl":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQP2jemoAzbrIwUtn3kWI49jYMm8wQsk3OHug&s",
            "slug":"python-kursu",
            "date":date(2024,12,14),
            "isActive":False,
            "isUpdated":True

        },
        {
            "title":"web geliştirme kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"https://e7.pngegg.com/pngimages/887/666/png-clipart-web-development-mobile-app-development-software-development-android-gadget-text.png",
            "slug":"web-kursu",
            "date":date(2024,12,18),
            "isActive":True,
            "isUpdated":False


        }
    ],
    "categories":[
        {id:1, "name":"programlama","slug":"programlama"},
        {id:2, "name":"web geliştirme","slug":"web-geliştirme"},
        {id:3, "name":"mobil uygulamar","slug":"mobil-uygulamar"},
    ]
}

#http://127.0.0.1:8000/kurslar

def index(request):
    #return HttpResponse('kurs listesi..')
    kurslar = db["courses"]
    kategoriler = db["categories"]

    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'courses':kurslar
    })

    """
       for category in category_list:
        redirect_url = reverse('courses_by_category', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"
    
    html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"
    return HttpResponse(html)
    """

def details(request,kurs):
    return HttpResponse(f"{kurs} detay sayfası")


def mobilUygulama(request):
    return render(request,'index.html')
    #return HttpResponse("mobil uygulamalar kurs listesi")

def getCoursesByCategory(request,category_name):
   
    try:
        category_text = data[category_name]
        return render(request,"courses/kurslar.html",
                      {
                          'category':category_name,
                          'category_text':category_text
                      })
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