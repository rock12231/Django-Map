from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(Coordenadas)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'lat', 'lon')

admin.site.register(Coordenadas, CourseAdmin)