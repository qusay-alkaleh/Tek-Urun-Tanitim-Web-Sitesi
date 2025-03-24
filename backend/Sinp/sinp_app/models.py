from django.db import models

# Create your models here.


class ProductA(models.Model):

    name=models.CharField(max_length=60)
    price=models.DecimalField(max_digits=7 , decimal_places=2)
