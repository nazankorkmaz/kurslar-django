from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('mobil-uygulama',views.mobilUygulama),
    path('<kurs_id>',views.details, name="course_details"),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategory, name = 'courses_by_category')
 
]

"""
<> içindeki isim, bir değişken adıdır. Bu, URL'nin o kısmındaki değeri yakalar ve view fonksiyonuna bir argüman olarak iletir.
"""

"""
2. 'courses_by_category' Neyi İfade Ediyor?
urls.py dosyasında belirtilen URL'nin adıdır (name). Bu isim, Django'nun URL yönlendirme sistemi tarafından tanınır.
name='courses_by_category':
Bu URL'yi bir isimle tanımlıyor.
"""