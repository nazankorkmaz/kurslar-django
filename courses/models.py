from django.db import models
from django.utils.text import slugify

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank = False)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="",null=False,blank=True,editable=False,unique=True,db_index=True)  # null olmasin ve default bos gelsin

    """
    blank=False ise ve kullanıcı bir formda bu alanı doldurmazsa, Django bir ValidationError fırlatır.
    """
    """
    Eğer veritabanı düzeyinde bir kontrol istiyorsanız, null kullanmanız gerekir. Örneğin:
blank=True, null=True: Hem formda boş bırakılabilir, hem de veritabanında NULL değeri alabilir.
    """

    def save(self,*args,**kwargs): # default hali cagirildi
        self.slug = slugify(self.title) # ayri olarak burasi eklendi
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.title} {self.description}"


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"