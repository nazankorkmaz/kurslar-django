from django import forms

from courses.models import Course
"""
class CourseCreateForm(forms.Form):
    title = forms.CharField(
        label="kurs başlığı",
        required=True,
        error_messages={"required": "Please enter your name"},# bu sekilde form properties eklenebilir
        widget = forms.TextInput(attrs={"class":"form-control"}) # form alani kullaniciya nasil gozuksun
        ) 
        
    description = forms.CharField(widget = forms.Textarea(attrs={"class":"form-control"}))
    imageUrl = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
    slug = forms.SlugField(widget = forms.TextInput(attrs={"class":"form-control"}))


"""
# 2.Yontem : MODELFORM CLASS
class CourseCreateForm(forms.ModelForm):
    
    # bir alt sinif olusturuluyor. Yani hazir olan Course sınıfının ozelliklerini cekicez sifirdan yazmak yerine
    class Meta:
        model = Course
        fields = ('title','description','imageUrl') #"__all__" # bunda direk hepsi geliyor
        labels ={
            "title" :"kurs başlığı",
            "description":"açıklama"
        }
    widgets ={
        "title" : forms.TextInput(attrs={"class":"form-control"}),
        "description":forms.Textarea(attrs={"class":"form-control"}),
        "imageUrl":forms.TextInput(attrs={"class":"form-control"})
    }
    error_messages ={
        "title" :{
            "required" :"kurs başlığı girmelisiniz.",
            "max_length":"maksimum 50 karakter girmelisiniz"
        },
        "description":{
            "required":"kurs açıklaması girmelisiniz."
        }
    }
      

class CourseEditForm(forms.ModelForm):
    
    # bir alt sinif olusturuluyor. Yani hazir olan Course sınıfının ozelliklerini cekicez sifirdan yazmak yerine
    class Meta:
        model = Course
        fields = ('title','description','imageUrl','categories','isActive',) #"__all__" # bunda direk hepsi geliyor
        labels ={
            "title" :"kurs başlığı",
            "description":"açıklama"
        }
    widgets ={
        "title" : forms.TextInput(attrs={"class":"form-control"}),
        "description":forms.Textarea(attrs={"class":"form-control"}),
        "imageUrl":forms.TextInput(attrs={"class":"form-control"}),
        "categories":forms.SelectMultiple(attrs={"class":"form-control"})
    }
    error_messages ={
        "title" :{
            "required" :"kurs başlığı girmelisiniz.",
            "max_length":"maksimum 50 karakter girmelisiniz"
        },
        "description":{
            "required":"kurs açıklaması girmelisiniz."
        }
    }
      