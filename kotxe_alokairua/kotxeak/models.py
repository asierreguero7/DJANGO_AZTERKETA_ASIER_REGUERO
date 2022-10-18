from django.db import models

class Kotxeak(models.Model):
  marka = models.CharField(max_length=255)
  modeloa = models.CharField(max_length=255)
  matrikula = models.CharField(max_length=7)