from django.db import models

# Create your models here.

class MatriculaEscolares(models.Model):
    ano=models.CharField(primary_key=True,max_length=6)
    Nmatriculados=models.PositiveIntegerField()
    preescolar=models.PositiveIntegerField()
    primaria=models.PositiveIntegerField()
    basicaSecundarioa=models.PositiveIntegerField()
    media=models.PositiveIntegerField()