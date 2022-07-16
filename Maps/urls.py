from django.contrib import admin
from django.urls import path
from . import views
from Maps.views import CrimeDetials

urlpatterns = [
     path('',views.coordinates_form, name = 'coordinates-form'),
     path('map', views.maps, name = 'maps'),
     path('crime/',CrimeDetials.as_view(), name = 'crime-details'),
  ]