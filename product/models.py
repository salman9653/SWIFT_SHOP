from django.db import models
from shopkeeper.models import ShopProfile



class Product(models.Model):
    # product_id      =   models.BigAutoField()
    shop            =   models.ForeignKey(ShopProfile,on_delete=models.CASCADE)
    product_name    =   models.CharField(max_length=120,blank=False,null=False)
    # product_code    =   models.
    product_price   =   models.IntegerField()
    product_color   =   models.CharField(max_length=120)
    product_size    =   models.CharField(max_length=120)
    brand_name      =   models.CharField(max_length=120)
    quantity        =   models.IntegerField()
    description     =   models.TextField()




    def __str__(self):
        return  self.product_name
