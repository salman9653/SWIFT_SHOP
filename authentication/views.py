from django.shortcuts import render
from .serializer import RegisterSerializer,ProfileSerializer
from rest_framework import generics,mixins
from .models import User,Profile




class    RegisterAPIView(generics.CreateAPIView):
     queryset               =   User.objects.all()
     permission_classes     =   []
     authentication_classes =   []
     serializer_class       =   RegisterSerializer


class    CreateProfileAPIView(generics.CreateAPIView):
    queryset               =   Profile.objects.all()
    permission_classes     =   []
    authentication_classes =   []
    serializer_class       =   ProfileSerializer

class   RetrieveProfileAPIView(generics.RetrieveAPIView):
    queryset               =   Profile.objects.all()
    permission_classes     =   []
    authentication_classes =   []
    serializer_class       =   ProfileSerializer
    lookup_field           =    'pk'
