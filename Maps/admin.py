from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(Crimes2001)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'lat', 'lon')

admin.site.register(Coordenadas, CourseAdmin)


class Crime(admin.ModelAdmin):
    list_display = ('id','caseno', 'block', 'Type', 'Type_desc', 'Where', 'Arrest', 'Domestic', 'District', 'Community_area', 'Year', 'Latitude', 'Longitude')

admin.site.register(Crimes2001, Crime)