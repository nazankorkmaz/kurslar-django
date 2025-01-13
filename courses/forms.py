from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(label="kurs başlığı",required=True,error_messages={"required": "Please enter your name"}) # bu sekilde form properties eklenebilir
    description = forms.CharField(widget=forms.Textarea)
    imageUrl = forms.CharField()
    slug = forms.SlugField()
