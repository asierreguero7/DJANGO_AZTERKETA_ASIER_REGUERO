from django.db import models

class Alokairuak(models.Model):
  pertsona_id = models.IntegerField()
  kotxea_id = models.IntegerField()
  hasiera_data = models.CharField(max_length=255)
  amaiera_data = models.CharField(max_length=255)