from django.urls import path
from .views import RegisterAPIView,CreateProfileAPIView,RetrieveProfileAPIView

urlpatterns=[
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('profile/create/',CreateProfileAPIView.as_view(),name='create profile'),
    path('profile/<pk>/',RetrieveProfileAPIView.as_view(),name='profile')


]
