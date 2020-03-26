from django.shortcuts import render
from .models import CustomerProfile
from .serializer import CustomerProfileSerializer
from rest_framework import  generics



class CreateProfileAPIView(generics.CreateAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       []




class EditProfileAPIView(generics.UpdateAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       []
    lookup_field            =       'username'


class CustomerListAPIView(generics.ListAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       []
