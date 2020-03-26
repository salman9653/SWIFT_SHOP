from django.db import models
from django.contrib.auth.models import AbstractUser
# from utils.models   import  BaseAbstarctModel




class User(AbstractUser):
    user_choice=(('SHOPKEEPER','shopkeeper'),('DELIVERY_PERSON','delivery person'),('CUSTOMER','customer'))
    email           =   models.EmailField(unique=True,blank=False)
    role            =   models.CharField(verbose_name='user role',choices=user_choice,max_length=20,default='CUSTOMER')


class Profile(models.Model):

    user               =    models.OneToOneField(User,on_delete=models.CASCADE)
    first_name         =    models.CharField(max_length=120,null=True)
    last_name          =    models.CharField(max_length=120,null=True)
    email              =    models.EmailField(unique=True,null=True)

    def    __str__(self):
        return self.user
