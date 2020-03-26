from django.urls import path
from .views import ProductCreateAPIView,ProductListAPIView


urlpatterns=[
    path('',ProductListAPIView.as_view(),name='products'),
    path('create/',ProductCreateAPIView.as_view(),name='create product')


]
