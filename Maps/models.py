from django.db import models

# Create your models here.
class Coordenadas(models.Model):
    lat = models.FloatField(max_length=20)
    lon = models.FloatField(max_length=20)
    # created_at = models.DateTimeField(auto_now_add=True)



    # 'caseno' : tempDF['caseno'][i],	
    #             'block' : tempDF['caseno'][i],
    #             'Type' : tempDF['caseno'][i],
    #             'Type_desc' : tempDF['caseno'][i],
    #             'Where' : tempDF['caseno'][i],
    #             'Arrest' : tempDF['caseno'][i],
    #             'Domestic' : tempDF['caseno'][i],
    #             'District' : tempDF['caseno'][i],
    #             'Community_area' : tempDF['caseno'][i],
    #             'Year' : tempDF['caseno'][i],
    #             'Latitude' : tempDF['caseno'][i],
    #             'Longitude' : tempDF['caseno'][i],
# Create your models here.
class Crimes2001(models.Model):
    caseno = models.CharField(max_length=20)
    Date = models.DateTimeField(auto_now_add=True)
    block = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Type_desc = models.CharField(max_length=100)
    Where = models.CharField(max_length=100)
    Arrest = models.BooleanField()
    Domestic = models.BooleanField()
    District = models.IntegerField()
    Community_area = models.FloatField(null=True)
    Year = models.IntegerField()
    Latitude = models.FloatField(max_length=20, null=True)
    Longitude = models.FloatField(max_length=20, null=True)

