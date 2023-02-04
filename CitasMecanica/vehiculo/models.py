from django.db import models
from usuario.models import Profile

# Create your models here.
class Vehiculo(models.Model):
    duenio = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    placa=models.CharField(max_length=30, blank=True, null=True,verbose_name="placa" )
    marca=models.CharField(max_length=30, blank=True, null=True,verbose_name="marca" )
    modelo=models.CharField(max_length=30, blank=True, null=True,verbose_name="modelo" )
    anovehiculo=models.DateField(blank=True, null=True,verbose_name="año del vehiculo" )
    
    def __str__(self):
        return f"{self.placa}"

    class Meta:
        verbose_name = 'vehiculo'
        verbose_name_plural = 'vehiculos'
