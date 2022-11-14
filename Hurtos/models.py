from django.db import models

# Create your models here.
class Hurtos(models.Model):
    ano=models.CharField(primary_key=True,max_length=6)
    Ncasos=models.PositiveIntegerField()
    residencia=models.PositiveIntegerField()
    personas=models.PositiveIntegerField()
    comercio=models.PositiveIntegerField()
    automotores=models.PositiveIntegerField()
    