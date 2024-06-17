from django.urls import path
from .views import *
from main import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('map/', map_page, name='map_page'),
]