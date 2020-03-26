from django.db import models
from authentication.models import User


class ShopProfile(models.Model):
    shop_name           =   models.CharField(max_length=120,blank=False,null=False)
    address_line_1      =   models.CharField(max_length=120,blank=False,null=False)
    address_line_2      =   models.CharField(max_length=120,blank=False,null=False)
    address_line_3      =   models.CharField(max_length=120,blank=True,null=True)
    town_city           =   models.CharField(max_length=120,blank=False,null=False)
    country             =   models.CharField(max_length=120,blank=False,null=False)
    contact             =   models.IntegerField()
    email_address       =   models.EmailField(unique=True)
    timming             =   models.IntegerField()
    shop_details        =   models.TextField()





    def __str__(self):
        return self.shop_name
