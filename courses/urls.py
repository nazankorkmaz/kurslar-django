from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="index"),
    path('search',views.search, name = "search"),
    path('mobil-uygulama',views.mobilUygulama),
    path('create_course',views.create_course, name="create_course"),
    path('course-list',views.course_list,name="course_list"),
    path('course-edit/<int:id>', views.course_edit, name="course_edit"),
    path('<slug:slug>',views.details, name="course_details"),

    #path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    #path('kategori/<str:category_name>',views.getCoursesByCategory, name = 'courses_by_category')
    path('kategori/<slug:slug>',views.getCoursesByCategoryYeni,name='courses_by_category'),

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