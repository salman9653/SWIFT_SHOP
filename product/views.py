from django.shortcuts import render
from rest_framework import generics
from .models import Product
from django.db.models import Q
from .serializer import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    # queryset                =   Product.objects.all()
    serializer_class        =   ProductSerializer
    permission_classes      =   []
    authentication_classes  =   []



    def get_queryset(self):
        request    =    self.request
        queryset   =    Product.objects.all()
        query      =    request.GET.get('q')
        print(query)
        if query is not None:
            queryset     =    queryset.filter(Q(product_name__icontains=query)|
                                                Q(brand_name__icontains=query))
                                                # Q(shop__icontains=query))

        return queryset



class ProductCreateAPIView(generics.CreateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductSerializer
    permission_classes      =   []
    authentication_classes  =   []
