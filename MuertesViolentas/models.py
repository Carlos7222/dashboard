from django.db import models

# Create your models here.

class MuertesViolentas(models.Model):
    ano=models.CharField(primary_key=True,max_length=6)
    personas=models.PositiveIntegerField()
    suicidios=models.PositiveIntegerField()
    muertesAccidentes=models.PositiveIntegerField()
    muerteTransporte=models.PositiveIntegerField()
    homicidio=models.PositiveIntegerField()
    