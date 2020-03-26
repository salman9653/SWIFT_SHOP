from django.db import models
from authentication.models import User
from product.models import Product



class Cart(models.Model):
    Cart_name   =       models.CharField(max_length=10,default='cart')
    User        =       models.OneToOneField(User,on_delete=models.CASCADE)
    products    =       models.ManyToManyField(Product)



    def __str__(self):
        return  self.Cart_name
