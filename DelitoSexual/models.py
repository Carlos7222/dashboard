from django.db import models

# Create your models here.

class DelitoSexuales(models.Model):
    ano=models.CharField(primary_key=True,max_length=6)
    Ncasos=models.PositiveIntegerField()
    hombres=models.PositiveIntegerField()
    mujeres=models.PositiveIntegerField()