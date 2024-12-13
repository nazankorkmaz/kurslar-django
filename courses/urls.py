from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('mobil-uygulama',views.mobilUygulama),
    path('<kurs>',views.details),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategory, name = 'courses_by_category')
 
]
