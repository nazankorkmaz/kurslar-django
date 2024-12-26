from django.contrib import admin

# Register your models here.
from .models import Course,Category

# 1. yontem
"""
class CourseAdmin(admin.ModelAdmin):
    pass 
    # buraya istenen ozellikler yazilir

admin.site.register(Course,CourseAdmin)
"""

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","category") #hangileri gozuksun listelemede
    list_display_links = ("title","slug",)  #hangileri link olsun
    readonly_fields = ("slug",) #burasini model.pyDa kaldırmıstık ama simdi sadece okunabilir olarak gozukuyor
    list_filter = ("isActive","title","category") #sag taradfa filtreleme kısmı cıktı
    list_editable = ("isActive",) #onceden icine girip yaman lazımdı simdi checkbox oldu
    search_fields = ("title","descriptions") # ustte arama cubugu cıktı

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",),} #name dolsurulurken slug'da kendisi otomatik yazar asagida
    list_display = ("name","slug") #hangileri gozuksun listelemede
    list_filter = ("name",) #sag taradfa filtreleme kısmı cıktı
   