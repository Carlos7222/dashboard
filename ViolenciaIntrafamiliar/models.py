from django.db import models

# Create your models here.
class ViolenciaIntrafamiliar(models.Model):
    ano=models.CharField(primary_key=True,max_length=6)
    Ncasos=models.PositiveIntegerField()
    AdultoMayor=models.PositiveIntegerField()
    NiñoAdolecente=models.PositiveIntegerField()
    OtrosFamiliares=models.PositiveIntegerField()
    Pareja=models.PositiveIntegerField()
    