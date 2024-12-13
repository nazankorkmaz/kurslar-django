from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('anasayfa',views.index),
    path('contact',views.contact),
    path('about',views.about),
    path('iletisim',views.iletisim),
    path('hakkimizda',views.hakkimizda),
 
]
