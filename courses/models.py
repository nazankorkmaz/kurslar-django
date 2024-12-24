from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank = False)
    date = models.DateField()
    isActive = models.BooleanField()

    """
    blank=False ise ve kullanıcı bir formda bu alanı doldurmazsa, Django bir ValidationError fırlatır.
    """
    """
    Eğer veritabanı düzeyinde bir kontrol istiyorsanız, null kullanmanız gerekir. Örneğin:
blank=True, null=True: Hem formda boş bırakılabilir, hem de veritabanında NULL değeri alabilir.
    """

    def __str__(self):
        return f"{self.title} {self.description}"