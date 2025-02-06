from django.contrib import admin

# Register your models here.
from .models import Course,Category, Slider

# 1. yontem
"""
class CourseAdmin(admin.ModelAdmin):
    pass 
    # buraya istenen ozellikler yazilir

admin.site.register(Course,CourseAdmin)
"""

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","isHome","slug","category_list") #hangileri gozuksun listelemede
    list_display_links = ("title","slug",)  #hangileri link olsun
    readonly_fields = ("slug",) #burasini model.pyDa kaldırmıstık ama simdi sadece okunabilir olarak gozukuyor
    list_filter = ("isActive","title","isHome") #sag taradfa filtreleme kısmı cıktı
    list_editable = ("isActive","isHome") #onceden icine girip yaman lazımdı simdi checkbox oldu
    search_fields = ("title","descriptions") # ustte arama cubugu cıktı

    def category_list(self,obj): # obj yani sirayla gelen kurs
        html=""
        for category in obj.categories.all():
            html += category.name + ", "
        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",),} #name dolsurulurken slug'da kendisi otomatik yazar asagida
    list_display = ("name","slug","course_count") #hangileri gozuksun listelemede
    list_filter = ("name",) #sag taradfa filtreleme kısmı cıktı
   
    def course_count(self,obj):
        return obj.course_set.count()
    
admin.site.register(Slider)