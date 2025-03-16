from django.db import models

# Create your models here.



class Product(models.Model):

    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=100 ,decimal_places=2)
    pub_date=models.DateTimeField(auto_now_add=True)
