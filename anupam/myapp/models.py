from django.db import models

# Create your models here.
class About(models.Model):
    short_discripition = models.CharField(max_length=300)
    birthday=models.DateField(max_length=10)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=20)

    def __str__(self):
        return self.short_discripition
