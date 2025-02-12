from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(default="",null=False,blank=True,unique=True,db_index=True) 


    def __str__(self):
        return f"{self.name}"

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)

    subtitle = models.CharField(max_length=100,default="")
    description = RichTextField()

    #imageUrl = models.CharField(max_length=50, blank = False)
    image = models.ImageField(upload_to="images",default="")
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False,blank=True,editable=False,unique=True,db_index=True)  # null olmasin ve default bos gelsin
    categories = models.ManyToManyField(Category)


    # category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE, related_name="kurslar" ) # onceki kayitlarda hata vermesin diye defaulttta id'si 1 olan categoryleri alsin dedik

    # models.CASCADE : mesela bir kategori silinirse ona bagli tum kurslar silinsin demek
    #models.SET_NULL : kategorsi isilinirse o kurslar silinmesin o sutuna Null atsin ama bunun için bir de null = True da yazman lazim null alabilen bir sutun olmasi icin
    # ya da models.SET_DEFAULT yapip default =1 deger de verebirlisin
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


class UploadModels(models.Model):
    image = models.ImageField(upload_to="images")

# settings.py'a eklendi -->  MEDIA_ROOT = BASE_DIR / "uploads"

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    is_active= models.BooleanField(default=False)
    course= models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"