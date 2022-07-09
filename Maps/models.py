from django.db import models

# Create your models here.
class Coordenadas(models.Model):
    lat = models.FloatField(max_length=20)
    lon = models.FloatField(max_length=20)
    # created_at = models.DateTimeField(auto_now_add=True)
