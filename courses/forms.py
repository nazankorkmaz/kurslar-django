from django import forms

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
