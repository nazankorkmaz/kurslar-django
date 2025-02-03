from django.shortcuts import get_object_or_404, render ,redirect
from django.urls import reverse
from datetime import date
# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404

from .models import Course,Category

from django.core.paginator import Paginator

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
            "imageUrl":"img1.png",
            "slug":"javascript-kursu",
            "date":date(2024,12,14),
            "isActive":True,
            "isUpdated":True

        },
        {
            "title":"python kursu",
            "description":"python kurs açıklaması",
            "imageUrl":"img2.png",
            "slug":"python-kursu",
            "date":date(2024,12,14),
            "isActive":False,
            "isUpdated":True

        },
        {
            "title":"web geliştirme kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"img3.png",
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
    kurslar = Course.objects.filter(isActive=1, isHome=1)
    #db["courses"]
    kategoriler = Category.objects.all()
    #db["categories"]

    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'courses':kurslar
    })
    """
    index.html şablonunu işlemeden önce kategoriler ve kursları veritabanından çeker, bu verileri şablona aktarır ve kullanıcıya işlenmiş HTML dosyasını döner.
    """

    """
       for category in category_list:
        redirect_url = reverse('courses_by_category', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"
    
    html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"
    return HttpResponse(html)
    """

def details(request,slug): #artik slug parametresinden slug degerini aliyorum

    try:
        course = Course.objects.get(slug=slug)
    except:
        raise Http404()
    context= {
        'course':course
    }

    return render(request,'courses/details.html',context)
    #return HttpResponse(f"{kurs} detay sayfası")


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
    #print(redirect_url) ---> /kurs/kategori/mobil
    #print(category_name) --> mobil

    return redirect(redirect_url)

"""
reverse şu adımları izliyor:

reverse, name='courses_by_category' olan URL'yi buluyor.
args=[category_name]: URL'ye dinamik olarak category_name değerini ekliyor
"""
 

"""
    redirect_text = category_list[category_id - 1]
    #return redirect('/kurs/kategori/'+ redirect_text)
    return HttpResponseRedirect('/kurs/kategori/'+redirect_text)
#    return HttpResponse(f"{category_id} kategorisine ait kurslar listesi int")

"""

def getCoursesByCategoryYeni(request,slug):
   
   kurslar = Course.objects.filter(categories__slug = slug, isActive=True).order_by("date")
   # bire çokta (category__slug = slug, isActive=True)
   kategoriler = Category.objects.all()

   paginator = Paginator(kurslar,1) # hangisini sayfalicaksan onu ve adetini ver
   page = request.GET.get('page',1) # yani url'de page varsa onu al o sayfayı dondur yoksa ilk sayfayi dondur
    #http://127.0.0.1:8000/kurs/kategori/programlama?page=2
   page_obj = paginator.page(page) # o sayfadaki gosterilecek kurs bilgilerini cektik

   print(page_obj.paginator.count)
   print(page_obj.paginator.num_pages)

   return render(request, 'courses/list.html',
                 {
                     'categories':kategoriler,
                     'page_obj':page_obj,#kurslar,
                     'seciliKategori':slug
                 })


#http://127.0.0.1:8000/kurs/search?q=web
def search(request):
    #print(request.GET)
    #print(request.GET["q"])
    #print(request.GET["order_by"])

    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True,title__contains=q).order_by("date")

        kategoriler = Category.objects.all()
    
    else:
        return redirect("/kurs")


    return render(request, 'courses/search.html',
                    {
                        'categories':kategoriler,
                        'courses':kurslar,
                    })

from courses.forms import CourseCreateForm, CourseEditForm
def create_course(request):
 
    if request.method == "POST":
        form = CourseCreateForm(request.POST) # form olusturuldu

        if form.is_valid(): # yani form duzgun doldurulmus ve gecerli ise
            """
            kurs = Course(
                title= form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                imageUrl = form.cleaned_data["imageUrl"],
                slug = form.cleaned_data["slug"]
            )
            kurs.save()
            """
            form.save()  #modelform metodu ile
            return redirect("/kurs") #kursu veritabanina ekle ve kusrlar sayfasina don
    else: # yani ilk burasi cagirilir.
        form = CourseCreateForm() # formu bos tekrar olustur ve sayfaya yolla 
    
    return render(request,"courses/create-course.html",{"form":form})
    

    # ilk yol html sayfasi ile kendisimiz manuel yapmistk
    """
    if request.method == "POST":
        title = request.POST["title"] # nameden geliyor forumlardaki
        description = request.POST["description"]
        slug = request.POST["slug"]
        imageUrl = request.POST["imageUrl"]
        isActive = request.POST.get("isActive",False) # isaretlenmemisse false versin defaultta
        isHome = request.POST.get("isHome",False)

        if isActive == "on":
            isActive = True
        
        if isHome == "on":
            isHome = True

        #error validation
        error = False
        msg = ""

        if title == "":
            error = True
            msg = "Title zorunlu bir alandır"
        
        if len(title)<5:
            error = True
            msg = "Title için en az 5 karakter girilmelidir."

        if error:
            return render(request,"courses/create-course.html",{"error":True,"msg":msg})

        print(title,description)
        
        #veritabanina kayit edildi
        kurs = Course(title=title,description=description,imageUrl=imageUrl,slug=slug,isActive=isActive,isHome=isHome)
        kurs.save()
        return redirect("/kurs")

    return render(request,'courses/create-course.html') 
    #bu sadece GET requestleri karsilar
"""

def course_list(request):
    kurslar = Course.objects.all()
    return render(request,'courses/course-list.html',
                  {
                      "courses":kurslar
                  })

def course_edit(request, id):
    course = get_object_or_404(Course,pk=id)   # id degeri ile eslesen kurs gelsin

    #buradada post edilen bilgilerle veritabanina sql sorgusu gonderilir ve kaydedilir
    if request.method == "POST":
        form = CourseEditForm(request.POST,instance=course)
        form.save()
        return redirect("course_list")
    else:

        form = CourseEditForm(instance=course)  # form nesnesini ilgli kurs bilgisi ile olusturur

    return render(request, "courses/edit-course.html",{"form":form})


def course_delete(request, id):
    course = get_object_or_404(Course,pk = id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    
    return render(request,"courses/course-delete.html", {"course":course})

def upload(request):

    if request.method == "POST":
        uploaded_name = request.FILES["image"] # name'den geldi htmldeki 
        print(uploaded_name)
        print(uploaded_name.size)
        print(uploaded_name.content_type)

        return render(request, "courses/success.html")

    return render(request, "courses/upload.html")