from django.db import models

# Create your models here.
class destination(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)