from django.db import models

# Create your models here.

class User(models.Model):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    company_name = models.CharField(max_length=200)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=5)
    email = models.EmailField()
    web = models.URLField(max_length=200)
    

    def __str__(self):
        return self.first_name


